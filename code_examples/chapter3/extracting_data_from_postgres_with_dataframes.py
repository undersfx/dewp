import psycopg2 as db
import pandas as pd

# Connect with PostgreSQL
connection_params="dbname='dataengineering' host='localhost' user='airflow' password='airflow'"
connection = db.connect(connection_params)

# Query database into DataFrame
df = pd.read_sql("select * from users", connection)

# Write to disk
df.to_json('data.json', orient='records')
