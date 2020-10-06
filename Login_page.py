from tkinter import *
#import mysql.connector
from tkinter import messagebox

root=Tk()
def login():
    conn=mysql.connector.connect(host="localhost",user="root",password="",db="registration")
    cursor=conn.cursor()
    cursor.execute("select * from registration where USERNAME='"+e1.get()+"' and PASSWORD='"+e2.get()+"'")
    if(cursor.fetchone()):
        root.destroy()
        import LOGIN
    elif(e1.get()=="" or e2.get()==""):
        messagebox.showinfo("OH BHAI!!","KHALI KYU CHHOD RAHA H")
    else:
        messagebox.showinfo("OH BHAI!!","GALAT PASSWORD DALTA H")
    




    

root.config(background="DarkOrange")
root.geometry("500x500+400+100")
root.title("Login")
#Label(root,text="Welcome in KT's world",bg="orange",fg="white",font=("Arial",25)).place(x=100,y=50)
Label(root,text="Enter Username",bg="DarkOrange",fg="white",font=("MV boli",15)).grid(row=0,column=0)
Label(root,text="Enter Password",bg="DarkOrange",fg="white",font=("MV boli",15)).grid(row=1,column=0)
e1=Entry(root)
e1.grid(row=0,column=1)
e2=Entry(root,show="*")
e2.grid(row=1,column=1)
Button(root,text="Login",fg="Black",font=("BROADWAY",10),command=login).grid(row=2,column=0)
Button(root,text="Register",fg="Black",font=("BROADWAY",10)).grid(row=2,column=1)
root.mainloop()
