from tkinter import*
import tkinter.messagebox


root1 = Tk()
root1.geometry("720x420+400+220")
root1.title("Login Page")
root1.configure(background='red')

name_inp = StringVar()
password_inp = StringVar()

def enter():
	if name_inp.get() == "grishma" and password_inp.get() == "123123":
		root1.destroy()
		import question
	else:
		tkinter.messagebox.showinfo('Error','Authentication Failed')
		name_inp.set("")
		password_inp.set("")	

def destroy():
	root1.destroy()	


label = Label(root1, font = ('Colonna MT',30,'bold'), text ="Login Page",bg="yellow",width=50,fg = "steel blue", bd = 10)
label.pack()


label1 = Label(root1, text="Name",bg="red" ,font= ('Colonna MT',25,'bold')).place(x=150,y=150)
label2 = Label(root1, font = ('Colonna MT',25,'bold'),bg="red",text="Password").place(x=150,y=200)
	
entry1 = Entry(root1,font = ('Arial',15,'bold'), textvariable = name_inp)
entry2 = Entry(root1,show="*",font = ('Arial',15,'bold'), textvariable = password_inp)

entry1.place(x=350,y=150)
entry2.place(x=350,y=200)


enter_btn = Button(root1,font = ('Cooper',10,'bold'),bd=5,bg="red",fg="white",width=40, text="Enter", command= enter)
enter_btn.place(x=200,y=280)

exit_btn = Button(root1,font = ('Cooper',10,'bold'),bd=5,bg="red",fg="white",width=40, padx= 1, text="Exit", command= destroy)
exit_btn.place(x=200,y=320)

root1.mainloop()

