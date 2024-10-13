from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
# helps to connect python to mysql
import pymysql

# clears text in boxes after registration
def clear():
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmEntry.delete(0, END)

# All boxes must be filled and must be correct
def connect_database():
    if usernameEntry.get() == '' or passwordEntry.get() == '' or confirmEntry.get() == '':
        messagebox.showerror('Error', 'ALL FIELDS ARE REQUIRED')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error', 'Passwords Do Not Match!')
    else:
        # if connection is successful then this will be done
        try:
            con = pymysql.connect(host='localhost', user='root', password='Adil105729')
            mycursor = con.cursor()
        except:
            # else if can't connect then error will occur
            messagebox.showerror('ERROR', 'Database Connectivity Issue, Please Try Again')
            return
        
        # This will create user data database
        try:
            query = 'create database userdata'
            mycursor.execute(query)
            query = 'use userdata'
            mycursor.execute(query)
            query = 'create table data(id int auto_increment primary key not null, username varchar(10), password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')

#if data already exists then error will appear
query = 'select * from data where username=%s'
mycursor.execute(query,(usernameEntry.get()))

row = mycursor.fetchone()
if row != None:
    messagebox.showerror('ERROR', 'Username Already exists')

else:
    #data will be inserted into data table
    query='insert into data(username,password) values(%s, %s)'
    mycursor.execute(query,(usernameEntry.get(), passwordEntry.get()))
    con.commit()
    con.close()
    messagebox.showinfo('Success', 'Registration is successful')
    clear()
    #closes signup window when registration is successful and boots login page
    signup_window.destroy()
    import signin

#links signup and login windows
def login_page():
    #signup window will be destroyed
    signup_window.destroy()
    #signin page will be shown
    import signin

signup_window = Tk()
signup_window.title('signup Page')
signup_window.resizable(0, 0)
background = ImageTk.PhotoImage(file="bg.jpg")

bgLabel=Label(signup_window, image=background)
bgLabel.grid()

frame=Frame(signup_window, bg="white")
frame.place(x=320, y=80)

heading = Label(frame, text='CREATE AN ACCOUNT', font=('Microsoft Yahei UI Light', 24, 'bold '), bg ='white')
heading.grid(row=0, column=0, padx=10, pady=10)

#create username box
usernameLabel=Label(frame, text='Username', font=("Microsoft Yahei UI Light", 12, 'bold '), fg='black', bg='white')
usernameLabel.grid(row=1, column=0, sticky='w', padx=25, pady=(10,0))

usernameEntry=Entry(frame, width=25, font=('Microsoft Yahei UI Light', 12, 'bold'), fg='white', bg="#558F1E")
usernameEntry.grid(row=2, column=0, sticky='w', padx=25)

#create password box
passwordLabel=Label(frame, text='Password', font=("Microsoft Yahei UI Light", 12, 'bold '), fg='black', bg='white')
passwordLabel.grid(row=3, column=0, sticky='w', padx=25, pady=(10,0))

passwordEntry=Entry(frame, width=25, font=('Microsoft Yahei UI Light', 12, 'bold'), fg='white', bg="#558F1E")
passwordEntry.grid(row=4, column=0, sticky='w', padx=25)

#create confirm password
confirmLabel=Label(frame, text='Confirm Password', font=("Microsoft Yahei UI Light", 12, 'bold '), fg='black', bg='white')
confirmLabel.grid(row=5, column=0, sticky='w', padx=25, pady=(10,0))

confirmEntry=Entry(frame, width=25, font=('Microsoft Yahei UI Light', 12, 'bold'), fg='white', bg="#558F1E")
confirmEntry.grid(row=6, column=0, sticky='w', padx=25)

#create sign up button
signupButton=Button(frame, text="Sign Up!!", font=('Open Sans', 15, 'bold '), bd=0, bg="#558F1E", fg="black", 
                    activebackground="#558F1E", activeforeground='black', width=20, command=connect_database)
signupButton.place(x=28, y=270)

#create already have an account text
alreadyaccount=Label(frame, text="Already have an account?", font=('Open Sans', 10, 'bold'), 
                     bg='white', fg='black')
alreadyaccount.grid(row=8, column=0, sticky='w', padx=25, pady=80)

#create Log in button which takes you back to login
loginButton=Button(frame, text='Log in', font=('Open Sans', 11, 'bold underline'), 
                   bg='white', fg='black', bd=0, cursor='hand2', activebackground='white', 
                   activeforeground='black', command=login_page)
loginButton.place(x=200, y=328)

signup_window.mainloop()
