DeskSlot Booking System

DeskSlot Booking is a lab desk booking system developed using Python, Tkinter, and SQL. It was designed to help students book lab systems during non-working hours and simplify system management for administrators. The project ensures efficient usage of lab systems and provides a clear, user-friendly interface with a seat visualization map.

Features:
Student Module
Students log in using their credentials.
Date and time are selected before booking.
Lab availability is dynamic (for example, on Sundays only the Digital Library is available).
A seat map shows availability using colors:
White → Available
Yellow → Booked
Red → Under Repair
Green → Currently Selected
After confirmation, the booking is stored in the database.
Students can also view their upcoming or past bookings.

Admin Module:
Admin login is separate from student login.
Admin can monitor all student bookings.
Admin can mark systems as under repair or restore them to available after repair.
Admin can also manage lab availability on specific days.

System Architecture
Frontend: Tkinter (Python GUI framework)
Backend: Python (logic and validations)
Database: SQL (stores user data, bookings, and system status)

Installation and Setup:

Clone the repository:
git clone https://github.com/your-username/DeskSlotBooking.git
cd DeskSlotBooking

Install dependencies:
Python 3.x is required.

Install libraries:
pip install tk sqlite3


Setup database:
The project uses SQLite or MySQL.
Run the SQL script in the project to create the required tables.

Run the project:
python main.py

Database Design
Users Table: stores student and admin credentials with fields like user_id, username, password, and role.
Bookings Table: stores booking records with fields like booking_id, student_id, lab_id, system_no, date, and time_slot.
Labs Table: stores lab details with fields like lab_id, lab_name, and available_days.
Systems Table: tracks system status with fields like system_id, lab_id, and status (available, booked, repair).
