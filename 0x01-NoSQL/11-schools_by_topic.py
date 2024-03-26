#!/usr/bin/env python3
'''
11-schools_by_topic
'''


def schools_by_topic(mongo_collection, topic):
    """
    Function that returns a list of schools that have a specific topic
    within their list of topics.

    Args:
        mongo_collection (pymongo.collection.Collection):
        A pymongo collection object.
        topic (str): The topic to search for in the schools' topics list.

    Returns:
        list: A list of dictionaries representing the school documents
              that contain the specified topic.
    """

    filter_doc = {"topics": {"$in": [topic]}}

    # Find matching schools
    schools = list(mongo_collection.find(filter_doc))

    return schools
