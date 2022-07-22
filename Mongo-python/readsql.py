import mysql.connector
import pymongo

client = pymongo.MongoClient('mongodb://127.0.0.1:27017')

mydb = client['DSE10']

kimseur = mydb.students

mysqldb = mysql.connector.connect(
    host="localhost",
    database="student",
    port='3306',
    user="root",
    password="1234"
)

mycursor= mysqldb.cursor(dictionary=True)
mycursor.execute("SELECT * from DSE10;")
myresult= mycursor.fetchall()

# print(myresult)

if len(myresult)>0:
    x = kimseur.inser_many(myresult)
    print(len(x.inserted_ids))