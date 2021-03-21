from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan, bulk

ES_INDEX = "frompostgresql"
ES_DOCTYPE = "doc"
BULK_SIZE = 1000

query = {"query":{"match_all":{}}}

def stream_items(es, query):
    for e in scan(es, 
                  query=query, 
                  index=ES_INDEX,
                  doc_type=ES_DOCTYPE, 
                  scroll='1m',
                  _source=False):

        # There exists a parameter to avoid this del statement (`track_source`) but at my version it doesn't exists.
        del e['_score']
        e['_op_type'] = 'delete'
        yield e

es = Elasticsearch()
bulk(es, stream_items(es, query), chunk_size=BULK_SIZE)
