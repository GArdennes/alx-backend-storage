#!/usr/bin/env python3
'''
10-update_topics
'''


def update_topics(mongo_collection, name, topics):
    """
    Function that updates the topics field of documents in a collection
    matching a specific school name.

    Args:
        mongo_collection (pymongo.collection.Collection):
        A pymongo collection object.
        name (str): The name of the school to update documents for.
        topics (list): The new list of topics to be assigned.

    Returns:
        None
    """

    # Define the filter criteria
    filter_document = {"name": name}

    # Update document using $set operator
    update_document = {"$set": {"topics": topics}}

    # Update matching documents
    mongo_collection.update_many(filter_document, update_document)
