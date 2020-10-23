from tkinter import *
root=Tk()
left = Frame(root, width = 800
             , height = 700, relief = SUNKEN)
left.pack(side = LEFT)
drinks_inp=StringVar()
txt_drinks = Entry(left,font=('arial',16,'bold'), textvariable=drinks_inp, bd=10, bg = "powder blue", justify ='right')
txt_drinks.grid(row=4,column=1)
