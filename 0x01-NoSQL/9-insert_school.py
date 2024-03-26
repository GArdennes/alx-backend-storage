#!/usr/bin/env python3
'''
9-insert_school
'''


def insert_school(mongo_collection, **kwargs):
    """
    Function that inserts a new document in a collection.

    Args:
        mongo_collection (pymongo.collection.Collection):
        A pymongo collection object.
        **kwargs: Additional arguments defining the document to insert.

    Returns:
        ObjectId: The ObjectId of the inserted document.

    Raises:
        pymongo.errors.PyMongoError: If an error occurs during insertion.
    """
    result = mongo_collection.insert_one(**kwargs)
    if result.inserted_id:
        return result.inserted_id
    else:
        raise pymongo.errors.PyMongoError("Insertion failed")
