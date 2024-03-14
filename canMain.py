import customtkinter
import tkinter
from customtkinter import *
from tkinter import *
from PIL import *
import mysql.connector
from CTkMessagebox import *


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="alperen0519",
  database ="libmanagementdb"
)



app = CTk()

app.geometry("600x480")

app.resizable(True,True)
imgLogo = Image.open("/Users/alperen/PycharmProjects/HospitalManagement/img/logo.png")


#imgLogo = Image.open("logo.png")

google_icon_data = Image.open("/Users/alperen/PycharmProjects/HospitalManagement/img/google-icon.png")

imgEmail = Image.open("/Users/alperen/PycharmProjects/HospitalManagement/img/email-icon.png")

imgUser = Image.open("/Users/alperen/PycharmProjects/HospitalManagement/img/man.png")
imgPassword = Image.open("/Users/alperen/PycharmProjects/HospitalManagement/img/password-icon.png")

imgLogoCTk =CTkImage(dark_image=imgLogo,light_image=imgLogo,size=(300,480))

google_icon = CTkImage(dark_image=google_icon_data, light_image=google_icon_data, size=(17,17))

userIcon = CTkImage(dark_image=imgUser, light_image=imgUser,size=(20,20))

passwordIcon = CTkImage(dark_image=imgPassword,light_image=imgPassword, size=(20,20))


#MediCareHub frame kismi
logoLabel = CTkLabel(master=app, text="", image=imgLogoCTk).pack(expand=True, side="left")


frame = CTkFrame(master=app, width=300, height=480, fg_color="#ffffff")

frame.pack_propagate(0)

frame.pack(expand=True, side="right")

#MediCareHub frame bitis



medicarehubLabel = CTkLabel(master=frame,text_color="#261E76",anchor="w",justify=CENTER,
                            text="Welcome to \n"
                                 "MediCareHub!",
                            font=("Arial Bold",28)).pack(anchor="w",pady=(50,5),padx=(65,0))

signLabel = CTkLabel(master=frame,text_color="#7E7E7E",anchor="w",justify="left",
                            text="       Please login to    \n"
                                 "MediCareHub System!",
                            font=("Arial Bold",14)).pack(anchor="w",pady=(5,0), padx=(85,0))

usernameLabel = CTkLabel(master=frame,text_color="#7E7E7E",anchor="w",justify=CENTER,
                            text="Username:",
                            font=("Arial Bold",14),image=userIcon,compound="left").pack(anchor="w",pady=(25,0),padx=(30,0))

usernameEntry = CTkEntry(master=frame,width=240,height=30 ,fg_color="#EEEEEE",border_color="#261E76",border_width=2
                         ,text_color="#000000")
usernameEntry.pack(anchor="w",padx=(30,0))



passwordLabel = CTkLabel(master=frame,text_color="#7E7E7E",anchor="w",justify="left",
                            text="Password:",
                            font=("Arial Bold",14),image=passwordIcon,compound="left").pack(anchor="w",pady=(10,0),padx=(30,0))

passwordEntry = CTkEntry(master=frame,width=240,height=30 , fg_color="#EEEEEE",border_color="#261E76",border_width=2
                         ,text_color="#000000",show="*")
passwordEntry.pack(anchor="w",padx=(30,0))



def entryTest():
    username = usernameEntry.get()
    print(username)

def click_handler():
    print("Login Button Clicked")

def loginChecker():


  try:
    username = usernameEntry.get()
    password = passwordEntry.get()
    query = '''SELECT admin_username,admin_password FROM admin WHERE admin_username=='"+username+"''''
    mycursor=mydb.cursor()
    mycursor.execute(query)

    myresult = mycursor.fetchall()
    print(myresult)
    if myresult:
        realpswrd = myresult[0]
        # Assuming psswrd_entry is your tkinter Entry widget for password
        if realpswrd == password:
            CTkMessagebox(title="Info", message="Welcome to MediCareHub Services!")
            # Code to open admin panel window
        else:
            CTkMessagebox(title="Error", message="Username or Password is wrong.", icon="cancel")
    else:
        CTkMessagebox(title="Error", message="You don't have access!!", icon="cancel")
  except mysql.connector.Error as e:
    CTkMessagebox(title="Error", message="Database is Wrong", icon="cancel")



#def username_handler(username):
 #   print(username)


app.title("MediCareHub Login Page")

set_appearance_mode("light")

loginButton = CTkButton(master=frame,command=loginChecker, text="Login", fg_color="#601E88", hover_color="#E44982",
                        font=("Arial Bold", 12), text_color="#ffffff", width=240,height=35).pack(anchor="w", pady=(30, 0), padx=(30, 0))
googleButton= CTkButton(master=frame, text="Continue With Google", fg_color="#EEEEEE", hover_color="#EEEEEE",
                        font=("Arial Bold", 11), text_color="#601E88", width=240, image=google_icon).pack(anchor="w", pady=(10, 0), padx=(30, 0))
signupButton = CTkButton(master=frame,text="Create Account",fg_color="#EEEEEE",hover_color="#EEEEEE",font=("Arial Bold",12),text_color="#0000FF",width=240,height=25)
signupButton.pack(anchor="w", pady=(10, 0), padx=(30, 0))


app.mainloop()
