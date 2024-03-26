#!/usr/bin/env python3
'''
8-all
'''


def list_all(mongo_collection):
    """
    Function that lists all documents in a collection.

    Args:
        mongo_collection (pymongo.collection.Collection):
        A pymongo collection object.

    Returns:
        list: A list of documents from the collection.
        If no documents are found, an empty list is returned.
    """

    documents = []
    for document in mongo_collection.find():
        documents.append(document)
    return documents
