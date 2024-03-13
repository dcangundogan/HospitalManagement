import mysql
import mysql.connector

import tkinter as tk


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password= "bercan2003",
  database = "libmanagementdb"
)



def submitact():
    user = Username.get()
    passw = password.get()

    print(f"The name entered by you is {user} {passw}")

    logintodb(user, passw)


def logintodb(user, passw):


    if passw:
        db = mysql.connector.connect(host="localhost",
                                     user="root",
                                     password="bercan2003",
                                     db="libmanagementdb")
        cursor = db.cursor()

    # If no password is entered by the
    # user
    else:
        db = mysql.connector.connect(host="localhost",
                                     user="root",
                                     db="libmanagementdb")
        cursor = db.cursor()

    # A Table in the database
    savequery = "select admin_username,admin_password from admin"

    try:
        cursor.execute(savequery)
        myresult = cursor.fetchall()

        # Printing the result of the
        # query
        for x in myresult:
            print(x)
        print("Query Executed successfully")
        print(myresult)

    except:
        db.rollback()
        print("Error occurred")



def loginChecker():
    db=mysql.connector.connect(host="localhost",
                                     user="root",
                                     password="bercan2003",
                                     db="libmanagementdb")
    query = "SELECT admin_username,admin_password FROM admin"
    dbcursor = db.cursor()
    dbcursor.execute(query)
    myresult=dbcursor.fetchall()
    print(myresult)


root = tk.Tk()
root.geometry("300x300")
root.title("DBMS Login Page")

# Defining the first row
lblfrstrow = tk.Label(root, text="Username -", )
lblfrstrow.place(x=50, y=20)

Username = tk.Entry(root, width=35)
Username.place(x=150, y=20, width=100)

lblsecrow = tk.Label(root, text="Password -")
lblsecrow.place(x=50, y=50)

password = tk.Entry(root, width=35)
password.place(x=150, y=50, width=100)

submitbtn = tk.Button(root, text="Login",
                      bg='blue', command=submitact)
submitbtn.place(x=150, y=135, width=55)

root.mainloop()


