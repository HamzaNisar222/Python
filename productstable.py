# productstable.py
from db import mongoconnection

def main():
    # Initialize the MongoDB connection
    mongo_db = mongoconnection.MongoDB(db_name="example_db", collection_name="example_collection")

    # # Insert a document
    # document = {
    #     "name": "John Doe",
    #     "age": 30,
    #     "city": "New York"
    # }
    # mongo_db.insert_document(document)

    # Read documents
    documents = mongo_db.read_documents()
    print("Documents in collection:")
    for doc in documents:
        print(doc)

    # Update a document
    query = {"name": "John Doe"}
    new_values = {"age": 31}
    mongo_db.update_document(query, new_values)

    # Read documents again to see the update
    documents = mongo_db.read_documents()
    print("Documents in collection after update:")
    for doc in documents:
        print(doc)

    # Delete a document
    mongo_db.delete_document(query)

    # Read documents again to see the deletion
    documents = mongo_db.read_documents()
    print("Documents in collection after deletion:")
    for doc in documents:
        print(doc)

    # Close the connection
    mongo_db.close_connection()

if __name__ == "__main__":
    main()
