import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

import pandas as pd


default_args = {
        'owner': 'Thiago Rodrigues',
        'start_date': dt.datetime(2021, 4, 1),
        'retries': 1,
        'retry_delay': dt.timedelta(minutes=5),
    }


def clean_scooter():
    df = pd.read_csv('dags/scooter.csv')
    df.drop(columns=['region_id'], inplace=True)
    df.columns=[name.lower() for name in df.columns]
    df['started_at'] = pd.to_datetime(df['started_at'], format='%m/%d/%Y %H:%M')
    df.to_csv('clean_scooter.csv')


def filter_scooter():
    df = pd.read_csv('clean_scooter.csv')
    from_date = '2019-05-23'
    to_date = '2019-06-03'
    filtered = df[(df['started_at'] > from_date) & (df['started_at'] < to_date)]
    filtered.to_csv('may23-june3.csv')


dag_args = {
        "dag_id": "clean_data",
        "default_args": default_args,
        "schedule_interval": timedelta(minutes=60)
    }

with DAG(**dag_args) as dag:
    clean_data = PythonOperator(task_id='clean', python_callable=clean_scooter)
    filter_data = PythonOperator(task_id='filter', python_callable=filter_scooter)
    copy_file = BashOperator(task_id='copy', bash_command='cp /opt/airflow/may23-june3.csv /opt/airflow/dags/')


clean_data >> filter_data >> copy_file
