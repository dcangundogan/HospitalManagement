import this

import mysql
import mysql.connector
from customtkinter import *
import tkinter as tk
from CTkMessagebox import CTkMessagebox
import customtkinter

import CTkMessagebox as msgbox






class AdminPanel:
    window ="600x800"
    title = "Admin Panel"

    def __init__(self,window,title):
        adminPanel = CTk()


        adminPanel.geometry(window)

        adminPanel.resizable(False, False)
        adminPanel.title(title)
        button = CTkButton(master=adminPanel, text="Login", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225).pack(anchor="w", pady=(40, 0), padx=(25, 0))
        adminPanel.mainloop()





def loginChecker():
    db=mysql.connector.connect(host="localhost",
                                     user="root",
                                     password="bercan2003",
                                     db="libmanagementdb")
    query = "SELECT admin_username,admin_password FROM admin"
    dbcursor = db.cursor()
    dbcursor.execute(query)
    myresult=dbcursor.fetchall()

    if (myresult[0][0]==Username.get() and myresult[0][1]== password.get()):
        print(myresult)
        print(myresult[0][0])
        print(myresult[0][1])
        root.destroy()

        AdminPanel(window="600x800",title="Melisa cok guzel")
    else:
        CTkMessagebox(title="Error", message="Password or Username is wrong", icon="cancel")





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
                      bg='blue', command=loginChecker)
submitbtn.place(x=150, y=135, width=55)

root.mainloop()
