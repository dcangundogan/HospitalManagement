import tkinter as tk
import customtkinter
from customtkinter import *

import PIL
import mysql
import mysql.connector
import customtkinter
import tkinter
from customtkinter import *
from tkinter import *
from PIL import *
import mysql.connector
from CTkMessagebox import *



class MainPage:

    def __init__(self,window,title):
        mainpage=CTk()
        imgLogo = Image.open("/Users/alperen/PycharmProjects/HospitalManagement/img/logo.png")
        patientLogo = Image.open("/Users/alperen/PycharmProjects/HospitalManagement/img/patient1.png")
        doctorLogo = Image.open("/Users/alperen/PycharmProjects/HospitalManagement/img/doctor.png")

        imgLogoCTk = CTkImage(dark_image=imgLogo, light_image=imgLogo, size=(300, 480))
        imgpatient = CTkImage(dark_image=patientLogo, light_image=patientLogo, size=(20,20))
        imgdoctor = CTkImage(dark_image=doctorLogo,light_image=doctorLogo,size=(20,20))
        mainpage.geometry(window)
        mainpage.title(title)
        mainpage.resizable(False,False)
        logoLabel = CTkLabel(master=mainpage, text="", image=imgLogoCTk).pack(expand=True, side="left")

        frame = CTkFrame(master=mainpage, width=320, height=480, fg_color="#ffffff",)


        frame.pack_propagate(0)

        frame.pack(expand=True, side="right")



        welcomeLabel = CTkLabel(master=frame, text="WELCOME TO \n"
                                                   "MEDICAREHUB \n"
                                                   " SYSTEM!",font=("Arial Bold",26),text_color="#261E76",
                                anchor="w",justify=CENTER,)
        welcomeLabel.pack(anchor="w",padx=(55,0),pady=(75,0))

        doctorButton =  CTkButton(master=frame, text="Doctor ", fg_color="#EEEEEE", command=MainPage.doctorCommand,
                                  hover_color="#08e590", font=("Arial Bold", 18), text_color="#601E88", width=275,height=32,
                                               image=imgdoctor).pack(anchor="w", pady=(55, 0), padx=(15, 0))

        patientButton = CTkButton(master=frame, text="Patient ", fg_color="#EEEEEE", command=MainPage.doctorCommand,
                                 hover_color="#08e590", font=("Arial Bold", 18), text_color="#601E88", width=275,
                                 height=32,
                                 image=imgpatient).pack(anchor="w", pady=(20, 0), padx=(15, 0))

        adminButton = CTkButton(master=frame, text="Admin ", fg_color="#EEEEEE", command=MainPage.doctorCommand,
                                  hover_color="#08e590", font=("Arial Bold", 18), text_color="#601E88", width=275,
                                  height=32,
                                  image=imgdoctor).pack(anchor="w", pady=(20, 0), padx=(15, 0))

        mainpage.mainloop()


    def doctorCommand(self):
        print("Doing Doctor")
    def patientCommand(self):
        print("Doing Patient")




mp=MainPage(window="600x400",title="Welcome to MediCareHub",)
