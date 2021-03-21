import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

import pandas as pd
import psycopg2 as db
from elasticsearch import Elasticsearch


default_args = {
 'owner': 'Thiago Rodrigues',
 'start_date': dt.datetime(2021, 3, 20),
 'retries': 1,
 'retry_delay': dt.timedelta(minutes=5),
}


def query_postgresql_to_csv():
    # Connect with PostgreSQL
    connection_params="dbname='dataengineering' host='postgres_database' user='airflow' password='airflow'"
    connection = db.connect(connection_params)

    # Query database into DataFrame
    df = pd.read_sql("select name, city from users", connection)

    # Write to disk
    df.to_csv('postgres_data.csv')
    print(df)
    print("---> Data from postgresql saved to disk.")


def insert_elasticsearch_data():
    es = Elasticsearch({'elasticsearch'})
    df = pd.read_csv('postgres_data.csv')
    for i, r in df.iterrows():
        body = r.to_json()
        res = es.index(
                index='frompostgresql',
                doc_type='doc',
                body=body
            )
        print(res)


with DAG(
    'postgres_to_es_dag',
    default_args=default_args,
    schedule_interval=timedelta(minutes=60), # '0 * * * *',
) as dag:
    getData = PythonOperator(
        task_id='QueryPostgreSQL',
        python_callable=query_postgresql_to_csv
    )

    insertData = PythonOperator(
        task_id='InsertDataElasticsearch',
        python_callable=insert_elasticsearch_data
    )


getData >> insertData