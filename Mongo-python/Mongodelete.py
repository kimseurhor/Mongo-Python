import pymongo

client = pymongo.MongoClient('mongodb://127.0.0.1:27017')

mydb = client['Student']

information = mydb.students

# information.delete_one({'Id': 1357})
information.delete_many({})
# information.delete_many({'age': 18})