from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3

# Add your own database name and password here to reflect in the code
# mypass = "root"
# mydatabase="db"

database_connection = sqlite3.connect("LIBRARY.db")
database_cursor = database_connection.cursor()

# Enter Table Names here
# issueTable = "books_issued" 
bookTable = "BOOKS" #Book Table


def deleteBook():
    
    bid = bookInfo1.get()

    # database_connection = sqlite3.connect("LIBRARY.db")
    # database_cursor = database_connection.cursor()
    
    deleteSql = "DELETE from BOOKS where BOOK_ID ="+bid+";"
    # deleteIssue = "delete from "+issueTable+" where bid = '"+bid+"'"
    try:
        print(deleteSql)
        database_cursor.execute(deleteSql)
        database_connection.commit()
        # cur.execute(deleteIssue)
        # con.commit()
        
        messagebox.showinfo('Success',"Book Record Deleted Successfully")
    except:
        messagebox.showinfo("Please check Book ID")
    

    print(bid)

    bookInfo1.delete(0, END)
    root.destroy()
    # database_connection.close()


def delete(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo5,bookInfo6,bookInfo7,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    Canvas1 = Canvas(root)
        
    Canvas1.config(bg="ORANGE")
    Canvas1.pack(expand=True,fill=BOTH)
            
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Delete Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    lb2 = Label(labelFrame,text="Book ID : ", bg='black', fg='white', font=('Calisto MT',11))
    lb2.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteBook, font=('Calisto MT',10))
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy, font=('Calisto MT',10))
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()