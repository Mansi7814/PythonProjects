from tkinter import *
from tkinter import messagebox
#import mysql.connector
top=Tk()
top.config(background="Bisque")
top.title("add book")
top.geometry("1600x800+0+0")


Label(top,text="HELLO",bg="Bisque",fg="Black",font=("comic sans MS",40,"underline")).place(x=400,y=10)



def addbev():
    a=str(e1.get())
    b=str(e2.get())
    c=str(e3.get())
    conn=mysql.connector.connect(user="root",password="",host="localhost",db="main")
    cursor=conn.cursor()
    cursor.execute("insert into beverages(SNo,NAME,PRICE)values('"+a+"','"+b+"','"+c+"'")
    conn.commit()


Label(top,text="BEVERAGES",bg="Bisque",fg="dodgerblue4",font=("comic sans MS",30)).place(x=100,y=220)

Label(top,text="SNo. :",bg="Bisque",fg="dodgerblue4",font=("comic sans MS",20)).place(x=50,y=290)
e1=Entry(top,font=("comic sans MS",15),bd=2,fg="navyblue",bg="grey")
e1.place(x=210,y=290)

Label(top,text="NAME :",bg="Bisque",fg="dodgerblue4",font=("comic sans MS",20)).place(x=50,y=330)
e2=Entry(top,font=("comic sans MS",15),bd=2,fg="navyblue",bg="grey")
e2.place(x=210,y=330)

Label(top,text="PRICE :",bg="Bisque",fg="dodgerblue4",font=("comic sans MS",20)).place(x=50,y=370)
e3=Entry(top,font=("comic sans MS",15),bd=2,fg="navyblue",bg="grey")
e3.place(x=210,y=370)




Button(top,text="Submit",command=addbev, bd=4, fg= "grey", font= ('comic sans MS',10,'bold'),bg="dodgerblue4").place(x=250,y=500)





top.mainloop()
