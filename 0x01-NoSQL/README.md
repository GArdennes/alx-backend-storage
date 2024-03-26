# 0x01. NoSQL
## Learning Objectives
1) What does NoSQL mean?
2) What is the difference between SQL and NoSQL
3) What is ACID
4) What is a document storage
5) What are NoSQL types
6) What are benefits of a NoSQL database
7) How to query information from a NoSQL database
8) How to insert/update/delete information from a NoSQL database
9) How to use MongoDB

## Learning
NoSQL stands for **Not Only SQL**. It refers to a type of database that stores and manages data in a different way compared to relational databases like SQL. Unlike the rigid structures relational databases provide, NoSQL has the advantage of offering flexible structures that allow for many other data formats like documents, key-value pairs or graphs. NoSQL offers other advantages like horizontal scalability to accommodate growing datasets, and fast performance for applications dealing with big data or real-time web applications.

SQL follows a set of properties that guarantee data integrity. These properties are called ACID which stands for **A**tomicity **C**onsistency **I**solation **D**urability. Atomicity guarantees that transactions on the database would be treated as a single unit preventing partially completed transactions from leaving the database in an inconsistent state. Consistency means the transaction would adhere to the defined rules before and after operation. Isolation guarantees that concurrent transactions don’t affect each other although they are happening at the same time. Durability highlights the strength in the database such that after a transaction occurs the changes are permanent and not affected by system failures.

SQL follows a relational model of storage which organizes data according to rows and columns; however , document models implemented by NoSQL store data in documents in JSON or XML formats. Each document can hold various data types and structures such as strings, numbers, booleans, arrays, key-value pairs and nested structures. There are different types of NoSQL. Here is a quick guideline:
1) **Document stores:** Flexible for complex, semi-structured data.
2) **Key-value stores:** Fast and scalable for simple data retrieval.
3) **Column-oriented databases:** Efficient for analyzing large datasets with specific queries.
4) **Graph databases:** Best for modeling connections and relationships

MongoDB is a document type of NoSQL. For fetching data from its collections it uses its own query language called MongoDB Query Language (MQL). MQL utilizes JavaScript expressions to define filters and conditions for retrieving documents.

Here is the basic syntax for querying data in MongoDB:
```
db.collection_name.find({filter_document})
```
- `db`: This refers to the database you’re connected to
- `collection_name`: Stands in for the collection containing the documents you want to query
- `find()`: This is the main method for retrieving documents
- `filter_document`: This defines a condition for selecting a specific document

Let’s show how to filter for products with a price greater than 100:
```
db.products.find({price: {$gt: 100}})
```
 Aside from this, MongoDB provides several methods to insert, delete, and update information within a collection. Let’s take a look at them:
**Inserting documents**
- insertOne(): This method inserts a single document into a collection. It takes a document you want to insert as an argument.
```
db.collection_name.insertOne({ name: "Alice", age: 30 })
```
- insertMany(): This method inserts an array of documents into a collection in a single operation.
```
db.collection_name.insertMany([
  { name: "Bob", age: 25 },
  { name: "Charlie", age: 42 }
])
```

**Updating documents**
- updateOne(): This method updates a single document that matches a specific filter criteria. It takes two arguments: the filter document to identify the document and the update document specifying the changes.
```
db.collection_name.updateOne({ age: 30 }, { $set: { age: 31 } })
```
In the above example, the document where age is 30 will have its age updated to 31. The `$set` operator is used to modify specific fields.

- updateMany(): This method updates multiple documents that match a filter criteria.
```
db.collection_name.updateMany({ price: { $gt: 100 } }, { $set: { discount: 10 } })
```
This query updates all documents where price is greater than 100 by adding a new field discount with a value of 10.

- replaceOne(): This method replaces an entire matching document with a new document provided.
```
db.collection_name.replaceOne({ name: "Alice" }, { name: "Alice", occupation: "Teacher" })
```
This replaces the document where name is Alice with a new document containing the same name and an additional field occupation.

**Deleting Documents**
- deleteOne(): As the method suggests, it deletes a single document that matches a specific criteria.
```
db.collection_name.deleteOne({ name: "Bob" })
```
This deletes the document where the name field is Bob.

- deleteMany(): This method deletes all documents that match a specific filter criteria.
```
db.collection_name.deleteMany({ age: { $lt: 25 } })
```
This deletes all documents where the age field is less than 25.

## Requirements
### MongoDB Command File
1) All your files will be interpreted on Ubuntu 18.04 LTS using MongoDB 
2) All your files should end with a new line
3) The first line of all your files should be a comment: //comment
4) A readme.md file, at the root of the folder of the project, is mandatory
5) The length of your files will be tested using wc

### Python Scripts
1) All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 and PyMongo
2) All your files should end with a new line
3) The first line of all your files should be exactly `#!/usr/bin/env python3`
4) A readme.md file, at the root of the folder of the project, is mandatory.
5) Your code should use the pycodestyle style (version 2.5.)
6) The length of your files will be tested using wc
7) All your modules should have a documentation
8) All your functions should have a documentation

### Install MongoDB 4.2 in Ubuntu 18.04
```
$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
...
$  sudo service mongod status
mongod start/running, process 3627
$ mongo --version
MongoDB shell version v4.2.8
git version: 43d25964249164d76d5e04dd6cf38f6111e21f5f
OpenSSL version: OpenSSL 1.1.1  11 Sep 2018
allocator: tcmalloc
modules: none
build environment:
    distmod: ubuntu1804
    distarch: x86_64
    target_arch: x86_64
$  
$ pip3 install pymongo
$ python3
>>> import pymongo
>>> pymongo.__version__
'3.10.1'
```

## Tasks
### 0. List all databases
Write a script that lists all databases in MongoDB


### 1. Create a database
Write a script that creates or uses the database my_db


### 2. Insert document
Write a script that inserts a document in the collection `school`:
Requirement
- The document must have one attribute `name` with value **Holberton school**.
- The database name will be passed as an option of `mongo` command


### 3. All documents
Write a script that lists all documents in the collection `school`:
- The database name will be passed as option of `mongo` command


### 4. All matches
Write a script that lists all documents with `name=Holberton school` in the collection `school`:
- The database will be passed as option of `mongo` command


### 5. Count
Write a script that displays the number of documents in the collection `school`:
- The database name will be passed as an option of `mongo` command.


### 6. Update
Write a script that adds a new attribute to a document in the collection `school`:
Requirements
- The script should update only the document with `name=Holberton school` (all of them)
- The update should add the attribute `address` with the value **972 Mission street**
- The database name will be passed as option of `mongo` command


### 7. Delete by match
Write a script that deletes all documents with `name=Holberton school` in the collection `school`.
- The database name will be passed as an option of `mongo` command.


### 8. List all documents in Python
Write a Python function that lists all documents in a collection.
Requirements:
- Prototype: `def list_all(mongo_collection):`
- Return an empty list if no document in the collection
- `mongo_collection` will be the `pymongo` collection object


### 9. Insert a document in Python
Write a Python function that inserts a new document in a collection based on `kwargs`.
Requirements:
- Prototype: `def insert_school(mongo_collection, **kwargs):`
- `mongo_collection` will be the `pymongo` collection object
- Returns the new `_id`


### 10. Change school topics
Write a Python function that changes all topics of a school document based on the name:
Requirements:
- Prototype: `def update_topics(mongo_collection, name, topics):`
- `mongo_collection` will be the `pymongo` collection object
- `name` (string) will be the school name to update
- `topics` (list of strings) will be the list of topics approached in the school


### 11. Where can I learn Python?
Write a Python function that returns the list of school having a specific topic:
Returns
- Prototype: `def schools_by_topic(mongo_collection, topic):`
- `mongo_collection` will be the `pymongo` collection object
- `topic` (string) will be topic searched


### 12. Log stats
Write a Python script that provides some stats about Nginx logs stored in MongoDB:
- Database: `logs`
- Collection: `nginx`
- Display (same as the example):
- - first line: `x logs` where x is the number of documents in this collection
- - second line: `Methods:`
- - 5 lines with the number of documents with the `method` - `["GET", "POST", "PUT", "PATCH", "DELETE"]` in this order.
- - One line with the number of documents with: `method=Get` and `path=/status`

You can use this dump as data sample: [dump.zip](https://intranet.alxswe.com/rltoken/0szbpslKvH3RqKb_2HUeoQ)


### 13. Regex filter
Write a script that lists all documents with `name` starting by `Holberton` in the collection `school`:
- The database name will be passed as an option of `mongo` command.


### 14. Top students
Write a Python function that returns all students sorted by average score:
- Prototype: `def top_students(mongo_collection):`
- `mongo_collection` will be the `pymongo` collection object.
- The top must be ordered
- The average score must be part of each item returns with key = `averageScore`


### 15. Log stats - new version
Improve `12-log_stats.py` by adding the top 10 of the most present IPs in the collection `nginx` of the database `logs`:
- The IPs top must be sorted
