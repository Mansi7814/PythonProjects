from tkinter import *
#import mysql.connector

root=Tk()

def regis():
    a=str(e1.get())
    b=str(e2.get())
    c=str(e3.get())
    d=str(e4.get())
    e=str(e5.get())
    f=str(e6.get())
    
    conn=mysql.connector.connect(host="localhost",user="root",password="",db="registration")
    cursor=conn.cursor()
    cursor.execute("insert into registration(FullName,EmailID,DOB,USERNAME,PASSWORD,MobileNo) values('"+a+"','"+b+"','"+c+"','"+d+"','"+e+"','"+f+"')")
    root.destroy()
    import Login_page
    conn.commit()
    


root.config(background="cyan")
root.geometry("1600x800+0+0")
root.title("REGISTER")
#Label(root,text="Welcome in KT's world",bg="orange",fg="white",font=("Arial",25)).place(x=100,y=50)
Label(root,text="Enter Fullname",bg="cyan",fg="black",font=("MV boli",30)).grid(row=0,column=4)
Label(root,text="Enter Email ID",bg="cyan",fg="black",font=("MV boli",30)).grid(row=1,column=4)
Label(root,text="Enter DOB",bg="cyan",fg="black",font=("MV boli",30)).grid(row=2,column=4)
Label(root,text="Create USERNAME",bg="cyan",fg="black",font=("MV boli",30)).grid(row=3,column=4)


Label(root,text="Create PASSWORD",bg="cyan",fg="black",font=("MV boli",30)).grid(row=4,column=4)
Label(root,text="Enter Mobile No.",bg="cyan",fg="black",font=("MV boli",30)).grid(row=5,column=4)

e1=Entry(root)
e1.grid(row=0,column=6)
e2=Entry(root)
e2.grid(row=1,column=6)
e3=Entry(root)
e3.grid(row=2,column=6)
e4=Entry(root)
e4.grid(row=3,column=6)
e5=Entry(root,show="*")
e5.grid(row=4,column=6)
e6=Entry(root)
e6.grid(row=5,column=6)
Button(root,text="REGISTER",fg="blue",font=("BROADWAY",10),command=regis).grid(row=6,column=6)
root.mainloop()
