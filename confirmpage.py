import mysql.connector
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from datetime import datetime
from tkinter import Tk, Frame, Entry, Label, messagebox, Button, Radiobutton
from tkcalendar import Calendar

fonts = ('Times New Roman', 20, 'bold')

def convertToTime(time):
        converted_time = datetime.strptime(time, "%H:%M").time()
        return converted_time

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
            self.query = f"insert into Booking (StudentId, CompId) values('{self.regno}', 'PENDING')"
            cursor.execute(self.query)
            conn.commit()
            messagebox.showinfo('WELCOME','WELCOME ' + self.regno)
            self.login_frame.destroy()
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

    def save(self):
        
        self.regno = self.reg_no_entry.get()
        self.password = self.passw_entry.get()

        self.query = f"insert into StudentDetails values('{self.regno}','{self.password}')"
        cursor.execute(self.query)
        conn.commit()
        messagebox.showinfo('SUCCESS', 'Successfully created the account')
        self.create_frame.destroy()
        login = Login(root)

class SelectBlock:
    def __init__(self, root, studId):
        self.root = root
        self.studId = studId
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

    def isValidDate(self):
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
        else:
            messagebox.showerror('Invalid', 'Enter valid Date !!!')

    def isValidTimeOfDigiLib(self, day):
        current_hour = datetime.now().hour
        self.day = day
        current_day = datetime.now().day
        start_time_str = self.starttime_entry.get()
        end_time_str = self.endtime_entry.get()
        try:
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
        except ValueError:
            return False
        
    def isValidDTime(self, day):
        current_hour = datetime.now().hour
        self.day = day
        current_day = datetime.now().day
        start_time_str = self.starttime_entry.get()
        end_time_str = self.endtime_entry.get()
        try:
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
        except ValueError:
            return False
    
            
    def isSunday(self):
        selected_date = self.date_cal.selection_get()
        if selected_date.isoweekday() == 7:
            if self.isValidTimeOfDigiLib(selected_date):
                self.digilib_button = Button(self.time_frame,  text = 'DIGITAL LIBRARY', bg = 'white', fg = 'steel blue', command = self.bookdesks_in_digilib, font = fonts, cursor = 'hand2', activebackground = 'burlywood1', width = 45)
                self.digilib_button.place(x = 100, y = 450)
            else:
                messagebox.showerror('ERROR', 'Enter valid Time')
        else:
            if self.isValidDTime(selected_date):
                self.d_212_button = Button(self.time_frame,  text = 'D-211', bg = 'white', fg = 'steel blue', command = self.bookdesks_in_d211, font = fonts, cursor = 'hand2', activebackground = 'burlywood1', width = 45)      
                self.d_212_button.place(x = 100, y = 450) 
            if self.isValidTimeOfDigiLib(selected_date):
                self.digilib_button = Button(self.time_frame,  text = 'DIGITAL LIBRARY', bg = 'white', fg = 'steel blue', command = self.bookdesks_in_digilib, font = fonts, cursor = 'hand2', activebackground = 'burlywood1', width = 45)
                self.digilib_button.place(x = 100, y = 550)
            else:
                messagebox.showerror('ERROR', 'Enter valid Time')
    
    def bookdesks_in_digilib(self):
        start_time_str = convertToTime(self.starttime_entry.get())
        end_time_str = convertToTime(self.endtime_entry.get())
        self.query1 = f"INSERT INTO LibVacancy (BookedDate, StartTime, EndTime) VALUES('{self.date_cal.selection_get()}', '{start_time_str}', '{end_time_str}')"
        cursor.execute(self.query1)
        conn.commit()
        self.query2= f"UPDATE Booking SET BookedDate = '{self.date_cal.selection_get()}', StartTime = '{start_time_str}', EndTime ='{end_time_str}' WHERE StudentId = '{self.studId}'"
        cursor.execute(self.query2)
        conn.commit()
        self.time_frame.destroy()
        select = SelectDeskLib(root, self.studId)

    def bookdesks_in_d211(self):
        start_time_str = convertToTime(self.starttime_entry.get())
        end_time_str = convertToTime(self.endtime_entry.get())
        self.query1 = f"INSERT INTO DblockVacancy (BookedDate, StartTime, EndTime) VALUES('{self.date_cal.selection_get()}', '{start_time_str}', '{end_time_str}')"
        cursor.execute(self.query1)
        conn.commit()
        self.query2= f"UPDATE Booking SET BookedDate = '{self.date_cal.selection_get()}', StartTime = '{start_time_str}', EndTime ='{end_time_str}' WHERE StudentId = '{self.studId}'"
        cursor.execute(self.query2)
        conn.commit()
        self.time_frame.destroy()
        select = SelectDeskDBlock(root, self.studId)
class SelectDeskDBlock:
    def __init__(self, root, studId) -> None:
        self.root = root
        self.studId = studId
        self.root.title("Desk Slot")
        self.selected_seat = None
        self.seat_booked = False
        # Create labels and buttons 
        self.create_seat_map(studId)

    def create_seat_map(self,studId):
        seat_count = 0
        for i in range(7):
            for j in range(10):
                seat_label = tk.Label(
                    self.root, text=f"D-{seat_count+1}", width=8, height=2, relief="solid"
                )
                seat_label.grid(row=i, column=j, padx=5, pady=5)
                self.s = f"D-{seat_count+1}"
                self.query1 = f"SELECT repairD FROM Repair WHERE repairD LIKE '{self.s}'"
                cursor.execute(self.query1)
                result1 = cursor.fetchone()
                if result1:
                    self.update_seat_color(i, j, "red")
                self.query1 = f"SELECT CompId FROM DBlockVacancy WHERE CompId LIKE '{self.s}'"
                cursor.execute(self.query1)
                result2 = cursor.fetchone()
                if result2:
                    self.update_seat_color(i, j, "yellow")
                else:
                    seat_label.bind("<Button-1>", lambda event, row=i, col=j: self.on_seat_click(row, col,studId))
                seat_count += 1

            
    def on_seat_click(self, row, col,studId):

        if self.selected_seat is not None:
            # If a seat is already selected, deselect it
            self.update_seat_color(*self.selected_seat, "white")

        self.selected_seat = (row, col)
        self.update_seat_color(row, col, "green",studId)

    def update_seat_color(self, row, col, color):
        widget = self.root.grid_slaves(row=row, column=col)[0]
        widget.configure(bg=color)
            
    def update_seat_color(self, row, col, color,studId):
        widget = self.root.grid_slaves(row=row, column=col)[0]
        widget.configure(bg=color)
        Dclick = confirmation(root, studId)

class SelectDeskLib:
    def __init__(self, root, studId) -> None:
        self.root = root
        self.studId = studId
        self.root.title("Desk Slot")
        self.selected_seat = None
        self.seat_booked = False
        # Create labels and buttons 
        self.create_seat_map(studId)

    def create_seat_map(self,studId):
        seat_count = 0
        for i in range(7):
            for j in range(10):
                seat_label = tk.Label(
                    self.root, text=f"L-{seat_count+1}", width=8, height=2, relief="solid"
                )
                seat_label.grid(row=i, column=j, padx=5, pady=5)
                self.s = f"L-{seat_count+1}"
                self.query1 = f"SELECT repairD FROM Repair WHERE repairD LIKE '{self.s}'"
                cursor.execute(self.query1)
                result1 = cursor.fetchone()
                if result1:
                    self.update_seat_color(i, j, "red")
                self.query1 = f"SELECT CompId FROM DBlockVacancy WHERE CompId LIKE '{self.s}'"
                cursor.execute(self.query1)
                result2 = cursor.fetchone()
                if result2:
                    self.update_seat_color(i, j, "yellow")
                else:
                    seat_label.bind("<Button-1>", lambda event, row=i, col=j: self.on_seat_click(row, col,studId))
                seat_count += 1

            
    def on_seat_click(self, row, col, studId):

        if self.selected_seat is not None:
            # If a seat is already selected, deselect it
            self.update_seat_color(*self.selected_seat, "white")

        self.selected_seat = (row, col)
        self.update_seat_color(row, col, "green",studId)

    def update_seat_color(self, row, col, color):
        widget = self.root.grid_slaves(row=row, column=col)[0]
        widget.configure(bg=color)
            
    def update_seat_color(self, row, col, color, studId):
        widget = self.root.grid_slaves(row=row, column=col)[0]
        widget.configure(bg=color)
        click = confirmation(root, studId)

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
            repair = UpdateRepair(root)
        else:
            messagebox.showerror('INVALID CREDENTIALS','CHECK YOUR CREDENTIALS')

class UpdateRepair:
    def __init__(self, root):
        self.root = root
        self.setrepairframe = Frame(self.root, width=900, height=650, bg='dark turquoise')
        self.setrepairframe.place(x=0, y=0)

        self.updatelabel = Label(self.setrepairframe, text='UPDATE REPAIRED COMPUTERS ?', font=fonts, bg='dark turquoise', fg='navy')
        self.updatelabel.place(x=200, y=100)

        self.Yes_btn = Button(self.setrepairframe, text='YES', bg='white', fg='steel blue', command=self.blockselection, font=fonts, cursor='hand2', activebackground='Rosy Brown1')
        self.Yes_btn.place(x=250, y=180)

        self.No_btn = Button(self.setrepairframe, text='NO ', bg='white', fg='steel blue', font=fonts, cursor='hand2', activebackground='Rosy Brown1')
        self.No_btn.place(x=480, y=180)

    def blockselection(self):
        self.d_212_button = Button(self.setrepairframe, text='D-211', bg='white', fg='steel blue',command=self.Dblockframe ,font=fonts, cursor='hand2', activebackground='burlywood1', width=45)
        self.d_212_button.place(x=100, y=350)

        self.digilib_button = Button(self.setrepairframe, text='DIGITAL LIBRARY', bg='white', fg='steel blue',command=self.Libframe, font=fonts, cursor='hand2', activebackground='burlywood1', width=45)
        self.digilib_button.place(x=100, y=450)
    
    def Dblockframe(self):
        self.setrepairframe.destroy()
        d_blockrep = D_blockRepair(root)

    def Libframe(self):
        self.setrepairframe.destroy()
        Lib_rep = Lib_Repair(root)


class D_blockRepair:
    def __init__(self, root):
        self.root = root
        self.root.title("Computer Seat Booking")
        
        # Initialize a list to store the seat status (e.g., "available", "booked", "selected")
        self.seat_status = [["available" for _ in range(10)] for _ in range(7)]

        # Create labels and buttons for the seat map
        self.create_seat_map()

    def create_seat_map(self):
        seat_count = 0
        for i in range(7):
            for j in range(10):
                seat_label = tk.Label(
                    self.root, text=f"D-{seat_count + 1}", width=8, height=2, relief="solid"
                )
                seat_label.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")  # Use sticky option
                seat_label.bind("<Button-1>", lambda event, row=i, col=j: self.on_seat_click(row, col))
                seat_count += 1

        # Column configure to make columns expand equally
        for j in range(10):
            self.root.grid_columnconfigure(j, weight=1)

        # Row configure to make rows expand equally
        for i in range(7):
            self.root.grid_rowconfigure(i, weight=1)

        # Center the grid in the frame
        self.root.grid_rowconfigure(7, weight=1)
        self.root.grid_columnconfigure(10, weight=1)


    def on_seat_click(self, row, col):
        current_status = self.seat_status[row][col]

        if current_status == "available":
            self.seat_status[row][col] = "repair"
            self.update_seat_color(row, col, "red")
        elif current_status == "selected":
            self.seat_status[row][col] = "available"
            self.update_seat_color(row, col, "white")

    def update_seat_color(self, row, col, color):
        widget = self.root.grid_slaves(row=row, column=col)[0]
        widget.configure(bg=color)

class Lib_Repair:
    def __init__(self, root):
        self.root = root
        self.root.title("Computer Seat Booking")
        
        # Initialize a list to store the seat status (e.g., "available", "booked", "selected")
        self.seat_status = [["available" for _ in range(10)] for _ in range(7)]

        # Create labels and buttons for the seat map
        self.create_seat_map()

    def create_seat_map(self):
        seat_count = 0
        for i in range(7):
            for j in range(10):
                seat_label = tk.Label(
                    self.root, text=f"Lib-{seat_count + 1}", width=8, height=2, relief="solid"
                )
                seat_label.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")  # Use sticky option
                seat_label.bind("<Button-1>", lambda event, row=i, col=j: self.on_seat_click(row, col))
                seat_count += 1

        # Column configure to make columns expand equally
        for j in range(10):
            self.root.grid_columnconfigure(j, weight=1)

        # Row configure to make rows expand equally
        for i in range(7):
            self.root.grid_rowconfigure(i, weight=1)

        # Center the grid in the frame
        self.root.grid_rowconfigure(7, weight=1)
        self.root.grid_columnconfigure(10, weight=1)


    def on_seat_click(self, row, col):
        current_status = self.seat_status[row][col]

        if current_status == "available":
            self.seat_status[row][col] = "repair"
            self.update_seat_color(row, col, "red")
        elif current_status == "selected":
            self.seat_status[row][col] = "available"
            self.update_seat_color(row, col, "white")

    def update_seat_color(self, row, col, color):
        widget = self.root.grid_slaves(row=row, column=col)[0]
        widget.configure(bg=color)

class confirmation:
    def __init__(self, root, studId):
        self.root = root
        self.confirm_frame = Frame(self.root, width = 900, height = 650, bg = 'dark turquoise')
        self.confirm_frame.place(x = 0, y = 0)

        #label for confirmation
        self.confirmation_label = Label(self.confirm_frame, text = 'CONFIRMATION !!!', font = fonts, bg = 'dark turquoise', fg = 'navy', width =40)
        self.confirmation_label.place(x = 110, y = 145)

        #label for reg.no
        self.reg_no_label = Label(self.confirm_frame, text = 'Admission Number :', font = fonts, bg = 'dark turquoise', fg = 'navy', width =40)
        self.reg_no_label.place(x = 50, y = 225)
        self.reg_no_label_text = Label(self.confirm_frame, text = '501', font = fonts, bg = 'dark turquoise', fg = 'navy', width =5)
        self.reg_no_label_text.place(x = 550, y = 225)
        
        #label for CT.no
        self.ctnum_label = Label(self.confirm_frame, text = 'CT Number :', font = fonts, bg = 'dark turquoise', fg = 'navy', width = 10)
        self.ctnum_label.place(x = 250, y = 275)
        self.ctnum_label_text = Label(self.confirm_frame, text = 'D-1', font = fonts, bg = 'dark turquoise', fg = 'navy', width = 5)
        self.ctnum_label_text.place(x = 450, y = 275)

        #label for CT.no
        self.date_label = Label(self.confirm_frame, text = 'Date :', font = fonts, bg = 'dark turquoise', fg = 'navy', width = 10)
        self.date_label.place(x = 210, y = 325)
        self.date_label_text = Label(self.confirm_frame, text = '01-03-2024', font = fonts, bg = 'dark turquoise', fg = 'navy', width = 10)
        self.date_label_text.place(x = 410, y = 325)

        #label for CT.no
        self.time_label = Label(self.confirm_frame, text = 'Time :', font = fonts, bg = 'dark turquoise', fg = 'navy', width = 10)
        self.time_label.place(x = 210, y = 375)
        self.time_label_text = Label(self.confirm_frame, text = '18:00 - 19:00', font = fonts, bg = 'dark turquoise', fg = 'navy', width = 10)
        self.time_label_text.place(x = 410, y = 375)
        
        #label for button
        self.confirm_btn = Button(self.confirm_frame, text = 'CANCEL', bg = 'white', fg = 'steel blue', font = fonts, cursor = 'hand2', activebackground = 'Rosy Brown1', command = lambda: self.save(studId))
        self.confirm_btn.place(x = 390, y = 425)

    def save(self, studId):
        result = messagebox.askquestion('CONFIRM CANCELLATION', 'Do you want to cancel your slot?')
        if(result=='yes'):
            messagebox.showinfo('Cancelled Successfully')
            self.confirm_frame.destroy()
            after = SelectBlock(self.root, studId)


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
    password = '90006@Bhagi',
    auth_plugin='mysql_native_password'
)
cursor = conn.cursor()
cursor.execute('create database if not exists DeskSlot')
cursor.execute('use DeskSlot')
cursor.execute("create table if not exists Admin(empId varchar(15) PRIMARY KEY,  password varchar(15))")
cursor.execute('create table if not exists StudentDetails(StudentId varchar(15) PRIMARY KEY, password varchar(15))')
cursor.execute("CREATE TABLE IF NOT EXISTS DblockVacancy(BookedDate date, StartTime varchar(15), EndTime varchar(15), CompId varchar(10))")
cursor.execute("CREATE TABLE IF NOT EXISTS LibVacancy(BookedDate date, StartTime varchar(15), EndTime varchar(15), CompId varchar(10), StudentId varchar(15))")
cursor.execute('create table if not exists Booking(BookedDate date,StartTime varchar(15), EndTime varchar(15), CompId varchar(10), StudentId varchar(15))')
cursor.execute('create table if not exists repair(repairL varchar(5), repairD varchar(5))')

root = Tk()
root.title('DeskSlot')
root.geometry('900x650+350+100')
welcome = Welcome(root)
root.resizable(False, False)
root.mainloop()

