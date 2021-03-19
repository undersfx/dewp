import psycopg2 as db

connection_params="dbname='dataengineering' host='localhost' user='airflow' password='airflow'"
connection = db.connect(connection_params)
cursor = connection.cursor()

query = "select * from users"
cursor.execute(query)

# cur.fetchone() # Return the a list with next tuple from select response
# cur.fetchmany(10) # Return a list with the next 10 tuples from select response
# cur.fetchall() # Return a list with all tuples of data from select response

# Alternative
for record in cursor:
    print(record)