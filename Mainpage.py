from tkinter import *
#import mysql.connector
from tkinter import messagebox

def rec():
    yo.destroy()
    import rec
def show():
    yo.destroy()
    import img
def listbev():
    import cafelistbev
def listmc():
    import cafelistmc
def listdes():
    import cafelistdes
def regis():
    import REgister
def login():
    import Login_page
def emp():
    import employee
def Staff():
    import Staff
def partners():
    import partners
def contact():
    import contact


yo=Tk()
yo.config(background="chocolate1")
yo.title("Menubar")
yo.geometry("1600x800+0+0")


img=PhotoImage(file="H:\KT_Cafe\Images\KT.png")
Label(yo,image=img).place(x=590,y=150)
Label(yo,font=('MV boli',60,'bold','underline'), text="Cafe_KT390",fg="white",bg="chocolate1").place(x=400,y=250)

Label(yo,font=('Arial',30),text="Welcome to the best Cafe in the world,\nHere we provide the best meal to our costumers at their doorstep\n",fg="white",bg="chocolate1").place(x=120,y=350)
                                 


category=Menu(yo)
d=Menu(category,tearoff=0)
category.add_cascade(label="Cafe Menu",menu=d)
d.add_command(label="Beverages",command=listbev)
d.add_separator()
d.add_command(label="Main Course",command=listmc)
d.add_separator()
d.add_command(label="Dessert",command=listdes)

a=Menu(category,tearoff=0)
category.add_cascade(label="SIGN IN",menu=a)
a.add_command(label="user",command=login)
a.add_separator()
a.add_command(label="employee",command=emp)
a.add_separator()
a.add_command(label="Register",command=regis)

#About=Menu(yo)
b=Menu(category,tearoff=0)
category.add_cascade(label="About Us",menu=b)
b.add_command(label="Staff",command=Staff)
b.add_separator()
b.add_command(label="Our Partners & Branches",command=partners)
b.add_separator()
b.add_command(label="Contact Us",command=contact)
b.add_separator()


c=Menu(category,tearoff=0)
category.add_cascade(label="Gallery",menu=c)

c.add_command(label="Kitchen",command=show)
c.add_separator()
c.add_command(label="Reception",command=rec)
c.add_separator()


yo.config(menu=category)







yo.mainloop()




