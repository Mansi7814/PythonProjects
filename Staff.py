from tkinter import *
import mysql.connector
from tkinter import messagebox


yo=Tk()
yo.config(background="chocolate1")
yo.title("Menubar")
yo.geometry("1600x800+0+0")



Label(yo,font=('MV Boli',60,'bold','underline'), text="KT390's Staff :",fg="white",bg="chocolate1").place(x=300,y=200)

Label(yo,font=('Arial',30), text="KT BHAI as President",fg="white",bg="chocolate1").place(x=300,y=400)

Label(yo,font=('Arial',30), text="Harsh Sharma as CEO",fg="white",bg="chocolate1").place(x=300,y=450)

Label(yo,font=('Arial',30), text="Nandini,Purtika as Managers",fg="white",bg="chocolate1").place(x=300,y=500)




yo.mainloop()

