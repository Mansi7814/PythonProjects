from tkinter import*
import tkinter.messagebox


root1 = Tk()
root1.geometry("1590x820+0+0")
root1.title("Login Page")
root1.configure(background='red')
def back():
    root1.destroy()
    import question

fries_p=StringVar()
samosa_p=StringVar()
burger_p=StringVar()
drinks_p=StringVar()
Ice_cream_p=StringVar()
pestry_p=StringVar()
chicken_tikka=IntVar()

f1 = open('value.txt','r')
line = f1.readlines()
fries_p.set(float(line[0]))
samosa_p.set(float(line[1]))
burger_p.set( float(line[2]))
drinks_p.set(float(line[3]))
Ice_cream_p.set( float(line[4]))
pestry_p.set(float(line[5]))

f1.close()


scrollbar = Scrollbar(root1)
scrollbar.pack( side = RIGHT, fill = Y )

background_image = PhotoImage(file="image/Burger.png")
background = Label(root1, image=background_image,
                   bg="white",bd=0)
background.place(x=10,y=10)

Label(root1,text="Burger",bg="red",font= ('Colonna MT',30,'bold')).place(x=85,y=250)
Label(root1,textvariable=burger_p,bg="red",font=('Arial',30,'bold')).place(x=95,y=300)

background_image1 = PhotoImage(file="image/samosa.png")
background1 = Label(root1, image=background_image1,
                   bg="white",bd=0)
background1.place(x=320,y=10)

Label(root1,text="Samosa",bg="red",font= ('Colonna MT',30,'bold')).place(x=395,y=250)
Label(root1,textvariable=samosa_p,bg="red",font=('Arial',30,'bold')).place(x=405,y=300)

background_image2 = PhotoImage(file="image/chicken-chowmein.png")
background2 = Label(root1, image=background_image2,
                   bg="white",bd=0)
background2.place(x=630,y=10)

Label(root1,text="Chowmeen",bg="red",font= ('Colonna MT',30,'bold')).place(x=675,y=250)
Label(root1,text="50.0",bg="red",font=('Arial',30,'bold')).place(x=720,y=300)

background_image3 = PhotoImage(file="image/illi-potat.png")
background3 = Label(root1, image=background_image3,
                   bg="white",bd=0)
background3.place(x=940,y=10)

Label(root1,text="Chilli-Patato",bg="red",font= ('Colonna MT',30,'bold')).place(x=975,y=250)
Label(root1,text="45.0",bg="red",font=('Arial',30,'bold')).place(x=1040,y=300)

background_image4 = PhotoImage(file="image/ice_cream_PNG20991.png")
background4 = Label(root1, image=background_image4,
                   bg="white",bd=0)
background4.place(x=1250,y=10)

Label(root1,text="Ice-Cream",bg="red",font= ('Colonna MT',30,'bold')).place(x=1300,y=250)
Label(root1,textvariable=Ice_cream_p,bg="red",font=('Arial',30,'bold')).place(x=1340,y=300)

background_image5 = PhotoImage(file="image/fries_PNG6.png")
background5 = Label(root1, image=background_image5,
                   bg="white",bd=0)
background5.place(x=10,y=410)

Label(root1,text="Fries",bg="red",font= ('Colonna MT',30,'bold')).place(x=100,y=650)
Label(root1,textvariable=fries_p,bg="red",font=('Arial',30,'bold')).place(x=100,y=700)

background_image6 = PhotoImage(file="image/Chicken-tikka-kabab.png")
background6 = Label(root1, image=background_image6,
                   bg="white",bd=0)
background6.place(x=320,y=410)

Label(root1,text="Chicken-tikka",bg="red",font= ('Colonna MT',30,'bold')).place(x=340,y=650)
Label(root1,text="75.0",bg="red",font=('Arial',30,'bold')).place(x=420,y=700)

background_image7 = PhotoImage(file="image/spring-rolls_category.png")
background7 = Label(root1, image=background_image7,
                   bg="white",bd=0)

background7.place(x=630,y=410)


Label(root1,text="Spring-rolls",bg="red",font= ('Colonna MT',30,'bold')).place(x=670,y=650)
Label(root1,text="35.0",bg="red",font=('Arial',30,'bold')).place(x=720,y=700)

background_image8 = PhotoImage(file="image/pestry.png")
background8 = Label(root1, image=background_image8,
                   bg="white",bd=0)
background8.place(x=940,y=410)

Label(root1,text="Pestry",bg="red",font= ('Colonna MT',30,'bold')).place(x=1020,y=650)
Label(root1,textvariable=pestry_p,bg="red",font=('Arial',30,'bold')).place(x=1040,y=700)

background_image9 = PhotoImage(file="image/drink.png")
background9 = Label(root1, image=background_image9,
                   bg="white",bd=0)
background9.place(x=1250,y=410)


Label(root1,text="Drink",bg="red",font= ('Colonna MT',30,'bold')).place(x=1340,y=650)
Label(root1,textvariable=drinks_p,bg="red",font=('Arial',30,'bold')).place(x=1340,y=700)


btn_bck = Button(root1, padx= 16, pady= 5, bd= 16, fg= "black", font=('arial',16,'bold'), width=10, text= "Back", bg= "red",command=back)
btn_bck.place(x=650,y=750)





root1.mainloop()
