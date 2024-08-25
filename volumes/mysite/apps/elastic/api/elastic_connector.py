from elasticsearch import Elasticsearch

class Elastic:
    def __init__(self, host, port, user=None, password=None,index=None, aggs=None ) -> None:
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.index = index
        self.aggs = aggs

        self.client = Elasticsearch([f"http://{self.user}:{self.password}@{self.host}:{self.port}"])

    
    def create_index(self, index_name):
        self.client.indices.create(index=index_name)
        return f"index {index_name} is created."
    def create_row(self):
        self.client.index(index="mobile", id="3", document={"price1": 5000000})


    def aggregation(self):        
        print(self.aggs)
        response = self.client.search(
            index=self.index,
            body={
                "aggs": {
                    "average_age": {
                        "avg": {
                            "field": self.aggs
                        }
                    }
                }
            }
        )

        average_age = response["aggregations"]["average_age"]
        return average_age











# from elasticsearch import Elasticsearch
# from datetime import datetime

# def create_es_connection(host: str, port: int, api_key_id: str, api_key: str, user: str, pw: str) -> Elasticsearch:
#     client= Elasticsearch([f"http://{user}:{pw}@{host}:{port}"])
#     # client.indices.create(index='mobile')

    
#     client.index(index="mobile", id="8", document={"price1": 5000000})
    
#     response = client.search(
#         index="mobile",
#         body={
#             "aggs": {
#                 "average_age": {
#                     "meta": {
#                         "field": "price1"
#                     }
#                 }
#             }
#         }
#     )

#     # نمایش نتیجه
#     average_age = response["aggregations"]["average_age"]
#     print(average_age)

#     # print(client.get(index="javad-sl", id="3"))

#     # print(client.info())
#     # doc = {
#     #     "author": "kimchy",
#     #     "text": "Elasticsearch: cool. bonsai cool.",
#     #     "timestamp": datetime.now(),
#     # }
#     # resp = client.index(index="test-index", id=1, document=doc)
#     # print(resp["result"])

#     # resp = client.get(index="test-index", id=1)
#     # print(resp["_source"])

#     # client.indices.refresh(index="test-index")

#     # resp = client.search(index="test-index", query={"match_all": {}})
#     # print("Got {} hits:".format(resp["hits"]["total"]["value"]))
#     # for hit in resp["hits"]["hits"]:
#     #     print("{timestamp} {author} {text}".format(**hit["_source"]))

#     #  a = client.indices.create(index="my_index3", mappings=mappings)
#     #  print(a)
#     # print(client.get(index="test-index", id="1"))

#     # client.index(
#     #     index="my_index1",
#     #     id="1",
#     #     document={
#     #         "price":"1000"
#     #     }
#     # )
    

# create_es_connection(host="127.0.0.1", port="9200", user="javad", pw="Salam1234", api_key=None, api_key_id=None)
