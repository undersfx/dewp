import datetime as dt

import pandas as pd
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator


def csv_names_to_json():
    df = pd.read_csv('dags/data.csv')
    for _, r in df.iterrows():
        print(r['name'])
    df.to_json('logs/from_airflow.json', orient='records')

default_args = {
    'owner': 'Thiago Rodrigues',
    'start_date': dt.datetime(2021, 3, 17),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5)
}

with DAG('my_csv_dag',
        default_args=default_args,
        schedule_interval=dt.timedelta(minutes=5)
        ) as dag:
    print_starting = BashOperator(
            task_id='starting',
            bash_command='echo "I am reading the CSB now..."'
        )

    csv_to_json = PythonOperator(
            task_id='convert_csv_to_json',
            python_callable=csv_names_to_json
        )

print_starting >> csv_to_json  # Same as: print_starting.set_downstream(csv_to_json)
