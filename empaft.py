from tkinter import *
from tkinter import messagebox
import mysql.connector
top=Tk()
top.config(background="Bisque")
top.title("Employee")
top.geometry("1600x800+0+0")


Label(top,text="HELLO",bg="Bisque",fg="Black",font=("comic sans MS",40,"underline")).place(x=400,y=10)


def dest():
    top.destroy()
    import employee

    
def addbev():
    a=str(e1.get())
    b=str(e2.get())
    c=str(e3.get())
    conn=mysql.connector.connect(user="root",password="",host="localhost",db="main")
    cursor=conn.cursor()
    cursor.execute("insert into beverages(SNo,NAME,PRICE)values('"+a+"','"+b+"','"+c+"')")
    conn.commit()

    
def addmc():
    d=str(e4.get())
    e=str(e5.get())
    f=str(e6.get())
    conn=mysql.connector.connect(user="root",password="",host="localhost",db="main")
    cursor=conn.cursor()
    cursor.execute("insert into maincourse(SNo,NAME,PRICE)values('"+d+"','"+e+"','"+f+"')")
    conn.commit()

    
def adddes():
    g=str(e7.get())
    h=str(e8.get())
    i=str(e9.get())
    conn=mysql.connector.connect(user="root",password="",host="localhost",db="main")
    cursor=conn.cursor()
    cursor.execute("insert into dessert(SNo,NAME,PRICE)values('"+g+"','"+h+"','"+i+"')")
    conn.commit()

LO=Menu(top)
a=Menu(LO,tearoff=0)
LO.add_cascade(label="LOGOUT",menu=a)
a.add_command(label="log-out",command=dest)
top.config(menu=LO)



Label(top,text="BEVERAGES",bg="Bisque",fg="dodgerblue4",font=("comic sans MS",30)).place(x=100,y=220)
Label(top,text="MAIN COURSE",bg="Bisque",fg="dodgerblue4",font=("comic sans MS",30)).place(x=560,y=220)
Label(top,text="DESSERT",bg="Bisque",fg="dodgerblue4",font=("comic sans MS",30)).place(x=1020,y=220)


Label(top,text="SNo. :",bg="Bisque",fg="dodgerblue4",font=("comic sans MS",20)).place(x=50,y=290)
e1=Entry(top,font=("comic sans MS",15),bd=2,fg="navyblue",bg="grey")
e1.place(x=210,y=290)

Label(top,text="NAME :",bg="Bisque",fg="dodgerblue4",font=("comic sans MS",20)).place(x=50,y=330)
e2=Entry(top,font=("comic sans MS",15),bd=2,fg="navyblue",bg="grey")
e2.place(x=210,y=330)

Label(top,text="PRICE :",bg="Bisque",fg="dodgerblue4",font=("comic sans MS",20)).place(x=50,y=370)
e3=Entry(top,font=("comic sans MS",15),bd=2,fg="navyblue",bg="grey")
e3.place(x=210,y=370)

Label(top,text="SNo :",bg="Bisque",fg="dodgerblue4",font=("comic sans MS",20)).place(x=450,y=290)
e4=Entry(top,font=("comic sans MS",15),bd=2,fg="navyblue",bg="grey")
e4.place(x=650,y=290)

Label(top,text="NAME :",bg="Bisque",fg="dodgerblue4",font=("comic sans MS",20)).place(x=450,y=330)
e5=Entry(top,font=("comic sans MS",15),bd=2,fg="navyblue",bg="grey")
e5.place(x=650,y=330)

Label(top,text="PRICE :",bg="Bisque",fg="dodgerblue4",font=("comic sans MS",20)).place(x=450,y=370)
e6=Entry(top,font=("comic sans MS",15),bd=2,fg="navyblue",bg="grey")
e6.place(x=650,y=370)

Label(top,text="SNo :",bg="Bisque",fg="dodgerblue4",font=("comic sans MS",20)).place(x=910,y=290)
e7=Entry(top,font=("comic sans MS",15),bd=2,fg="navyblue",bg="grey")
e7.place(x=1110,y=290)

Label(top,text="NAME :",bg="Bisque",fg="dodgerblue4",font=("comic sans MS",20)).place(x=910,y=330)
e8=Entry(top,font=("comic sans MS",15),bd=2,fg="navyblue",bg="grey")
e8.place(x=1110,y=330)

Label(top,text="PRICE :",bg="Bisque",fg="dodgerblue4",font=("comic sans MS",20)).place(x=910,y=370)
e9=Entry(top,font=("comic sans MS",15),bd=2,fg="navyblue",bg="grey")
e9.place(x=1110,y=370)





Button(top,text="Submit",command=addbev, bd=4, fg= "grey", font= ('comic sans MS',10,'bold'),bg="dodgerblue4").place(x=250,y=500)
Button(top,text="Submit",command=addmc, bd=4, fg= "grey", font= ('comic sans MS',10,'bold'),bg="dodgerblue4").place(x=750,y=500)
Button(top,text="Submit",command=adddes, bd=4, fg= "grey", font= ('comic sans MS',10,'bold'),bg="dodgerblue4").place(x=1250,y=500)















top.mainloop()
