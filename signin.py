from tkinter import *
from tkinter import messagebox
# from Pillow - python image library - import image class
from PIL import ImageTk
import pymysql

# Functionality part
def login_user():
    if usernameEntry.get() == "" or passwordEntry.get() == "":
        messagebox.showerror('Error', 'All Fields Are Required!')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='Adil105729')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Connection is not established, Please Try Again!')

        # Try to check in database whether the username and password user is entering match the one in database
        query = 'use userdata'
        mycursor.execute(query)
        query = 'select * from data where username=%s and password=%s'
        mycursor.execute(query, (usernameEntry.get(), passwordEntry.get()))

        # If user is entering wrong username or password
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error', 'Invalid username or password!')
        else:
            login_window.destroy()
            import Main_Menu

def signup_page():
    # Destroys login page
    login_window.destroy()
    # Displays signup page
    import signup

# when open eye is clicked, it changes/configs to closed eye
def hide():
    openeye.config(file='closeeye.png')
    # when close eye is clicked the password is hashed
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

# When eye is clicked again, it should change back to open eye and show password
def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

# text in box will be deleted when user clicks on box
def user_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)

def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)

# GUI part
# login_window is object variable, Tk is class name
login_window = Tk()
login_window.geometry('926x644+200+30')
# Disables the full screen function by passing false values
login_window.resizable(0, 0)
# Adds title to the top of the window
login_window.title('Login')

bgImage = ImageTk.PhotoImage(file='bg.jpg')

# create image on the label, login_window as we want to see our label on window,
bgLabel = Label(login_window, image=bgImage)

# sets position of image
bgLabel.place(x=-34, y=5)
heading = Label(login_window, text='USER LOGIN', font=('Microsoft Yahei UI Light', 24, 'bold'), bg='white')
heading.place(x=340, y=170)

# Creates the Username box
usernameEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 12, 'bold'), bd=0)
# sets the box's placement on screen
usernameEntry.place(x=320, y=250)
usernameEntry.insert(0, 'Username')

usernameEntry.bind('<FocusIn>', user_enter)
frame1 = Frame(login_window, width=250, height=2, bg='#558F1E')
frame1.place(x=320, y=271)

# Creates the Password box
passwordEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 12, 'bold'), bd=0)
# sets the box's placement on screen
passwordEntry.place(x=320, y=300)
passwordEntry.insert(0, 'Password')

passwordEntry.bind('<FocusIn>', password_enter)
frame2 = Frame(login_window, width=250, height=2, bg='#558F1E')
frame2.place(x=320, y=323)

openeye = PhotoImage(file='openeye.png')

# creating the eye button and switching the mouse cursor to hand when mouse is hovering over it
eyeButton = Button(login_window, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2', command=hide)
eyeButton.place(x=548, y=300)

# Creating the Login Button
loginButton = Button(login_window, text='Login', font=('Open Sans', 16, 'bold'), fg='black', bg='#558F1E', activeforeground='black', activebackground='#558F1E', cursor='hand2', bd=0, width=19, command=login_user)
loginButton.place(x=315, y=350)

# Creating ---OR---
orlabel = Label(login_window, text='-------------------- OR -------------------', 
                font=('Open Sans', 16), fg='#558F1E', bg='white')
orlabel.place(x=315, y=405)

# Creating the 'don't have an account?'
signuplabel = Label(login_window, text="Don't have an account?", 
                    font=('Open Sans', 15, 'bold'), fg='#558F1E', bg='white')
signuplabel.place(x=315, y=445)

# Creating the signup button
newaccountButton = Button(login_window, text='Create new account', 
                          font=('Open Sans', 13, 'bold underline'), 
                          fg='black', bg='#558F1E', activeforeground='black', 
                          activebackground='#558F1E', cursor='hand2', bd=0, 
                          command=signup_page)
newaccountButton.place(x=350, y=500)

login_window.mainloop()

