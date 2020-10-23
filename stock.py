from tkinter import*

#window-----------------
newroot = Tk()
newroot.geometry("720x500+400+150")
newroot.title("Stock")
newroot.configure(background='red')

def update():
    newroot.destroy()
    import stockupdate
def backfn():
    newroot.destroy()
    import question


    
drinks_p=StringVar()
Ice_cream_p=StringVar()
pestry_p=StringVar()

f1 = open('value.txt','r')
line = f1.readlines()
x=((line[0]))
y=((line[1]))
z=((line[2]))

f1.close()

f1 = open('new.txt','r')
li = f1.read()
p=((li[0]))
q=((li[1]))
r=((li[2]))

f1.close()


print(p)

drinks = Label(newroot, font=('arial',16,'bold'),text = "Drinks",bg= "red", bd = 16, anchor = 'w' )
drinks.grid(row=4,column=0,sticky = E)
txt_drinks = Entry(newroot,font=('arial',16,'bold'), textvariable=drinks_p, bd=10, insertwidth =4,bg = "powder blue", justify ='right')
txt_drinks.grid(row=4,column=1)

paneer_tikka = Label(newroot, font=('arial',16,'bold'),text = "Ice-Cream",bg= "red", bd = 16, anchor = 'w' )
paneer_tikka.grid(row=5,column=0,sticky = E)
txt_paneer_tikka = Entry(newroot,font=('arial',16,'bold'), textvariable=Ice_cream_p, bd=10, insertwidth =4,bg = "powder blue", justify ='right')
txt_paneer_tikka.grid(row=5,column=1)

chicken_tikka = Label(newroot, font=('arial',16,'bold'),text = "Pestry",bg= "red", bd = 16, anchor = 'w' )
chicken_tikka.grid(row=6,column=0,sticky = E)
txt_chicken_tikka = Entry(newroot,font=('arial',16,'bold'), textvariable=pestry_p, bd=10, insertwidth =4,bg = "powder blue", justify ='right')
txt_chicken_tikka.grid(row=6,column=1)


btn_update = Button(newroot, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',16,'bold'), width=10, text= "Update", bg= "red",command = update)
btn_update.grid(row=7, column= 1)


btn_back = Button(newroot, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',16,'bold'), width=10, text= "Back", bg= "red",command = backfn)
btn_back.grid(row=7, column= 3)







newroot.mainloop()
