from faker import Faker
import json


with open('data.json', 'w') as file:
    fake = Faker()
    all_data = {}
    all_data['records'] = []
    for _ in range(1000):
        data = {
            "name": fake.name(),
            "age":fake.random_int(min=18, max=80, step=1),
            "street":fake.street_address(),
            "city":fake.city(),"state":fake.state(),
            "zip":fake.zipcode(),
            "lng":float(fake.longitude()),
            "lat":float(fake.latitude())
        }
        all_data['records'].append(data)

    json.dump(all_data, file)
