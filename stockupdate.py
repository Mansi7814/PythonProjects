from tkinter import*
import tkinter.messagebox


left1 = Tk()
left1.geometry("1600x800+0+0")
left1.title("Change Price")
left1.configure(background='red')

label4 = Label(left1, font = ('arial',50,'bold'), text ="Stock Update", fg = "steel blue", bd = 10, anchor = 'w')
label4.grid(row = 0)


fries_inp_p = StringVar()
samosa_inp_p = StringVar()
burger_inp_p = StringVar()
drinks_inp_p = StringVar()
paneer_tikka_inp_p = StringVar()
chicken_tikka_inp_p = StringVar()

def update():
	f = open('stock.txt','r')
	line = f.readlines()
	
	drinks_p = (line[0])
	paneer_tikka_p = (line[1])
	chicken_tikka_p = (line[2])
	f.close()
	
	f2 = open('stock.txt','w')
	

	try:
		CoD1 = (drinks_inp_p.get())
	except Exception as e:
		if drinks_inp_p.get() != "":
			tkinter.messagebox.showinfo('Error','Incorrect Input')
		drinks_inp_p.set("")
		f2.write(str(drinks_p)+"\n")
	else:
		f2.write(str(CoD1)+"\n")

	try:
		CoP1 = (paneer_tikka_inp_p.get())
	except Exception as e:
		if paneer_tikka_inp_p.get() != "":
			tkinter.messagebox.showinfo('Error','Incorrect Input')
		paneer_tikka_inp_p.set("")
		f2.write(str(paneer_tikka_p)+"\n")
	else:
		f2.write(str(CoP1)+"\n")

	try:
		CoC1 = (chicken_tikka_inp_p.get())
	except Exception as e:
		if chicken_tikka_inp_p.get() != "":	
			tkinter.messagebox.showinfo('Error','Incorrect Input')
		chicken_tikka_inp_p.set("")
		f2.write(str(chicken_tikka_p))
	else:
		f2.write(str(CoC1))
	
	#f.write(str(samosa_p) +"\n"+ str(paneer_tikka_p) +"\n"+ str(chicken_tikka_p) +"\n"+ str(fries_p) +"\n"+ str(burger_p) +"\n"+ str(drinks_p))
	
	tkinter.messagebox.showinfo('Update Box','Successfully Updated')
	f2.close()	

def reset1():
	
	drinks_inp_p.set("")
	paneer_tikka_inp_p.set("")
	chicken_tikka_inp_p.set("")


def backfn():
	left1.destroy()
	import stock




drinks = Label(left1, font=('arial',16,'bold'),text = "Drinks",bg="red", bd = 16, anchor = 'w' )
drinks.grid(row=4,column=0,sticky = E)
txt_drinks = Entry(left1,font=('arial',16,'bold'), textvariable=drinks_inp_p, bd=10, insertwidth =4,bg = "powder blue", justify ='right')
txt_drinks.grid(row=4,column=1)

paneer_tikka = Label(left1, font=('arial',16,'bold'),text = "Ice-Cream",bg="red", bd = 16, anchor = 'w' )
paneer_tikka.grid(row=5,column=0,sticky = E)
txt_paneer_tikka = Entry(left1,font=('arial',16,'bold'), textvariable=paneer_tikka_inp_p, bd=10, insertwidth =4,bg = "powder blue", justify ='right')
txt_paneer_tikka.grid(row=5,column=1)

chicken_tikka = Label(left1, font=('arial',16,'bold'),text = "Pestry",bg="red", bd = 16, anchor = 'w' )
chicken_tikka.grid(row=6,column=0,sticky = E)
txt_chicken_tikka = Entry(left1,font=('arial',16,'bold'), textvariable=chicken_tikka_inp_p, bd=10, insertwidth =4,bg = "powder blue", justify ='right')
txt_chicken_tikka.grid(row=6,column=1)


btn_update = Button(left1, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',16,'bold'), width=10, text= "Update", bg= "red",command = update)
btn_update.grid(row=7, column= 1)

btn_reset1 = Button(left1, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',16,'bold'), width=10, text= "Reset", bg= "red",command = reset1)
btn_reset1.grid(row=7, column= 2)


btn_back = Button(left1, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',16,'bold'), width=10, text= "Back", bg= "red",command = backfn)
btn_back.grid(row=8, column= 1)



left1.mainloop()





