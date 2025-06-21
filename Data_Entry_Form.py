import tkinter
from tkinter import ttk
from tkinter import messagebox
import tkinter.messagebox


def enter_data():

    accepted = accept_var.get()

    if accepted == "Accepted":


        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        if firstname and lastname:

           title = title_Combobox.get()
           age = age_spinbox.get()
           nationality = nationality_combobox.get()
    
           registered_status = reg_status_var.get()
           numcourses = numcourses_spinbox.get()
           numsemester = numsemester_spinbox.get()



           print("First name:",firstname, "Last name:",lastname)
           print("Title:",title, "Age:",age,"Nationality:",nationality)
           print("#Courses:",numcourses,"# Semesters: ",numsemester)
           print("Registered Status",registered_status)
           print("---------------------------------------------")
        else:
            tkinter.messagebox.showwarning(title="Erorr",message="First name and last name is required.")
    else:
       tkinter.messagebox.showwarning(title="Error",message="You have not accepted the terms")

window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

user__info__frame = tkinter.LabelFrame(frame, text = "User Information")
user__info__frame.grid(row = 0, column = 0 , padx = 20, pady = 10)

first_name_label = tkinter.Label(user__info__frame, text = "First Name")
first_name_label.grid(row = 0, column = 0)
last_name_label = tkinter.Label(user__info__frame, text = "Last Name")
last_name_label.grid(row = 0, column = 1)

first_name_entry = tkinter.Entry(user__info__frame)
last_name_entry = tkinter.Entry(user__info__frame)
first_name_entry.grid(row=1,column=0)
last_name_entry.grid(row = 1, column = 1)

title_label = tkinter.Label(user__info__frame, text = "Title")
title_Combobox = ttk.Combobox(user__info__frame,values=["", "Mr." , "Ms.", "Dr."])
title_label.grid(row = 0, column = 2)
title_Combobox.grid(row = 1, column = 2)

age_label = tkinter.Label(user__info__frame, text = "Age")
age_spinbox = tkinter.Spinbox(user__info__frame, from_= 18, to = 110)
age_label.grid(row=2,column=0)
age_spinbox.grid(row = 3, column = 0)

nationality_label = tkinter.Label(user__info__frame, text = "Nationality")
nationality_combobox = ttk.Combobox(user__info__frame,values=["India", "Africa","Asia","Europe","North America", "Oceania", "South America"])
nationality_label.grid(row = 2, column = 1)
nationality_combobox.grid(row = 3 , column = 1)

for widget in user__info__frame.winfo_children():
    widget.grid_configure(padx = 10, pady = 5)

courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row = 1, column = 0, sticky = "news", padx = 20, pady = 10)

registered_label = tkinter.Label(courses_frame, text="Registration Status")

reg_status_var = tkinter.StringVar()
registered_check = tkinter.Checkbutton(courses_frame,text="Currently Registered", variable = reg_status_var, onvalue="Registered",offvalue="Not registered")

registered_label.grid(row=0,column=0)
registered_check.grid(row=1,column=0)

numcourses_label = tkinter.Label(courses_frame,text="# Completed Courses")
numcourses_spinbox = tkinter.Spinbox(courses_frame,from_=0, to='infinity')
numcourses_label.grid(row = 0, column = 1)
numcourses_spinbox.grid(row = 1, column = 1)

numsemester_label = tkinter.Label(courses_frame,text="# Semesters")
numsemester_spinbox = tkinter.Spinbox(courses_frame,from_=0, to='infinity')
numsemester_label.grid(row = 0, column = 2)
numsemester_spinbox.grid(row = 1, column = 2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx = 10, pady = 5)


term_frame = tkinter.LabelFrame(frame, text = "Term & Conditions")
term_frame.grid(row = 2, column = 0, sticky = "news", padx = 20, pady = 10)

accept_var = tkinter.StringVar(value="Not Accepted")
term_check = tkinter.Checkbutton(term_frame, text = "I accept the terms and conditions.",variable=accept_var,onvalue="Accepted", offvalue="Not Accepted")
term_check.grid(row = 0, column = 0)

button = tkinter.Button(frame, text = "Enter data", command = enter_data )
button.grid(row = 3, column = 0, sticky = "news", padx = 20, pady = 10)




window.mainloop()