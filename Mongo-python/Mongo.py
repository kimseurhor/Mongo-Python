import pymongo

client = pymongo.MongoClient('mongodb://127.0.0.1:27017')

mydb = client['Student']

information = mydb.students

record1 = {
    'name': 'Hor Kimseur',
    'Id': 1234,
    'department': 'software engineer',
    'age': 18
}
record2= {
    'name': 'Sara Pich',
    'Id': 3853,
    'department': 'software engineer',
    'age': 17
    }
record3 = {'name': 'Sen',
    'Id': 6784,
    'department': 'software engineer',
    'age': 18}
record5 = {'name': 'Chan',
    'Id': 1357,
    'department': 'Tourism management',
    'age': 21}
record6 = {'name': 'chan',
    'Id': 2468,
    'department': 'architecture',
    'age': 20}

# information.insert_one(record1)
information.insert_many([record1, record2, record3, record5, record6])

