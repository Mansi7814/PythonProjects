from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import Image,ImageTk

def back():
    yo.destroy()
    import Mainpage


yo=Tk()
yo.config(background="chocolate1")
yo.title("Menubar")
yo.geometry("1600x800+0+0")


img=PhotoImage(file="F:\PYTHON 3.0\Sofwares\kitchen.png")
Label(yo,image=img).place(x=120,y=100)
Label(yo,font=('MV boli',40,'bold','underline'), text="Welcome to our beautiful Kitchen",fg="white",bg="chocolate1").place(x=120,y=20)
hey=Menu(yo)
a=Menu(yo,tearoff=0)
hey.add_cascade(label="HOME",menu=a)
a.add_command(label="Home",command=back)
yo.config(menu=hey)

