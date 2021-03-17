from os import openpty
import pandas as pd


# Read from CSV
df = pd.read_csv('data.csv')
print('Read from CSV result: \n', df.head(5), end='\n\n\n')

# Read from Object
data = {
    'Name': ['Paul', 'Bob', 'Susan', 'Yolanda'], 
    'Age': [23, 45, 18, 21]
    }
df = pd.DataFrame(data)
print('Read from Object result: \n', df, end='\n\n\n')

# Write to CSV
df.to_csv('from_pandas.csv', index=False)


# Read from JSON
df = pd.read_json('data.json')
print('Read from JSON result: \n', df.head(5), end='\n\n\n')

# Normalize nested list 'records'
from pandas import json_normalize
import pandas.io.json as pd_json

with open('data.json', 'r') as file:
    data = pd_json.loads(file.read())
    df = json_normalize(data, record_path='records')
    print('json_normalized dataframe: \n', df.head(5), end='\n\n\n')

    print('Be aware of the data format when writing "to_json": \n', df.head(5).to_json(), end='\n\n\n')
    print('Or normalize with "orient": \n', df.head(5).to_json(orient='records'), end='\n\n\n')
