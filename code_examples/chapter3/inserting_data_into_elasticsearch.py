from elasticsearch import helpers
from elasticsearch.client import Elasticsearch
from faker import Faker

fake = Faker()
es = Elasticsearch()

# Create Payload
actions = [
        {"_index": "users", "_type": "doc", "_source": {
            "name": fake.name(),
            "street": fake.street_address(),
            "city": fake.city(),
            "zip":fake.zipcode()
            }
        } for _ in range(1000)
    ]

# Insert into Elasticsearch
res = helpers.bulk(es, actions)

print(res)
