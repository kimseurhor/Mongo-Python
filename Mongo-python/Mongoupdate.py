import pymongo

client = pymongo.MongoClient('mongodb://127.0.0.1:27017')

mydb = client['Student']

information = mydb.students



information.update_one({'Id': 6784}, {'$set':{'name': 'Sreng Hanritheasen'}})
# information.update_many({'name': 'chan'}, {'$set':{'name': 'Reaksmey'}})