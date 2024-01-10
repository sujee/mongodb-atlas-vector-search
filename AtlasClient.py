from pymongo import MongoClient

class AtlasClient ():

    def __init__ (self, altas_uri, dbname):
        self.mongodb_client = MongoClient(altas_uri)
        self.database = self.mongodb_client[dbname]

    def find (self, collection_name, filter = {}, limit=10):
        collection = self.database[collection_name]
        items = list(collection.find(filter=filter, limit=limit))
        return items

    def vector_search(self, collection_name, index_name, attr_name, embedding_vector, limit=5):
        collection = self.database[collection_name]
        results = collection.aggregate([
            {
                '$vectorSearch': {
                    "index": index_name,
                    "path": attr_name,
                    "queryVector": embedding_vector,
                    "numCandidates": 50,
                    "limit": limit,
                }
            }
            ])
        return list(results)
