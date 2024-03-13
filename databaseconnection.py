import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="bercan2003",
  database ="libmanagementdb"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM admin")
myresult = mycursor.fetchall()

print(myresult)
for x in myresult:
     print(x)
