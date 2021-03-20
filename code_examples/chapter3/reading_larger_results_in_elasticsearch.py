from elasticsearch import Elasticsearch
from pprint import pprint

es = Elasticsearch()
res = es.search(
        index = 'users',
        doc_type = 'doc',
        scroll = '20m',
        size = 100,
        body = {"query":{"match_all":{}}}
    )

# Save the scroll id to do the next scroll
sid = res['_scroll_id']

# Total of records in this scroll
size = res['hits']['total']['value']

# Save partial total to a list
total_data = res['hits']['hits']

while size > 0:
    res = es.scroll(scroll_id = sid, scroll = '20m')
    print('Found:', size)
    sid = res['_scroll_id']
    size = len(res['hits']['hits'])
    total_data.extend(res['hits']['hits'])

print('total_data len:', len(total_data))