import psycopg2 as db
from faker import Faker


fake = Faker()
data = []
n = 1 # Starting ID
m = 1001 # Ending ID (-1)

for i in range(n, m):
    data.append((i, fake.name(), fake.street_address(), fake.city(), fake.zipcode()))

data = tuple(data)

connection_params="dbname='dataengineering' host='localhost' user='airflow' password='airflow'"
connection = db.connect(connection_params)
cursor = connection.cursor()
query = "insert into users (id,name,street,city,zip) values (%s,%s,%s,%s,%s)"

mogrify = cursor.mogrify(query, data[0])
print("Query will be sent this way:", mogrify)

cursor.executemany(query,data)
connection.commit()