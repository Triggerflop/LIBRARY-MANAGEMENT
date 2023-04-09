from tkinter import * 
import PIL
from PIL import ImageTk, Image
import ast
import sqlite3
# from APP import * 

database_connection = sqlite3.connect("LIBRARY.db")
database_cursor = database_connection.cursor()

def signuping():
    name = en1.get()
    mailing = en3.get()
    pas = en6.get()
    repas = en7.get()

    insertAdmin = "insert into ADMIN values('" "','"+name+"','"+pas+"','"+emailing+"','"+mobile+"');"
    insertUser = "insert into USER values('" "','"+name+"','"+pas+"','"+emailing+"','"+mobile+"');"

    if():
        try:
            database_cursor.execute()
            messagebox.showinfo("Success","You have registered successfully")
        except:
            messagebox.showinfo("Error","Sorry you are not able to register")
    else:
        try:
            database_cursor.execute()
            messagebox.showinfo("Success","You have registered successfully")
        except:
            messagebox.showinfo("Error","Sorry you are not able to register")
            
    pass






def signUp():

    global en7,en1,en3,en6


    # App.root.destroy()

    base = Tk()  


    # Open window having dimension 100x100
    base.geometry('800x500+10+20')
    base.title("SIGNUP form")

    # canvas = Canvas(base,width=400,heigh=400,bg="black")
    # img = PhotoImage(file="pict.jpg")
    # canvas.create_image(0,0,anchor=NW,image=img)
    # canvas.pack(pady=20)  

    labl_0 = Label(base, text="SIGN UP",width=20,font=("bold", 20))  
    labl_0.place(x=230,y=60)  
    
    lb1= Label(base, text="Enter Name", width=10, font=("arial",12))  
    lb1.place(x=200, y=120)  
    en1= Entry(base)  
    en1.place(x=380, y=120)  
    
    lb3= Label(base, text="Enter Email", width=10, font=("arial",12))  
    lb3.place(x=200, y=160)  
    en3= Entry(base)  
    en3.place(x=380, y=160)  
    
    
    
    lb5= Label(base, text="REGISTER AS ", width=15, font=("arial",12))  
    lb5.place(x=180, y=240)  
    vars = IntVar()  
    Radiobutton(base, text="USER", padx=5,variable=vars, value=1).place(x=380, y=240)  
    Radiobutton(base, text="ADMIN", padx =10,variable=vars, value=2).place(x=440,y=240)  
    

    
    
    lb6= Label(base, text="Enter Password", width=13,font=("arial",12))  
    lb6.place(x=200, y=280)  
    en6= Entry(base, show='*')  
    en6.place(x=380, y=280)  
    
    lb7= Label(base, text="Re-Enter Password", width=15,font=("arial",12))  
    lb7.place(x=200, y=320)  
    en7 =Entry(base, show='*')  
    en7.place(x=380, y=320)  
    
    Button(base, text="Register",commmand=signuping, width=20).place(x=300,y=400)  
    base.mainloop()  