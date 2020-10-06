from tkinter import *
#import mysql.connector
from tkinter import messagebox


yo=Tk()
yo.config(background="chocolate1")
yo.title("Menubar")
yo.geometry("1600x800+0+0")



Label(yo,font=('Harlow Solid Italic',60), text="Partners",fg="white",bg="chocolate1").place(x=200,y=200)

Label(yo,font=('Arial',30), text="Harsh Sharma, Nandini Suhane",fg="white",bg="chocolate1").place(x=200,y=400)

Label(yo,font=('Arial',30), text="Purtika Talwani, Navneet Agarwal",fg="white",bg="chocolate1").place(x=200,y=450)

Label(yo,font=('Arial',30), text="Palak Malik, Mansi Gupta",fg="white",bg="chocolate1").place(x=200,y=500)

Label(yo,font=('Harlow Solid Italic',60), text="Branches",fg="white",bg="chocolate1").place(x=900,y=200)

Label(yo,font=('Arial',30), text="BADA near VK",fg="white",bg="chocolate1").place(x=900,y=400)

Label(yo,font=('Arial',30), text="IN Aston Martin club",fg="white",bg="chocolate1").place(x=900,y=450)

Label(yo,font=('Arial',30), text="A Hypothetical Place",fg="white",bg="chocolate1").place(x=900,y=500)




yo.mainloop()


