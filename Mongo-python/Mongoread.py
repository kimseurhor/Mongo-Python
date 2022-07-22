import pymongo

client = pymongo.MongoClient('mongodb://127.0.0.1:27017')

mydb = client['Student']

information = mydb.students

x = information.find()
# print(x[0])

for i in x:
    print(i)

