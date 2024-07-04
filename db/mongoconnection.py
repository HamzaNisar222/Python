#db/mongoconnection.py

import pymongo

class MongoDB:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="example_db", collection_name="example_collection"):
        self.client = pymongo.MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
        print(f"Connected to MongoDB database: {db_name}, collection: {collection_name}")

    def insert_document(self, document):
        result = self.collection.insert_one(document)
        print(f"Document inserted with id: {result.inserted_id}")

    def read_documents(self, query={}):
        documents = self.collection.find(query)
        return list(documents)

    def update_document(self, query, new_values):
        result = self.collection.update_one(query, {"$set": new_values})
        print(f"Documents matched: {result.matched_count}, updated: {result.modified_count}")

    def delete_document(self, query):
        result = self.collection.delete_one(query)
        print(f"Documents deleted: {result.deleted_count}")

    def close_connection(self):
        self.client.close()
        print("MongoDB connection closed.")
