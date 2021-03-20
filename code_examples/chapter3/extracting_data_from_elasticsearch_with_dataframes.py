import pandas as pd
from pandas import json_normalize
from elasticsearch import Elasticsearch
from pprint import pprint


# Create connection
es = Elasticsearch()


# Query for everything
doc={"query":{"match_all":{}}}

# Query for named "Ronald Goodman" only
# doc={"query":{
#         "match":{"name":"Ronald Goodman"}
#         }}

# Filter out results by specific term
# doc={"query":{
#         "bool":{
#             "must":{"match":{"city":"Jamesberg"}},
#             "filter":{"term":{"zip":"63792"}}
#             }}}


# Query the rule to index "users"
res=es.search(index="users",body=doc,size=3)
pprint(res)

# Query for specific named user
# res=es.search(index="users",q="name:Ronald Goodman")


# Iterate in the values
for doc in res['hits']['hits']:
    print(doc['_source'])


# Loading data into a pandas DataFrame
df = json_normalize(res['hits']['hits'])
print(df)

