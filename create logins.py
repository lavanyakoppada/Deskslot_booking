import mysql.connector
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from datetime import *
from tkinter import Tk, Frame, Entry, Label, messagebox, Button, Radiobutton
from tkcalendar import Calendar

fonts = ('Times New Roman', 20, 'bold')

class Login:
    def __init__(self, root):
        self.root = root
        self.login_frame = Frame(self.root, width = 900, height = 650, bg = 'dark turquoise')
        self.login_frame.place(x = 0, y = 0)
        #create account
        self.create_button = Button(self.login_frame, text = 'CREATE', bg = 'white', fg = 'steel blue', command = self.create, font = fonts, cursor = 'hand2', activebackground = 'Rosy Brown1', width = 10)
        self.create_button.place(x = 360, y = 420)
        #image 
        self.im = ImageTk.PhotoImage(Image.open("..//assets//svecw.png"))
        self.img_label = Label(self.login_frame, image = self.im)
        self.img_label.place(x = 240 ,y = 90)
        #label for reg.no
        self.reg_no_label = Label(self.login_frame, text = 'Admission Number', font = fonts, bg = 'dark turquoise', fg = 'navy', width =40)
        self.reg_no_label.place(x = 50, y = 225)
        self.reg_no_entry = Entry(self.login_frame, width  = 13, font = fonts, bg = 'white')
        self.reg_no_entry.place(x = 490, y = 225)
        #label for password
        self.passw_label = Label(self.login_frame, text = 'Password', font = fonts, bg = 'dark turquoise', fg = 'navy', width = 10)
        self.passw_label.place(x = 250, y = 275)
        self.passw_entry = Entry(self.login_frame, width  = 13, font = fonts, bg = 'white', show = '*')
        self.passw_entry.place(x = 490, y = 275)
        #label for button
        self.login_btn = Button(self.login_frame, text = 'LOGIN', bg = 'white', fg = 'steel blue', command = self.check, font = fonts, cursor = 'hand2', activebackground = 'Rosy Brown1')
        self.login_btn.place(x = 390, y = 350)

    #checking valid student
    def check(self):
        self.regno = self.reg_no_entry.get()
        self.password = self.passw_entry.get()

        command = f"SELECT * FROM StudentDetails WHERE StudentId = '{self.regno}' AND password = '{self.password}'"
        cursor.execute(command)
        result = cursor.fetchone()
        if result:
            messagebox.showinfo('WELCOME','WELCOME ' + self.regno)
            self.login_frame.destroy()
            block = SelectBlock(self.root)
        else:
            messagebox.showerror('INVALID CREDENTIALS','CHECK YOUR CREDENTIALS')


    def create(self):
        self.login_frame.destroy()
        createstudent = Create(root)

class Create:
    def __init__(self, root):
        self.root = root
        self.root.title('Create a login')
        self.create_frame = Frame(self.root, width = 900, height = 650, bg = 'dark turquoise')
        self.create_frame.place(x = 0, y = 0)
        #label for reg. no
        self.reg_no_label = Label(self.create_frame, text = 'Admission Number', font = fonts, bg = 'dark turquoise', fg = 'navy', width =40)
        self.reg_no_label.place(x = 50, y = 225)
        self.reg_no_entry = Entry(self.create_frame, width  = 13, font = fonts, bg = 'white')
        self.reg_no_entry.place(x = 490, y = 225)
        #label for password
        self.passw_label = Label(self.create_frame, text = 'Password', font = fonts, bg = 'dark turquoise', fg = 'navy', width = 10)
        self.passw_label.place(x = 250, y = 275)
        self.passw_entry = Entry(self.create_frame, width  = 13, font = fonts, bg = 'white', show = '*')
        self.passw_entry.place(x = 490, y = 275)
        self.enter_button = Button(self.create_frame, text = 'SUBMIT', bg = 'white', fg = 'steel blue', command = self.save, font = fonts, cursor = 'hand2', activebackground = 'Rosy Brown1')
        self.enter_button.place(x = 390, y = 350)

    def save(self):
        #need
        self.regno = self.reg_no_entry.get()
        self.password = self.passw_entry.get()
        self.query = f"insert into StudentDetails values('{self.regno}','{self.password}')"
        cursor.execute(self.query)
        conn.commit()
        messagebox.showinfo('SUCCESS', 'Successfully created the account')
        self.create_frame.destroy()
        login = Login(root)

class SelectBlock:
    def __init__(self, root):
        self.root = root
        self.root.title('DESKSLOT BOOKING')
        self.time_frame = Frame(self.root, width = 900, height = 650, bg = 'aqua')
        self.time_frame.place(x = 0, y = 0)
        #label for selecting date
        self.date_label = Label(self.time_frame, text = 'Date', font = fonts, bg = 'aqua', fg = 'navy', width = 10)
        self.date_label.place(x = 40, y = 100)
        self.date_cal = Calendar(self.time_frame, selectmode = 'day', year = 2023, month = 10, day = 10)
        self.date_cal.pack(pady = 20)
        self.date_cal.place(x = 165, y = 100)
        #label for selecting time
        self.time_label = Label(self.time_frame, text = 'Start Time', font = fonts, bg = 'aqua', fg = 'navy', width = 10)
        self.time_label.place(x = 450, y = 100)
        self.time_entry = Entry(self.time_frame, width  = 5, font = fonts, bg = 'white')
        self.time_entry.place(x = 620, y = 100)
        #label for choosing duration
        self.duration_label = Label(self.time_frame, text = 'End Time', font = fonts, bg = 'aqua', fg = 'navy', width = 9)
        self.duration_label.place(x = 450, y = 150)
        self.duration_entry = Entry(self.time_frame, width  = 5, font = fonts, bg = 'white', textvariable= 'hours')
        self.duration_entry.place(x = 620, y = 150)
        #radio buttons
        '''self.select = tk.StringVar()
        self.amradiobutton = Radiobutton(self.time_frame, text = 'AM', variable = self.select, value = "AM", textvariable= 'false')
        self.amradiobutton.pack(pady = 50)
        self.amradiobutton.place(x = 700, y = 100)
        self.pmradiobutton = Radiobutton(self.time_frame, text = 'PM', variable = self.select, value = "PM")
        self.pmradiobutton.pack(pady = 50)
        self.pmradiobutton.place(x = 750, y = 100)'''
        #label for button
        self.submit_btn = Button(self.time_frame, text = 'SUBMIT', bg = 'white', fg = 'steel blue', command = self.bookdesks, font = fonts, cursor = 'hand2', activebackground = 'Rosy Brown1')
        self.submit_btn.place(x = 400, y = 350)
    #booking desks
    def bookdesks(self):
        '''self.t = self.time_entry.get()
        self.d = self.duration_entry.get()
        if self.t in accepted :
            if self.d in rangedur:  
                self.d_212_button = Button(self.time_frame,  text = 'D-211', bg = 'white', fg = 'steel blue', command = self.bookdesks_in_d211, font = fonts, cursor = 'hand2', activebackground = 'burlywood1', width = 45)
                self.digilib_button = Button(self.time_frame,  text = 'DIGITAL LIBRARY', bg = 'white', fg = 'steel blue', command = self.bookdesks_in_digilib, font = fonts, cursor = 'hand2', activebackground = 'burlywood1', width = 45)       
                self.d_212_button.place(x = 100, y = 450)
                self.digilib_button.place(x = 100, y = 550)
            else:
                messagebox.showerror('EROOR', 'Please enter duration in range of 1 - 3 hours')
        else:
            messagebox.showerror('ERROR', 'Enter valid Time')'''
        pass

    def bookdesks_in_d211(self):
        pass
    def bookdesks_in_digilib(self):
        pass

class Booking:
    pass

class Adminlog:
    
    def __init__(self, root):
        self.root = root
        self.login_frame = Frame(self.root, width = 900, height = 650, bg = 'dark turquoise')
        self.login_frame.place(x = 0, y = 0)
        #image 
        self.im = ImageTk.PhotoImage(Image.open("..//assets//svecw.png"))
        self.img_label = Label(self.login_frame, image = self.im)
        self.img_label.place(x = 240 ,y = 90)
        #label for admin.no
        self.adminId_label = Label(self.login_frame, text = 'Employee ID', font = fonts, bg = 'dark turquoise', fg = 'navy', width =40)
        self.adminId_label.place(x = 28, y = 225)
        self.adminId_entry = Entry(self.login_frame, width  = 13, font = fonts, bg = 'white')
        self.adminId_entry.place(x = 490, y = 225)
        #label for password
        self.adminpassw_label = Label(self.login_frame, text = 'Password', font = fonts, bg = 'dark turquoise', fg = 'navy', width = 10)
        self.adminpassw_label.place(x = 250, y = 275)
        self.adminpassw_entry = Entry(self.login_frame, width  = 13, font = fonts, bg = 'white', show = '*')
        self.adminpassw_entry.place(x = 490, y = 275)
        #label for button
        self.login_btn = Button(self.login_frame, text = 'LOGIN', bg = 'white', fg = 'steel blue', command = self.check, font = fonts, cursor = 'hand2', activebackground = 'Rosy Brown1')
        self.login_btn.place(x = 390, y = 350)
        #label for going back
        self.back_btn = Button(self.login_frame, text = 'BACK', bg = 'white', fg = 'steel blue', command = self.back, font = fonts, cursor = 'hand2', activebackground = 'Rosy Brown1')
        self.back_btn.place(x = 50, y = 650)

    def back(self):
        pass

    def check(self):
        self.adminid = self.adminId_entry.get()
        self.password = self.adminpassw_entry.get()

        command = f"SELECT * FROM Admin WHERE empId = '{self.adminid}' AND password = '{self.password}'"
        cursor.execute(command)
        result = cursor.fetchone()
        if result:
            messagebox.showinfo('WELCOME','WELCOME ' + self.adminid)
            self.login_frame.destroy()
            detailsOfBooking = Booking(self.root)
        else:
            messagebox.showerror('INVALID CREDENTIALS','CHECK YOUR CREDENTIALS')


class Welcome:
    def __init__(self, root):
        self.root = root
        self.Welcomeframe = Frame(self.root, width = 900, height = 650, bg = 'dark turquoise')
        self.Welcomeframe.place(x = 0, y = 0)

        self.im = ImageTk.PhotoImage(Image.open("..//assets//vishnu_logo.png"))
        self.img_label = Label(self.Welcomeframe, image = self.im)
        self.img_label.place(x = 50 ,y = 100, width= 460)

        self.Wellabel = Label(self.Welcomeframe, text = 'GET STARTED WITH', font = fonts, bg = 'dark turquoise', fg = 'navy')
        self.Wellabel.place(x = 560, y = 150)
        self.Wellabel2 = Label(self.Welcomeframe, text = 'DESKSLOT !!', font = fonts, bg = 'dark turquoise', fg = 'navy')
        self.Wellabel2.place(x = 615, y = 200)

        self.Stud_login_btn = Button(self.Welcomeframe, text = 'Student', bg = 'white', fg = 'steel blue', command = self.studlogin, font = fonts, cursor = 'hand2', activebackground = 'Rosy Brown1')
        self.Stud_login_btn.place(x = 630, y = 390)

        self.Admin_login_btn = Button(self.Welcomeframe, text = 'Admin', bg = 'white', fg = 'steel blue', command = self.adminlogin, font = fonts, cursor = 'hand2', activebackground = 'Rosy Brown1')
        self.Admin_login_btn.place(x = 635, y = 300)

    def studlogin(self):
        self.Welcomeframe.destroy()
        loginstud = Login(root)

    def adminlogin(self):
        self.Welcomeframe.destroy()
        loginad = Adminlog(root)

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Aditi5*#',

)
cursor = conn.cursor()
cursor.execute('create database if not exists DeskSlot')
cursor.execute('use DeskSlot')
cursor.execute("create table if not exists Admin(empId varchar(15) PRIMARY KEY,  password varchar(15))")
cursor.execute('create table if not exists StudentDetails(StudentId varchar(15) PRIMARY KEY, password varchar(15))')
cursor.execute("CREATE TABLE IF NOT EXISTS D_blockVacancy ( CompId VARCHAR(10) PRIMARY KEY, Allocated BOOLEAN)")
cursor.execute("CREATE TABLE IF NOT EXISTS LibVacancy (CompId VARCHAR(10) PRIMARY KEY, Allocated BOOLEAN)")
cursor.execute('create table if not exists Booking(CompId varchar(10) PRIMARY KEY, StudentId varchar(15))')
conn.commit()

root = Tk()
root.title('DeskSlot')
root.geometry('900x650+350+100')
welcome = Welcome(root)
root.resizable(False, False)
root.mainloop()

