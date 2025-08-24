import mysql.connector
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from datetime import datetime
from tkinter import Tk, Frame, Entry, Label, messagebox, Button, Radiobutton, PhotoImage
from tkcalendar import Calendar

fonts = ('Times New Roman', 20, 'bold')

def convertToTime(time):
    converted_time = datetime.strptime(time, "%H:%M").time()
    return converted_time
    
class Welcome:
    def __init__(self, root):
        self.root = root
        self.Welcomeframe = Frame(self.root, width = 900, height = 650, bg = 'dark turquoise')
        self.Welcomeframe.place(x = 0, y = 0)

        self.im = ImageTk.PhotoImage(Image.open("C:/Users/lavan/Downloads/deskslot_booking/vishnu_logo.png"))
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

class Login:
    def __init__(self, root):
        self.root = root
        self.login_frame = Frame(self.root, width = 900, height = 650, bg = 'dark turquoise')
        self.login_frame.place(x = 0, y = 0)
        #create account
        self.create_button = Button(self.login_frame, text = 'CREATE', bg = 'white', fg = 'steel blue', command = self.create, font = fonts, cursor = 'hand2', activebackground = 'Rosy Brown1', width = 10)
        self.create_button.place(x = 360, y = 420)
        #image 
        self.im = ImageTk.PhotoImage(Image.open("C:/Users/lavan/Downloads/deskslot_booking/svecw.png"))
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
        #label for back_button
        self.submit_btn = Button(self.login_frame, text = 'BACK', bg = 'white', fg = 'steel blue', command = self.back,  cursor = 'hand2', activebackground = 'Rosy Brown1',font = ('Times New Roman', 10, 'bold'), width=5, height=1)
        self.submit_btn.place(x = 20, y = 20)

    def back(self):
        self.login_frame.destroy()
        backnav = Welcome(root)

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
            '''command2 = f"SELECT * FROM Booking WHERE StudentId = '{self.regno}'"
            cursor.execute(command2)
            res = cursor.fetchone()
            if res:
                confirm = confirmation(root, self.regno)
            else:'''
            block = SelectBlock(self.root, self.regno)
        else:
            messagebox.showerror('INVALID CREDENTIALS','CHECK YOUR CREDENTIALS')


    def create(self):
        self.login_frame.destroy()
        createstudent = Create(self.root)

class Create:
    def __init__(self, root):
        self.root = root
        self.root.title('Create a login')
        self.create_frame = Frame(root, width = 900, height = 650, bg = 'dark turquoise')
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
        #label for back_button
        self.submit_btn = Button(self.create_frame, text = 'BACK', bg = 'white', fg = 'steel blue', command = self.back, cursor = 'hand2', activebackground = 'Rosy Brown1',font = ('Times New Roman', 10, 'bold'), width=5, height=1)
        self.submit_btn.place(x = 20, y = 20)

    def back(self):
        self.create_frame.destroy()
        backnav = Login(root)


    def save(self):
        
        self.regno = self.reg_no_entry.get()
        self.password = self.passw_entry.get()
        if self.regno and self.password:
            self.query = f"insert into StudentDetails values('{self.regno}','{self.password}')"
            cursor.execute(self.query)
            conn.commit()
            messagebox.showinfo('SUCCESS', 'Successfully created the account')
            self.create_frame.destroy()
            login = Login(root)
        else:
            messagebox.showerror("Error", "Enter Valid Credentials !")

class Adminlog:

    def __init__(self, root):
        self.root = root
        self.login_frame = Frame(self.root, width = 900, height = 650, bg = 'dark turquoise')
        self.login_frame.place(x = 0, y = 0)
        #image 
        self.im = ImageTk.PhotoImage(Image.open("C:/Users/lavan/Downloads/deskslot_booking/svecw.png"))
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
        #label for back_button
        self.submit_btn = Button(self.login_frame, text = 'BACK', bg = 'white', fg = 'steel blue', command = self.back, cursor = 'hand2', activebackground = 'Rosy Brown1',font = ('Times New Roman', 10, 'bold'), width=5, height=1)
        self.submit_btn.place(x = 20, y = 20)

    def back(self):
        self.login_frame.destroy()
        backnav = Welcome(root)

    def check(self):
        self.adminid = self.adminId_entry.get()
        self.password = self.adminpassw_entry.get()

        command = f"SELECT * FROM Admin WHERE empId = '{self.adminid}' AND password = '{self.password}'"
        cursor.execute(command)
        result = cursor.fetchone()
        if result:
            messagebox.showinfo('WELCOME','WELCOME ' + self.adminid)
            self.login_frame.destroy()
            repair = UpdateRepair(root)
        else:
            messagebox.showerror('INVALID CREDENTIALS','CHECK YOUR CREDENTIALS')

class SelectBlock:
    def __init__(self, root, studId):
        self.root = root
        self.studId = studId
        self.d = None
        self.root.title('DESKSLOT BOOKING')
        self.time_frame = Frame(self.root, width = 900, height = 650, bg = 'aqua')
        self.time_frame.place(x = 0, y = 0)
        #label for selecting date
        self.date_label = Label(self.time_frame, text = 'Date', font = fonts, bg = 'aqua', fg = 'navy', width = 10)
        self.date_label.place(x = 40, y = 100)
        self.date_cal = Calendar(self.time_frame, selectmode = 'day')
        self.date_cal.pack(pady = 20)
        self.date_cal.place(x = 165, y = 100)
        #label for selecting time
        self.starttime_label = Label(self.time_frame, text = 'Start Time', font = fonts, bg = 'aqua', fg = 'navy', width = 10)
        self.starttime_label.place(x = 450, y = 100)
        self.starttime_entry = Entry(self.time_frame, width  = 5, font = fonts, bg = 'white')
        self.starttime_entry.place(x = 620, y = 100)
        #label for choosing duration
        self.endtime_label = Label(self.time_frame, text = 'End Time', font = fonts, bg = 'aqua', fg = 'navy', width = 9)
        self.endtime_label.place(x = 450, y = 150)
        self.endtime_entry = Entry(self.time_frame, width  = 5, font = fonts, bg = 'white', textvariable= 'hours')
        self.endtime_entry.place(x = 620, y = 150)
        #label for button
        self.submit_btn = Button(self.time_frame, text = 'SUBMIT', bg = 'white', fg = 'steel blue', command = self.isValidDate, font = fonts, cursor = 'hand2', activebackground = 'Rosy Brown1')
        self.submit_btn.place(x = 400, y = 350)
        #label for back_button
        self.submit_btn = Button(self.time_frame, text = 'BACK', bg = 'white', fg = 'steel blue', command = self.back, cursor = 'hand2', activebackground = 'Rosy Brown1', font = fonts)
        self.submit_btn.place(x = 250, y = 350)
        #label for requests_button
        self.submit_btn = Button(self.time_frame, text = 'SHOW EXISTING REQUESTS', bg = 'white', fg = 'steel blue', command = self.requests, cursor = 'hand2', activebackground = 'Rosy Brown1', font = ('Times New Roman', 10, 'bold'))
        self.submit_btn.place(x = 700, y = 20)

    def requests(self):
        self.time_frame.destroy()
        requetsnav = liveRequests(root, self.studId)

    def back(self):
        self.time_frame.destroy()
        backnav = Login(root)

    def isValidDate(self):
        if self.d is not None:
            self.time_frame.destroy()
            block = SelectBlock(self.root, self.studId)
        current_date = datetime.now()
        year = current_date.year
        month = current_date.month
        day = current_date.day
        f = 0
        if year == self.date_cal.selection_get().year:
            if month == self.date_cal.selection_get().month:
                if day <= self.date_cal.selection_get().day:
                    f = 1   
            elif month < self.date_cal.selection_get().month:
                f = 1
        elif year < self.date_cal.selection_get().year:
            f = 1
        else:
            f = 0
        if f == 1:
            self.isSunday()
            self.d = self.date_cal.selection_get()
        else:
            messagebox.showerror('Invalid', 'Enter valid Date !!!')

    def isValidTimeOfDigiLib(self, day):
        current_hour = datetime.now().hour
        self.day = day
        current_day = datetime.now().day
        start_time_str = self.starttime_entry.get()
        end_time_str = self.endtime_entry.get()
        
        start_time = convertToTime(start_time_str)
        end_time = convertToTime(end_time_str)
        if current_day == self.day:
            if (start_time.hour < end_time.hour) and (9 <= start_time.hour < 23 and 9 <= end_time.hour < 23) and (start_time.hour > current_hour):
                return True
            else:
                return False
        else:
            if (start_time.hour < end_time.hour) and (9 <= start_time.hour < 23 and 9 <= end_time.hour < 23):
                return True
            else:
                return False
               
    def isValidDTime(self, day):
        current_hour = datetime.now().hour
        self.day = day
        current_day = datetime.now().day
        start_time_str = self.starttime_entry.get()
        end_time_str = self.endtime_entry.get()
            
        start_time = convertToTime(start_time_str)
        end_time = convertToTime(end_time_str)
            

        if current_day == self.day:
            if (start_time.hour < end_time.hour) and (17 <= start_time.hour < 23 and 17 <= end_time.hour < 23) and (start_time.hour > current_hour):
                return True
            else:
                return False
        else:
            if (start_time.hour < end_time.hour) and (17 <= start_time.hour < 23 and 17 <= end_time.hour < 23):
                return True
            else:
                return False
              
    def isSunday(self):
        selected_date = self.date_cal.selection_get()
        try:
            if selected_date.isoweekday() == 7:
                if self.isValidTimeOfDigiLib(selected_date):
                    self.digilib_button = Button(self.time_frame,  text = 'DIGITAL LIBRARY', bg = 'white', fg = 'steel blue', command = self.bookdesks_in_digilib, font = fonts, cursor = 'hand2', activebackground = 'burlywood1', width = 45)
                    self.digilib_button.place(x = 100, y = 450)
                else:
                    messagebox.showerror('ERROR', 'Enter valid Time!!')
            else:
                if self.isValidDTime(selected_date):
                    self.d_212_button = Button(self.time_frame,  text = 'D-211', bg = 'white', fg = 'steel blue', command = self.bookdesks_in_d211, font = fonts, cursor = 'hand2', activebackground = 'burlywood1', width = 45)      
                    self.d_212_button.place(x = 100, y = 450) 
                if self.isValidTimeOfDigiLib(selected_date):
                    self.digilib_button = Button(self.time_frame,  text = 'DIGITAL LIBRARY', bg = 'white', fg = 'steel blue', command = self.bookdesks_in_digilib, font = fonts, cursor = 'hand2', activebackground = 'burlywood1', width = 45)
                    self.digilib_button.place(x = 100, y = 550)
                else:
                    messagebox.showerror('ERROR', 'Enter valid Time!!')
        except Exception:
            messagebox.showerror("Error in Syntax", "Enter Hours in HH:MM in 24 hour format!!!")
    
    def checkBooked(self):
        #Checking whether the student booked on the same day
        query = f"SELECT * FROM Booking WHERE StudentId LIKE '{self.studId}' AND BookedDate LIKE '{self.date_cal.selection_get()}'"
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            messagebox.showerror("Error", "You already booked today!!")
            return True
        else:
            self.time_frame.destroy()
            conn.commit()
            return False
        
    def updateTables(self):
        current_time_str = convertToTime(f"{datetime.now().hour}:00")
        #Deleting the row when end time is matched with current time
        query = f"DELETE FROM LibVacancy WHERE EndTime LIKE '{current_time_str}' AND BookedDate LIKE '{self.date_cal.selection_get()}'"
        cursor.execute(query)
        conn.commit()
        query = f"DELETE FROM Booking WHERE EndTime LIKE '{current_time_str}'  AND BookedDate LIKE '{self.date_cal.selection_get()}'"
        cursor.execute(query)
        conn.commit()
        query = f"DELETE FROM DBlockVacancy WHERE EndTime LIKE '{current_time_str}' AND BookedDate LIKE '{self.date_cal.selection_get()}'"
        cursor.execute(query)
        conn.commit()

    
    def bookdesks_in_digilib(self):
        start_time_str = convertToTime(self.starttime_entry.get())
        end_time_str = convertToTime(self.endtime_entry.get())
        self.updateTables()
        if not self.checkBooked():
            select = SelectDeskLib(root, self.studId, self.date_cal.selection_get(), start_time_str, end_time_str)

    def bookdesks_in_d211(self):
        start_time_str = convertToTime(self.starttime_entry.get())
        end_time_str = convertToTime(self.endtime_entry.get())
        self.updateTables()
        if not self.checkBooked():
            select = SelectDeskDBlock(root, self.studId, self.date_cal.selection_get(), start_time_str, end_time_str)

class liveRequests:
    def __init__(self, root, studId):
        self.root = root
        self.studId = studId
        self.query = f"SELECT * FROM Booking WHERE StudentId = '{self.studId}'"
        cursor.execute(self.query)
        self.result = cursor.fetchall()
        style = ttk.Style()
        #style.configure('self.request_frame' , background='dark turquoise')
        
        self.request_frame = tk.Frame(self.root, width=900, height=650)
        #self.request_frame.config(background = 'dark turquoise')
        self.request_frame.pack(fill=tk.BOTH, expand=True)
        self.root.geometry('900x650+350+100')
        self.root.resizable(False, False)
        style.configure('Treeview', background='dark turquoise', foreground='navy', font=('Times New Roman', 15, 'bold'))
        # Create a Treeview widget to hold the seat grid
        self.tree = ttk.Treeview(self.request_frame, columns=('Date', 'Start Time', 'End Time', 'CT Number'), show='headings')
        self.tree.column('#0', width=0, stretch=tk.NO)
        self.tree.column('Date', width=200, anchor='center')
        self.tree.column('Start Time', width=200, anchor='center')
        self.tree.column('End Time', width=200, anchor='center')
        self.tree.column('CT Number', width=200, anchor='center')
        self.tree.heading('Date', text='Date')
        self.tree.heading('Start Time', text='Start Time')
        self.tree.heading('End Time', text='End Time')
        self.tree.heading('CT Number', text='CT Number')
        self.tree.pack(fill=tk.BOTH, expand=True)
        # Insert data into the Treeview widget
        for row in self.result:
            self.tree.insert('', 'end', values=row)
        #label for back_button
        self.submit_btn = Button(self.request_frame, text = 'BACK', bg = 'white', fg = 'steel blue', command = self.back, cursor = 'hand2', activebackground = 'Rosy Brown1',font = fonts)
        self.submit_btn.place(x = 400, y = 500)
    def back(self):
        self.request_frame.destroy()
        backnav = SelectBlock(root, self.studId)

class SelectDeskDBlock:
    def __init__(self, root, studId, date, start, end) -> None:
        self.root = root
        self.studId = studId
        self.start = start
        self.end = end
        self.date = date
        self.root.title("Desk Slot")
        self.root.geometry('900x650+350+100')
        self.root.resizable(False, False)

        # Create a frame to hold the seat grid
        self.grid_frame = Frame(self.root, width=900, height=650, bg='dark turquoise')
        self.grid_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.selected_seat = None
        self.seat_status = [["available" for i in range(10)] for j in range(7)]
        self.seat = ''
        # Create labels and buttons 
        self.create_seat_map()

        self.add_color_legends()

        login_btn = tk.Button(self.grid_frame, text="Submit", command=self.submit, bg="green", fg="white", width=8)
        login_btn.grid(row=7, column=4, pady=10, sticky="W")

        confirm_btn = tk.Button(self.grid_frame, text = 'Back', command=self.go_back, bg="green", fg="white", width=8)
        confirm_btn.grid(row=7, column=5, pady=10, sticky="W")

    def go_back(self):
        self.grid_frame.destroy()
        after = SelectBlock(self.root, self.studId)

    def submit(self):
        if self.seat == '':
            messagebox.showerror("Error", "Please select atleast one seat !!")
        else:
            result = messagebox.askquestion("Confirm Your Seat", "Do you want to confirm your Seat ?")
            if result == 'yes':
                self.query1 = f"INSERT INTO DBlockVacancy VALUES('{self.date}', '{self.start}', '{self.end}', '{self.seat}')"
                cursor.execute(self.query1)
                conn.commit()
                self.query2= f"INSERT INTO Booking VALUES('{self.date}', '{self.start}', '{self.end}', '{self.seat}', '{self.studId}')"
                cursor.execute(self.query2)
                conn.commit()
                confirm = confirmation(root, self.studId, self.seat)

    def create_seat_map(self):
        seat_count = 0
        for i in range(7):
            for j in range(10):
                seat_label = tk.Label(
                    self.grid_frame, text=f"D-{seat_count+1}", width=8, height=2, relief="solid"
                )
                seat_label.grid(row=i, column=j, padx=5, pady=5)
                self.s = f"D-{seat_count+1}"
                self.query1 = f"SELECT repairD FROM Repair WHERE repairD LIKE '{self.s}'"
                cursor.execute(self.query1)
                result1 = cursor.fetchone()
                if result1:
                    self.seat_status[i][j] = 'repair'
                    self.update_seat_color(i, j, "red")

                self.query2 = f"SELECT CompId FROM DBlockVacancy WHERE CompId LIKE '{self.s}' AND StartTime LIKE '{self.start}' AND BookedDate LIKE '{self.date}'"
                cursor.execute(self.query2)
                result2 = cursor.fetchone()
                if result2:
                    self.seat_status[i][j] = 'booked'
                    self.update_seat_color(i, j, "yellow")
                else:
                    if self.seat_status[i][j] == "available":
                        seat_label.bind("<Button-1>", lambda event, row=i, col=j: self.on_seat_click(row, col))
                seat_count += 1
    
    def on_seat_click(self, row, col):
        current_status = self.seat_status[row][col]
        s = 10 * row + col + 1
        if self.selected_seat is not None:
            # If a seat is already selected, deselect it
            self.seat_status[self.selected_seat[0]][self.selected_seat[1]] = "available"
            self.update_seat_color(*self.selected_seat, "white")

        if current_status == "available":
            # If the clicked seat is available, select it
            self.seat_status[row][col] = "selected"
            self.selected_seat = (row, col)
            s = 10 * row + col + 1
            self.seat = f"D-{s}"
            self.update_seat_color(row, col, "green")
        
        if self.seat_status[row][col] == "available":
            self.seat = ''
        
    def update_seat_color(self, row, col, color):
        widget = self.grid_frame.grid_slaves(row=row, column=col)[0]
        widget.configure(bg=color)

    def add_color_legends(self):
            color_legend_frame = tk.Frame(self.root, width=80, height=150, bg='dark turquoise')
            color_legend_frame.place(relx=0.90, rely=0.20, anchor=tk.SE)

            repair_legend = tk.Label(color_legend_frame, text="Repair", width=15, height=2, bg="red", relief="solid")
            repair_legend.grid(row=0, column=0, padx=5, pady=5)

            booked_legend = tk.Label(color_legend_frame, text="Booked", width=15, height=2, bg="yellow", relief="solid")
            booked_legend.grid(row=0, column=1, padx=5, pady=5)

            available_legend = tk.Label(color_legend_frame, text="Available", width=15, height=2, bg="white", relief="solid")
            available_legend.grid(row=0, column=2,padx=5,pady=5)

class SelectDeskLib:
    def __init__(self, root, studId, date, start, end) -> None:
        self.root = root
        self.studId = studId
        self.start = start
        self.end = end
        self.date = date
        self.root.title("Desk Slot")
        self.root.geometry('900x650+350+100')
        self.root.resizable(False, False)

        # Create a frame to hold the seat grid
        self.grid_frame = Frame(self.root, width=900, height=650, bg='dark turquoise')
        self.grid_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.selected_seat = None
        self.seat_status = [["available" for i in range(10)] for j in range(7)]
        self.seat = ''
        # Create labels and buttons 
        self.create_seat_map()

        self.add_color_legends()

        login_btn = tk.Button(self.grid_frame, text="Submit", command=self.submit, bg="green", fg="white", width=8)
        login_btn.grid(row=7, column=4, pady=10, sticky="W")

        confirm_btn = tk.Button(self.grid_frame, text = 'Back', command=self.go_back, bg="green", fg="white", width=8)
        confirm_btn.grid(row=7, column=5, pady=10, sticky="W")
    
    def go_back(self):
        self.grid_frame.destroy()
        after = SelectBlock(self.root, self.studId)

    def submit(self):
        if self.seat == '':
            messagebox.showerror("Error", "Please select atleast one seat !!")
        else:
            result = messagebox.askquestion("Confirm Your Seat", "Do you want to confirm your Seat ?")
            if result == 'yes':
                self.query1 = f"INSERT INTO LibVacancy VALUES('{self.date}', '{self.start}', '{self.end}', '{self.seat}')"
                cursor.execute(self.query1)
                conn.commit()
                self.query2= f"INSERT INTO Booking VALUES('{self.date}', '{self.start}', '{self.end}', '{self.seat}', '{self.studId}')"
                cursor.execute(self.query2)
                conn.commit()
                confirm = confirmation(root, self.studId, self.seat)

    def create_seat_map(self):
        seat_count = 0
        for i in range(7):
            for j in range(10):
                seat_label = tk.Label(
                    self.grid_frame, text=f"L-{seat_count+1}", width=8, height=2, relief="solid"
                )
                seat_label.grid(row=i, column=j, padx=5, pady=5)
                self.s = f"L-{seat_count+1}"
                self.query1 = f"SELECT repairL FROM Repair WHERE repairL LIKE '{self.s}'"
                cursor.execute(self.query1)
                result1 = cursor.fetchone()
                if result1:
                    self.seat_status[i][j] = 'repair'
                    self.update_seat_color(i, j, "red")

                self.query2 = f"SELECT CompId FROM LibVacancy WHERE CompId LIKE '{self.s}' AND StartTime LIKE '{self.start}' AND BookedDate LIKE '{self.date}'"
                cursor.execute(self.query2)
                result2 = cursor.fetchone()
                if result2:
                    self.seat_status[i][j] = 'booked'
                    self.update_seat_color(i, j, "yellow")
                else:
                    if self.seat_status[i][j] == "available":
                        seat_label.bind("<Button-1>", lambda event, row=i, col=j: self.on_seat_click(row, col))
                seat_count += 1

            
    def on_seat_click(self, row, col):
        current_status = self.seat_status[row][col]
        s = 10 * row + col + 1
        if self.selected_seat is not None:
            # If a seat is already selected, deselect it
            self.seat_status[self.selected_seat[0]][self.selected_seat[1]] = "available"
            self.update_seat_color(*self.selected_seat, "white")

        if current_status == "available":
            # If the clicked seat is available, select it
            self.seat_status[row][col] = "selected"
            self.selected_seat = (row, col)
            s = 10 * row + col + 1
            self.seat = f"L-{s}"
            self.update_seat_color(row, col, "green")
        
        if self.seat_status[row][col] == "available":
            self.seat = ''

            
    def update_seat_color(self, row, col, color):
        widget = self.grid_frame.grid_slaves(row=row, column=col)[0]
        widget.configure(bg=color)
    
    def add_color_legends(self):
            color_legend_frame = tk.Frame(self.root, width=80, height=150, bg='dark turquoise')
            color_legend_frame.place(relx=0.90, rely=0.20, anchor=tk.SE)

            repair_legend = tk.Label(color_legend_frame, text="Repair", width=15, height=2, bg="red", relief="solid")
            repair_legend.grid(row=0, column=0, padx=5, pady=5)

            booked_legend = tk.Label(color_legend_frame, text="Booked", width=15, height=2, bg="yellow", relief="solid")
            booked_legend.grid(row=0, column=1, padx=5, pady=5)

            available_legend = tk.Label(color_legend_frame, text="Available", width=15, height=2, bg="white", relief="solid")
            available_legend.grid(row=0, column=2,padx=5,pady=5)

class confirmation:
    def __init__(self, root, studId, seat):
        self.root = root
        self.studId = studId
        self.seat = seat

        self.query = f"SELECT * FROM Booking WHERE StudentId LIKE '{self.studId}' AND CompId LIKE '{self.seat}'"
        cursor.execute(self.query)
        self.result = cursor.fetchone()
        self.confirm_frame = Frame(self.root, width = 900, height = 650, bg = 'dark turquoise')
        self.confirm_frame.place(x = 0, y = 0)

        self.confirmation_label = Label(self.confirm_frame, text = 'CONFIRMATION !!!', font = fonts, bg = 'dark turquoise', fg = 'navy', width =40)
        self.confirmation_label.place(x = 110, y = 145)

        self.reg_no_label = Label(self.confirm_frame, text = 'Admission Number :', font = fonts, bg = 'dark turquoise', fg = 'navy', width =30)
        self.reg_no_label.place(x = 50, y = 225)
        self.reg_no_label_text = Label(self.confirm_frame, text = self.result[4], font = fonts, bg = 'dark turquoise', fg = 'navy', width =5)
        self.reg_no_label_text.place(x = 450, y = 225)
        
        self.ctnum_label = Label(self.confirm_frame, text = 'CT Number :', font = fonts, bg = 'dark turquoise', fg = 'navy', width = 10)
        self.ctnum_label.place(x = 250, y = 275)
        self.ctnum_label_text = Label(self.confirm_frame, text = self.result[3], font = fonts, bg = 'dark turquoise', fg = 'navy', width = 5)
        self.ctnum_label_text.place(x = 450, y = 275)

        self.date_label = Label(self.confirm_frame, text = 'Date :', font = fonts, bg = 'dark turquoise', fg = 'navy', width = 10)
        self.date_label.place(x = 210, y = 325)
        self.date_label_text = Label(self.confirm_frame, text = self.result[0], font = fonts, bg = 'dark turquoise', fg = 'navy', width = 10)
        self.date_label_text.place(x = 410, y = 325)

        self.time_label = Label(self.confirm_frame, text = 'Time :', font = fonts, bg = 'dark turquoise', fg = 'navy', width = 10)
        self.time_label.place(x = 210, y = 375)
        s = self.result[1] +  '-' + self.result[2]
        self.time_label_text = Label(self.confirm_frame, text = s, font = fonts, bg = 'dark turquoise', fg = 'navy', width = 15)
        self.time_label_text.place(x = 350, y = 375)
        
        self.confirm_btn = Button(self.confirm_frame, text = 'CANCEL', bg = 'white', fg = 'steel blue', font = fonts, cursor = 'hand2', activebackground = 'Rosy Brown1', command = self.cancel)
        self.confirm_btn.place(x = 390, y = 425)

        self.back_btn = Button(self.confirm_frame, text = 'BACK', bg = 'white', fg = 'steel blue', command = self.back,  cursor = 'hand2', activebackground = 'Rosy Brown1',font = ('Times New Roman', 10, 'bold'), width=5, height=1)
        self.back_btn.place(x = 20, y = 20)

    def back(self):
        self.confirm_frame.destroy()
        backnav = SelectBlock(root, self.studId)

    def cancel(self):
        r = messagebox.askquestion("Alert!!", "Confirm Cancellation")
        if r == 'yes':
            self.query = f"DELETE FROM Booking WHERE StudentId LIKE '{self.studId}' AND CompId LIKE '{self.seat}'"
            cursor.execute(self.query)
            self.deleteinlab()
            messagebox.showinfo('Cancelled Successfully', 'Redirecting To Booking')
            self.confirm_frame.destroy()
            after = SelectBlock(self.root, self.studId)

    def deleteinlab(self):
        if self.result[3][0] == 'D':
            self.query = f"DELETE FROM DBlockVacancy WHERE CompId LIKE '{self.result[3]}'"
        else:
            self.query = f"DELETE FROM LibVacancy WHERE CompId LIKE '{self.result[3]}'"

        cursor.execute(self.query)
        conn.commit()
        cursor.close()

class UpdateRepair:
    def __init__(self, root):
        self.root = root
        self.setrepairframe = Frame(self.root, width=900, height=650, bg='dark turquoise')
        self.setrepairframe.place(x=0, y=0)

        self.updatelabel = Label(self.setrepairframe, text='UPDATE REPAIRED COMPUTERS ?', font=fonts, bg='dark turquoise', fg='navy')
        self.updatelabel.place(x=200, y=100)

        self.Yes_btn = Button(self.setrepairframe, text='YES', bg='white', fg='steel blue', command=self.blockselection, font=fonts, cursor='hand2', activebackground='Rosy Brown1')
        self.Yes_btn.place(x=250, y=180)

        self.No_btn = Button(self.setrepairframe, text='NO ', bg='white', fg='steel blue', command = self.back, font=fonts, cursor='hand2', activebackground='Rosy Brown1')
        self.No_btn.place(x=480, y=180)
        # creating booked details button
        self.updatelabel = Button(self.setrepairframe, text='BOOKED DETAILS', font=fonts, bg='white', fg='navy',command=self.display_table, cursor='hand2', activebackground='Rosy Brown1')
        self.updatelabel.place(x=270, y=290)
    
    def back(self):
        self.setrepairframe.destroy()
        backnav = Adminlog(root)

    def blockselection(self):
        self.d_212_button = Button(self.setrepairframe, text='D-211', bg='white', fg='steel blue',command=self.Dblockframe ,font=fonts, cursor='hand2', activebackground='burlywood1', width=45)
        self.d_212_button.place(x=100, y=350)

        self.digilib_button = Button(self.setrepairframe, text='DIGITAL LIBRARY', bg='white', fg='steel blue',command=self.Libframe, font=fonts, cursor='hand2', activebackground='burlywood1', width=45)
        self.digilib_button.place(x=100, y=450)
    
    def display_table(self):
        self.setrepairframe.destroy()
        createstudent = Table(self.root)

    def Dblockframe(self):
        self.setrepairframe.destroy()
        d_blockrep = D_blockRepair(root)

    def Libframe(self):
        self.setrepairframe.destroy()
        Lib_rep = Lib_Repair(root)

#creating table for viewing booked details
class Table:
    def __init__(self, root):
        self.root = root
        self.query = f"SELECT * FROM Booking"
        cursor.execute(self.query)
        self.result = cursor.fetchall()
        style = ttk.Style()
        self.booked_details= tk.Frame(self.root, width=900, height=650,bg="dark turquoise")
        self.root.title('Booked Details')
        self.booked_details.pack(fill=tk.BOTH, expand=True)
        self.root.geometry('900x650+350+100')
        self.root.resizable(False, False)
        style.configure('Treeview', background='dark turquoise', foreground='navy', font=('Times New Roman', 15, 'bold'))
       
        # Create a Treeview widget to hold the booked details
        self.tree = ttk.Treeview(self.booked_details, columns=('BookedDate','StartTime','EndTime','CompId','StudentId'), show='headings')
        self.tree.column('#0', width=0, stretch=tk.NO)
        self.tree.column('BookedDate', width=180, anchor='center')
        self.tree.column('StartTime', width=180, anchor='center')
        self.tree.column('EndTime', width=180, anchor='center')
        self.tree.column('CompId', width=180, anchor='center')
        self.tree.column('StudentId', width=180, anchor='center')
        self.tree.heading('BookedDate', text='BookedDate')
        self.tree.heading('StartTime', text='StartTime')
        self.tree.heading('EndTime', text='EndTime')
        self.tree.heading('CompId', text='CompId')
        self.tree.heading('StudentId', text='StudentId')
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # Insert data into the Treeview widget
        for row in self.result:
            self.tree.insert('', 'end', values=row)
        
        #label for back_button
        self.submit_btn = Button(self.booked_details, text = 'BACK', bg = 'white', fg = 'steel blue', command = self.back, cursor = 'hand2', activebackground = 'Rosy Brown1',font = fonts)
        self.submit_btn.place(x = 400, y = 500)
    def back(self):
        self.booked_details.destroy()
        backnav = UpdateRepair(root)



class D_blockRepair:
    def __init__(self, root):
        self.root = root
        self.root.title("Repair Updation")
        self.root.geometry('900x650+350+100')
        self.root.resizable(False, False)

        # Create a frame to hold the seat grid
        self.grid_frame = Frame(self.root, width=900, height=650, bg='dark turquoise')
        self.grid_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.selected = []
        # Initialize a list to store the seat status (e.g., "available", "booked", "selected")
        self.seat_status = [["available" for i in range(10)] for j in range(7)]

        # Create labels and buttons for the seat map
        self.create_seat_map()

        self.add_color_legends()

    def insert(self):
        self.query1 = f"SELECT repairD FROM Repair"
        cursor.execute(self.query1)
        result = cursor.fetchall()
        r = [j for i in result for j in i]

        if len(self.selected) > 0:
            if result:
                for i in r:
                    if i not in self.selected:
                        self.query = f"delete from repair where repairD LIKE '{i}'"
                        cursor.execute(self.query)
                        conn.commit()
                
            for i in self.selected:
                self.query1 = f"SELECT repairD FROM Repair WHERE repairD LIKE '{i}'"
                cursor.execute(self.query1)
                result1 = cursor.fetchone()
                if result1:
                    pass
                else:
                    self.query = f"insert into repair (repairD) values('{i}')"
                    cursor.execute(self.query)
                    conn.commit()
            messagebox.showinfo("Confirmation", "Repairs Updated Succesfully !!")
            self.grid_frame.destroy()
            backnav = UpdateRepair(root)
                
        else:
            messagebox.showerror('ERROR','Select at least one seat')


    def create_seat_map(self):
        self.seat_count = 0

        for i in range(7):
            for j in range(10):
                seat_label = tk.Label(
                    self.grid_frame, text=f"D-{self.seat_count+1}", width=8, height=2, relief="solid"
                )
                seat_label.grid(row=i, column=j, padx=5, pady=5)
                seat_label.bind("<Button-1>", lambda event, row=i, col=j: self.on_seat_click(row, col))
                self.seat_count += 1

        login_button = tk.Button(self.grid_frame, text="update", command=self.insert, bg="green", fg="white", width=10, height=2)
        login_button.grid(row=7, column=4, pady=10, sticky="W")

        login_button = tk.Button(self.grid_frame, text="back", command=self.go_back, bg="green", fg="white", width=10, height=2)
        login_button.grid(row=7, column=6, pady=10, sticky="E")
    
    def go_back(self):
        self.grid_frame.destroy()
        after = UpdateRepair(self.root)


    def on_seat_click(self, row, col):
        current_status = self.seat_status[row][col]
        seat = 10 * row + col + 1
        if current_status == "available":
            self.seat_status[row][col] = "repair"
            self.selected.append(f"D-{seat}")
            self.update_seat_color(row, col, "red")
        if current_status == "repair":
            self.seat_status[row][col] = "available"
            self.update_seat_color(row, col, "white")
            self.selected.remove(f"D-{seat}")

    def update_seat_color(self, row, col, color):
        widget = self.grid_frame.grid_slaves(row=row, column=col)[0]
        widget.configure(bg=color)

    def add_color_legends(self):
            color_legend_frame = tk.Frame(self.root, width=80, height=150, bg='dark turquoise')
            color_legend_frame.place(relx=0.90, rely=0.20, anchor=tk.SE)

            repair_legend = tk.Label(color_legend_frame, text="Repair", width=15, height=2, bg="red", relief="solid")
            repair_legend.grid(row=0, column=0, padx=5, pady=5)

            booked_legend = tk.Label(color_legend_frame, text="Booked", width=15, height=2, bg="yellow", relief="solid")
            booked_legend.grid(row=0, column=1, padx=5, pady=5)

            available_legend = tk.Label(color_legend_frame, text="Available", width=15, height=2, bg="white", relief="solid")
            available_legend.grid(row=0, column=2,padx=5,pady=5)

class Lib_Repair:
    def __init__(self, root):
        self.root = root
        self.root.title("Repair Updation")
        self.root.geometry('900x650+350+100')
        self.root.resizable(False, False)

        # Create a frame to hold the seat grid
        self.grid_frame = Frame(self.root, width=900, height=650, bg='dark turquoise')
        self.grid_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.selected = []
        # Initialize a list to store the seat status (e.g., "available", "booked", "selected")
        self.seat_status = [["available" for i in range(10)] for j in range(7)]

        # Create labels and buttons for the seat map
        self.create_seat_map()

        self.add_color_legends()

    def insert(self):
        self.query1 = f"SELECT repairL FROM Repair"
        cursor.execute(self.query1)
        result = cursor.fetchall()
        r = [j for i in result for j in i]

        if len(self.selected) > 0:
            if result:
                for i in r:
                    if i not in self.selected:
                        self.query = f"delete from repair where repairL LIKE '{i}'"
                        cursor.execute(self.query)
                        conn.commit()
                
            for i in self.selected:
                self.query1 = f"SELECT repairL FROM Repair WHERE repairL LIKE '{i}'"
                cursor.execute(self.query1)
                result1 = cursor.fetchone()
                if result1:
                    pass
                else:
                    self.query = f"insert into repair (repairL) values('{i}')"
                    cursor.execute(self.query)
                    conn.commit()
            messagebox.showinfo("Confirmation", "Repairs Updated Succesfully !!")
            self.grid_frame.destroy()
            backnav = UpdateRepair(root)
                
        else:
            messagebox.showerror('ERROR','Select at least one seat')


    def create_seat_map(self):
        self.seat_count = 0

        for i in range(7):
            for j in range(10):
                seat_label = tk.Label(
                    self.grid_frame, text=f"L-{self.seat_count+1}", width=8, height=2, relief="solid"
                )
                seat_label.grid(row=i, column=j, padx=5, pady=5)
                seat_label.bind("<Button-1>", lambda event, row=i, col=j: self.on_seat_click(row, col))
                self.seat_count += 1

        login_button = tk.Button(self.grid_frame, text="update", command=self.insert, bg="green", fg="white", width=10, height=2)
        login_button.grid(row=7, column=4, pady=10, sticky="W")

        login_button = tk.Button(self.grid_frame, text="back", command=self.go_back, bg="green", fg="white", width=10, height=2)
        login_button.grid(row=7, column=6, pady=10, sticky="E")
    
    def go_back(self):
        self.grid_frame.destroy()
        after = UpdateRepair(self.root)


    def on_seat_click(self, row, col):
        current_status = self.seat_status[row][col]
        seat = 10 * row + col + 1
        if current_status == "available":
            self.seat_status[row][col] = "repair"
            self.selected.append(f"L-{seat}")
            self.update_seat_color(row, col, "red")
        if current_status == "repair":
            self.seat_status[row][col] = "available"
            self.update_seat_color(row, col, "white")
            self.selected.remove(f"L-{seat}")

    def update_seat_color(self, row, col, color):
        widget = self.grid_frame.grid_slaves(row=row, column=col)[0]
        widget.configure(bg=color)

    def add_color_legends(self):
            color_legend_frame = tk.Frame(self.root, width=80, height=150, bg='dark turquoise')
            color_legend_frame.place(relx=0.90, rely=0.20, anchor=tk.SE)

            repair_legend = tk.Label(color_legend_frame, text="Repair", width=15, height=2, bg="red", relief="solid")
            repair_legend.grid(row=0, column=0, padx=5, pady=5)

            booked_legend = tk.Label(color_legend_frame, text="Booked", width=15, height=2, bg="yellow", relief="solid")
            booked_legend.grid(row=0, column=1, padx=5, pady=5)

            available_legend = tk.Label(color_legend_frame, text="Available", width=15, height=2, bg="white", relief="solid")
            available_legend.grid(row=0, column=2,padx=5,pady=5)

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Rammi@123',
    database = "deskslot",
    auth_plugin = 'mysql_native_password'
)
cursor = conn.cursor()
cursor.execute('create database if not exists DeskSlot')
cursor.execute('use DeskSlot')
cursor.execute("create table if not exists Admin(empId varchar(15) PRIMARY KEY,  password varchar(15))")
cursor.execute('create table if not exists StudentDetails(StudentId varchar(15) PRIMARY KEY, password varchar(15))')
cursor.execute("CREATE TABLE IF NOT EXISTS DblockVacancy(BookedDate date, StartTime varchar(15), EndTime varchar(15), CompId varchar(10))")
cursor.execute("CREATE TABLE IF NOT EXISTS LibVacancy(BookedDate date, StartTime varchar(15), EndTime varchar(15), CompId varchar(10))")
cursor.execute('create table if not exists Booking(BookedDate date,StartTime varchar(15), EndTime varchar(15), CompId varchar(10), StudentId varchar(15))')
cursor.execute('create table if not exists Repair(repairD varchar(5), repairL varchar(5))')
cursor.execute("SELECT * FROM Booking")
data = cursor.fetchall()


if __name__ == "__main__":
    root = Tk()
    root.title('DeskSlot')
    root.geometry('900x650+350+100')
    welcome = Welcome(root)
    root.resizable(False, False)
    #root.iconphoto(True, PhotoImage(file="..//assets//DESKSLOT.png"))
    root.mainloop()
    

