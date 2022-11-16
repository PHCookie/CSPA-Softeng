import sys
import tkinter as tk
import tkinter.ttk as ttk
import csv
import pandas as pd
import regex as re
from tkinter import messagebox
from tkinter.constants import *

import Registration_support

class Register:

    #borrowed from https://stackoverflow.com/questions/16709638/
    #checking-the-strength-of-a-password-how-to-check-conditions
    def password_check(self):

        password = self.Entry1_4.get()

        # calculating the length
        length_error = len(password) < 8

        # searching for digits
        digit_error = re.search(r"\d", password) is None

        # searching for symbols
        symbol_error = re.search(r"\W", password) is None

        # overall result
        password_ok = not ( length_error or digit_error or symbol_error )

        return password_ok

    
    def entry_check(self):
        
        errors = []

        #Check if Empty
        if self.Entry1.get() == '':
            errors.append('Name field is Empty')
        if self.Entry1_1.get() == '':
            errors.append('Address field is Empty')
        if self.Entry1_2.get() == '':
            errors.append('Position at Work field is Empty')
        if self.Entry1_3.get() == '':
            errors.append('Username field is Empty')
        if self.Entry1_4.get() == '':
            errors.append('Password field is Empty')
        if ( self.Entry1_4.get() != self.Entry_rePass.get() ):
            errors.append('Password does not match')


        #check if Taken
        df = pd.read_csv("User_Information.csv")
        
        name_list = df['Name'].str.split(',', expand=True)
        for i in range (    len(name_list)  ):
            if name_list[0].iloc[i] == self.Entry1.get():
                errors.append('Name is already taken')
        email_list = df['Username'].str.split(',', expand=True)
        for i in range (    len(email_list)  ):
            if email_list[0].iloc[i].lower() == self.Entry1_3.get().lower():
                errors.append('Username is already taken')
        
            
        #Errors or Proceed P1
        if errors:
            messagebox.showerror("Error", '\n'.join(errors))
            return

        #check if appropriate username or password
        if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", self.Entry1_3.get()):
            errors.append('Invalid Email. Please use format of: cspa@example.com\n')                    
        if self.password_check() == False :
            errors.append('Password is weak! Please make sure to do the following: \
        8 characters length or more\n1 digit or more\n1 symbol or more')

        #Errors or Proceed P2
        if errors:
            messagebox.showerror("Error", '\n'.join(errors))
            return            

        #proceeding to accepting register
        response = messagebox.askyesno("Proceed","Information Finalized?") #MAKE LESS FORMAL lmao
        if response == 0:
            return
        else:
            self.entry_registration()  



    #placing information onto User_Information - registration
    def entry_registration (self):      
        name = self.Entry1.get()
        addr = self.Entry1_1.get()
        user = self.Entry1_3.get()
        passw = self.Entry1_4.get()
        pos = self.Entry1_2.get()
           
        with open("User_Information.csv", 'r', newline='') as inputFile, \
        open("User_Information.csv", 'a', newline='') as writerFile:        

            #checks current row index (as ID)
            line_count = -1
            for row in inputFile:
                line_count += 1
            writer = csv.writer (writerFile,delimiter=",")        
            writer.writerow([line_count,name,user,passw,addr, pos])
       
        #proceeding to login
        response = messagebox.showinfo("Success!","You have successfully Registered.")
        self.top.destroy()
        import os
        os.system('python Login.py')
               

    def login_popup(self):
        response = messagebox.askyesno("Warning!","Return to Login Screen?")
        if response == 1:
            self.top.destroy()
            import os
            os.system('python Login.py')
 


    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("1000x600+169+112")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("CSPA Application Software - Registration")
        top.configure(background="#160A26")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.61, rely=0.4, height=54, width=227)
        self.Button1.configure(activebackground="#00ff40")
        self.Button1.configure(activeforeground="#ffffff")
        self.Button1.configure(background="#22b7ff")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Arial} -size 17 -weight bold")
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(relief="groove")
        self.Button1.configure(text='''Create Account''')
        self.Button1.configure(command=self.entry_check)

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.59, rely=0.533, height=21, width=204)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#160A26")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Georgia} -size 13")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Already have an account?''')

        self.Button2 = tk.Button(self.top)
        self.Button2.place(relx=0.79, rely=0.528, height=24, width=67)
        self.Button2.configure(activebackground="#160A26")
        self.Button2.configure(activeforeground="white")
        self.Button2.configure(activeforeground="#ffffff")
        self.Button2.configure(background="#160A26")
        self.Button2.configure(borderwidth="0")
        self.Button2.configure(compound='left')
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font="-family {Georgia} -size 14 -weight bold")
        self.Button2.configure(foreground="#0080ff")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Log in''')
        self.Button2.configure(command=self.login_popup)

        #Name Entry
        self.Entry1 = tk.Entry(self.top)
        self.Entry1.place(relx=0.25, rely=0.333, height=30, relwidth=0.234)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="blue")
        self.Entry1.configure(selectforeground="white")

        #Address Entry
        self.Entry1_1 = tk.Entry(self.top)
        self.Entry1_1.place(relx=0.25, rely=0.433, height=30, relwidth=0.234)
        self.Entry1_1.configure(background="white")
        self.Entry1_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_1.configure(font="TkFixedFont")
        self.Entry1_1.configure(foreground="#000000")
        self.Entry1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_1.configure(highlightcolor="black")
        self.Entry1_1.configure(insertbackground="black")
        self.Entry1_1.configure(selectbackground="blue")
        self.Entry1_1.configure(selectforeground="white")

        #PositionAtWork Entry
        self.Entry1_2 = tk.Entry(self.top)
        self.Entry1_2.place(relx=0.25, rely=0.533, height=30, relwidth=0.234)
        self.Entry1_2.configure(background="white")
        self.Entry1_2.configure(disabledforeground="#a3a3a3")
        self.Entry1_2.configure(font="TkFixedFont")
        self.Entry1_2.configure(foreground="#000000")
        self.Entry1_2.configure(highlightbackground="#d9d9d9")
        self.Entry1_2.configure(highlightcolor="black")
        self.Entry1_2.configure(insertbackground="black")
        self.Entry1_2.configure(selectbackground="blue")
        self.Entry1_2.configure(selectforeground="white")

        #Username Entry
        self.Entry1_3 = tk.Entry(self.top)
        self.Entry1_3.place(relx=0.25, rely=0.633, height=30, relwidth=0.234)
        self.Entry1_3.configure(background="white")
        self.Entry1_3.configure(disabledforeground="#a3a3a3")
        self.Entry1_3.configure(font="TkFixedFont")
        self.Entry1_3.configure(foreground="#000000")
        self.Entry1_3.configure(highlightbackground="#d9d9d9")
        self.Entry1_3.configure(highlightcolor="black")
        self.Entry1_3.configure(insertbackground="black")
        self.Entry1_3.configure(selectbackground="blue")
        self.Entry1_3.configure(selectforeground="white")

        #Password Entry
        self.Entry1_4 = tk.Entry(self.top)
        self.Entry1_4.place(relx=0.25, rely=0.733, height=30, relwidth=0.234)
        self.Entry1_4.configure(background="white")
        self.Entry1_4.configure(disabledforeground="#a3a3a3")
        self.Entry1_4.configure(font="TkFixedFont")
        self.Entry1_4.configure(foreground="#000000")
        self.Entry1_4.configure(highlightbackground="#d9d9d9")
        self.Entry1_4.configure(highlightcolor="black")
        self.Entry1_4.configure(insertbackground="black")
        self.Entry1_4.configure(selectbackground="blue")
        self.Entry1_4.configure(selectforeground="white")

        #Re-Enter Password Entry
        self.Entry_rePass = tk.Entry(self.top)
        self.Entry_rePass.place(relx=0.25, rely=0.833, height=30, relwidth=0.234)
        self.Entry_rePass.configure(background="white")
        self.Entry_rePass.configure(disabledforeground="#a3a3a3")
        self.Entry_rePass.configure(font="TkFixedFont")
        self.Entry_rePass.configure(foreground="#000000")
        self.Entry_rePass.configure(highlightbackground="#d9d9d9")
        self.Entry_rePass.configure(highlightcolor="black")
        self.Entry_rePass.configure(insertbackground="black")
        self.Entry_rePass.configure(selectbackground="blue")
        self.Entry_rePass.configure(selectforeground="white")

        self.Label2 = tk.Label(self.top)
        self.Label2.place(relx=0.284, rely=0.217, height=41, width=184)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#160A26")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Arial} -size 20 -weight bold")
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Hello there !''')

        self.Label3 = tk.Label(self.top)
        self.Label3.place(relx=0.145, rely=0.333, height=21, width=44)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#160A26")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Label3.configure(foreground="#ffffff")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Name''')

        self.Label3_1 = tk.Label(self.top)
        self.Label3_1.place(relx=0.13, rely=0.433, height=21, width=54)
        self.Label3_1.configure(activebackground="#f9f9f9")
        self.Label3_1.configure(activeforeground="black")
        self.Label3_1.configure(anchor='w')
        self.Label3_1.configure(background="#160A26")
        self.Label3_1.configure(compound='left')
        self.Label3_1.configure(disabledforeground="#a3a3a3")
        self.Label3_1.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Label3_1.configure(foreground="#ffffff")
        self.Label3_1.configure(highlightbackground="#d9d9d9")
        self.Label3_1.configure(highlightcolor="black")
        self.Label3_1.configure(text='''Address''')

        self.Label3_2 = tk.Label(self.top)
        self.Label3_2.place(relx=0.077, rely=0.533, height=21, width=114)
        self.Label3_2.configure(activebackground="#f9f9f9")
        self.Label3_2.configure(activeforeground="black")
        self.Label3_2.configure(anchor='w')
        self.Label3_2.configure(background="#160A26")
        self.Label3_2.configure(compound='left')
        self.Label3_2.configure(disabledforeground="#a3a3a3")
        self.Label3_2.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Label3_2.configure(foreground="#ffffff")
        self.Label3_2.configure(highlightbackground="#d9d9d9")
        self.Label3_2.configure(highlightcolor="black")
        self.Label3_2.configure(text='''Position at Work''')

        self.Label3_3 = tk.Label(self.top)
        self.Label3_3.place(relx=0.079, rely=0.633, height=21, width=110)
        self.Label3_3.configure(activebackground="#f9f9f9")
        self.Label3_3.configure(activeforeground="black")
        self.Label3_3.configure(anchor='w')
        self.Label3_3.configure(background="#160A26")
        self.Label3_3.configure(compound='left')
        self.Label3_3.configure(disabledforeground="#a3a3a3")
        self.Label3_3.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Label3_3.configure(foreground="#ffffff")
        self.Label3_3.configure(highlightbackground="#d9d9d9")
        self.Label3_3.configure(highlightcolor="black")
        self.Label3_3.configure(text='''Email(Username)''') #makes more sense? name already exists

        self.Label3_4 = tk.Label(self.top)
        self.Label3_4.place(relx=0.12, rely=0.733, height=21, width=64)
        self.Label3_4.configure(activebackground="#f9f9f9")
        self.Label3_4.configure(activeforeground="black")
        self.Label3_4.configure(anchor='w')
        self.Label3_4.configure(background="#160A26")
        self.Label3_4.configure(compound='left')
        self.Label3_4.configure(disabledforeground="#a3a3a3")
        self.Label3_4.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Label3_4.configure(foreground="#ffffff")
        self.Label3_4.configure(highlightbackground="#d9d9d9")
        self.Label3_4.configure(highlightcolor="black")
        self.Label3_4.configure(text='''Password''')

        self.RePass = tk.Label(self.top)
        self.RePass.place(relx=0.063, rely=0.833, height=21, width=130)
        self.RePass.configure(activebackground="#f9f9f9")
        self.RePass.configure(activeforeground="black")
        self.RePass.configure(anchor='w')
        self.RePass.configure(background="#160A26")
        self.RePass.configure(compound='left')
        self.RePass.configure(disabledforeground="#a3a3a3")
        self.RePass.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.RePass.configure(foreground="#ffffff")
        self.RePass.configure(highlightbackground="#d9d9d9")
        self.RePass.configure(highlightcolor="black")
        self.RePass.configure(text='''Re-enter Password''')

def start_up():
    Registration_support.main()

if __name__ == '__main__':
    Registration_support.main()







