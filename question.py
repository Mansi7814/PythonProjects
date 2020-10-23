from tkinter import*

#window-----------------
newroot = Tk()
newroot.geometry("720x500+400+50")
newroot.title("Menu")
newroot.configure(background='red')
#function----------------
def enter1():
	newroot.destroy()
	import restaurant_management_system


def enter2():
	newroot.destroy()
	import price

def enter3():
        newroot.destroy()
        import stock

def enter4():
        newroot.destroy()
        import menu

#image--------------
background_image = PhotoImage(file="welcome.png")
background = Label(newroot, image=background_image,
                   bg="white",bd=0)
background.pack()

#body----------------------
label11 = Label(newroot,font= ('Colonna MT',20,'bold'),bg="red", text="Bill")
label11.place(x=200,y=200)

press_btn = Button(newroot, text="Press Here", command= enter2)
press_btn.place(x=400,y=250)

label21 = Label(newroot,font= ('Colonna MT',20,'bold'),bg="red", text="Change Price")        
label21.place(x=200,y=250)

press1_btn = Button(newroot, text="Press Here", command= enter1)
press1_btn.place(x=400,y=200)

label31 = Label(newroot,font= ('Colonna MT',20,'bold'),bg="red", text="Stock")        
label31.place(x=200,y=300)

press2_btn = Button(newroot, text="Press Here", command=enter3)
press2_btn.place(x=400,y=300)

label41 = Label(newroot,font= ('Colonna MT',20,'bold'),bg="red", text="Menu")        
label41.place(x=200,y=350)

press3_btn = Button(newroot, text="Press Here",command=enter4)
press3_btn.place(x=400,y=350)

newroot.mainloop()
