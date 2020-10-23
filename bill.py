from tkinter import *
import tkinter.messagebox
import time
import random

operator = ""
#### creating window and its geometry ######

root = Tk()
root.geometry("1600x800+0+0")
root.title("Restaurant Management System")
root.configure(background='red')


#### creating Frame ######

top = Frame(root, width = 1600, height = 50, relief = SUNKEN)
top.pack(side = TOP)

left = Frame(root, width = 800
             , height = 700, relief = SUNKEN)
left.pack(side = LEFT)

right = Frame(root, width = 300, height = 700)
right.pack(side = RIGHT)

#################
label_info = Label(top,font= ('Colonna MT',70,'bold'), text ="Restaurant Management System",bg="yellow" ,fg = "steel blue", bd = 10, anchor = 'w')
label_info.grid(row = 0, column = 0)

##############
rand = StringVar()
fries_inp = StringVar()
samosa_inp = StringVar()
samosa_inp1 = StringVar()
burger_inp1 = StringVar()
fries_inp1 = StringVar()
drinks_inp1 = StringVar()
burger_inp = StringVar()
drinks_inp = StringVar()
total_inp = StringVar()
###############

def ref():
    subtotal=fries_inp*fries_inp1
    print(subtotal.set(txt_total))


#############
fries = Label(left, font=('arial',16,'bold'),text = "Fries", bd = 16 )
fries.grid(row=1,column=0,sticky = E)
txt_fries = Entry(left,font=('arial',16,'bold'), textvariable=fries_inp, bd=10, insertwidth =4,bg = "powder blue", justify ='right')
txt_fries.grid(row=1,column=1)

txt_fries1 = Entry(left,font=('arial',16,'bold'), textvariable=fries_inp1, bd=10, insertwidth =4,bg = "powder blue", justify ='right')
txt_fries1.grid(row=1,column=2)

samosa = Label(left, font=('arial',16,'bold'),text = "Samosa", bd = 16, anchor = 'w' )
samosa.grid(row=2,column=0,sticky = E)
txt_samosa = Entry(left,font=('arial',16,'bold'), textvariable=samosa_inp, bd=10, insertwidth =4,bg = "powder blue", justify ='right')
txt_samosa.grid(row=2,column=1)

txt_samosa1 = Entry(left,font=('arial',16,'bold'), textvariable=samosa_inp1, bd=10, insertwidth =4,bg = "powder blue", justify ='right')
txt_samosa1.grid(row=2,column=2)
burger = Label(left, font=('arial',16,'bold'),text = "Burger", bd = 16, anchor = 'w' )
burger.grid(row=3,column=0,sticky = E)
txt_burger = Entry(left,font=('arial',16,'bold'), textvariable=burger_inp, bd=10, insertwidth =4,bg = "powder blue", justify ='right')
txt_burger.grid(row=3,column=1)

txt_burger1 = Entry(left,font=('arial',16,'bold'), textvariable=burger_inp1, bd=10, insertwidth =4,bg = "powder blue", justify ='right')
txt_burger1.grid(row=3,column=2)

drinks = Label(left, font=('arial',16,'bold'),text = "Drinks", bd = 16, anchor = 'w' )
drinks.grid(row=4,column=0,sticky = E)
txt_drinks = Entry(left,font=('arial',16,'bold'), textvariable=drinks_inp, bd=10, insertwidth =4,bg = "powder blue", justify ='right')
txt_drinks.grid(row=4,column=1)

txt_drinks1 = Entry(left,font=('arial',16,'bold'), textvariable=drinks_inp1, bd=10, insertwidth =4,bg = "powder blue", justify ='right')
txt_drinks1.grid(row=4,column=2)

total = Label(left, font=('arial',16,'bold'),text = "Total Cost", bd = 16, anchor = 'w' )
total.grid(row=5,column=1,sticky = E)
txt_total = Entry(left,font=('arial',16,'bold'), textvariable=total_inp, bd=10, insertwidth =4,bg = "powder blue", justify ='right')
txt_total.grid(row=5,column=2)
############

btn_total = Button(left, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',16,'bold'), width=10, text= "Total", bg= "powder blue",command = ref)
btn_total.grid(row=7, column= 1)
