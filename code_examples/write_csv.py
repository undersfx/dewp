from faker import Faker
import csv


with open('data.csv', 'w') as file:
    fake = Faker()
    header = ['name', 'age', 'street', 'city', 'state', 'zip', 'lng', 'lat']
    writer = csv.writer(file)
    writer.writerow(header)
    for r in range(1000):
        writer.writerow([
            fake.name(),
            fake.random_int(min=18, max=80),
            fake.street_address(),
            fake.city(),
            fake.state(),
            fake.zipcode(),
            fake.longitude(),
            fake.latitude(),
        ])
