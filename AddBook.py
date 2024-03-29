from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3
import os
import email
from email.message import EmailMessage
import ssl
import smtplib

def bookRegister():
    
    bid = bookInfo1.get()
    title = bookInfo2.get()
    btype = bookInfo5.get()
    price = bookInfo6.get()
    bcount = bookInfo7.get()
    author = bookInfo3.get()
    # status = bookInfo4.get()
    # status = status.lower()
    
    database_connection = sqlite3.connect("LIBRARY.db")
    database_cursor = database_connection.cursor()


    insertBooks = "insert into "+bookTable+" values('"+bid+"','"+title+"','"+btype+"','"+price+"','"+bcount+"','"+author+"');"
    try:
        database_cursor.execute(insertBooks)
        
        
        

        e = database_cursor.execute('''SELECT EMAIL FROM USER;''')

        for i in e:

            email_sender = 'autolibpy@gmail.com'
            email_password = 'epemdruoebcgmtta'
            email_reciever = i[0]

            print(email_reciever)

            subject = 'test mail'
            body = """
            Hi,
            Checkout our new book: """ +title+""" 
            written by,
                      """ +author+"""




            THANK YOU!!!!
            """


            em = EmailMessage()
            em['From'] = email_sender
            em['To']  = email_reciever
            em['subject'] = subject
            em.set_content(body)

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_reciever, em.as_string())


        database_connection.commit()    
        database_connection.close()
        messagebox.showinfo('Success',"Book added successfully")


    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    print(insertBooks)
    print(bid)
    print(title)
    print(author)
    # print(status)
    print(btype)
    print(bcount)
    print(price)

    root.destroy()
    
def addBook(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo5,bookInfo6,bookInfo7,Canvas1,con,cur,bookTable,root
    # bookInfo4

    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # Add your own database name and password here to reflect in the code
    # mypass = "root"
    # mydatabase="db"

    # con = sqlite3.connect(database=mydatabase)
    # cur = con.cursor()

    # Enter Table Names here
    bookTable = "BOOKS" # Book Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.05, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.05, relwidth=0.62, relheight=0.08)
        
    # Title
    lb2 = Label(labelFrame,text="Title : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.20, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.20, relwidth=0.62, relheight=0.08)
        
    # Book Author
    lb3 = Label(labelFrame,text="Author : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.35, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    # Book Status
    # lb4 = Label(labelFrame,text="Status(Avail/issued) : ", bg='black', fg='white')
    # lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    # bookInfo4 = Entry(labelFrame)
    # bookInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)

    # Book type
    lb5 = Label(labelFrame,text="Book Type : ", bg='black', fg='white')
    lb5.place(relx=0.05,rely=0.50, relheight=0.08)
        
    bookInfo5 = Entry(labelFrame)
    bookInfo5.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)

    # Book price
    lb6 = Label(labelFrame,text="Book Price : ", bg='black', fg='white')
    lb6.place(relx=0.05,rely=0.65, relheight=0.08)
        
    bookInfo6 = Entry(labelFrame)
    bookInfo6.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)

    # Book count
    lb7 = Label(labelFrame,text="Number of book : ", bg='black', fg='white')
    lb7.place(relx=0.05,rely=0.80, relheight=0.08)
        
    bookInfo7 = Entry(labelFrame)
    bookInfo7.place(relx=0.3,rely=0.80, relwidth=0.62, relheight=0.08)
        
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=bookRegister)
    SubmitBtn.place(relx=0.28,rely=0.90, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.90, relwidth=0.18,relheight=0.08)
    
    root.mainloop()