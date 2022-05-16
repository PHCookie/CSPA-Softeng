import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter.constants import *

import Login_support

global status_label

class Login: 
    def registration_popup(self):
        response = messagebox.askyesno("Note!","Proceed to Sign up?")
        if response == 1:
            self.top.destroy()
            import os
            os.system('python Registration.py')
     
    def login_entry(self):
        errors = []
        if self.Entry1.get() == '':
            errors.append('Username field is Empty')
        if self.Entry1_1.get() == '':
            errors.append('Password field is Empty')
        #Condition for Errors or Proceed    
        if errors:
            messagebox.showerror("Error", '\n'.join(errors))
        else:
            self.top.destroy()
            import os
            os.system('python Mainpage.py')
        
    
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("1200x700+0+0")
        top.minsize(120, 1)
        top.maxsize(1200, 700)
        top.resizable(1,  1)
        top.title("CSPA Application Software")
        top.configure(background="#160A26")

        self.top = top
        
        #CSPA TITLE LABEL
        self.Label3 = tk.Label(self.top)
        self.Label3.place(relx=0.15, rely=0.1, height=63, width=1048)
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#160A26")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Segoe UI} -size 25")
        self.Label3.configure(foreground="#ffffff")
        self.Label3.configure(text='''Credit Scoring and Predictive Analytics Application Software''')
        
        #"Signup" label/button
        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.325, rely=0.371, height=44, width=117)
        self.Button1.configure(activebackground="#160A26")
        self.Button1.configure(activeforeground="white")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#160A26")
        self.Button1.configure(borderwidth="0")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Georgia} -size 24")
        self.Button1.configure(foreground="#0080ff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Sign up''')
        self.Button1.configure(command=self.registration_popup)
        
    
        #"Log in |" label
        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.242, rely=0.371, height=43, width=105)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#160A26")
        self.Label1.configure(borderwidth="0")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Georgia} -size 24")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text='''Login |''')

        #Username_entry
        self.Entry1 = tk.Entry(self.top)
        self.Entry1.place(relx=0.242, rely=0.514, height=40, relwidth=0.245)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        #Password_entry
        self.Entry1_1 = tk.Entry(self.top)
        self.Entry1_1.place(relx=0.533, rely=0.514, height=40, relwidth=0.245)
        self.Entry1_1.configure(background="white")
        self.Entry1_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_1.configure(font="TkFixedFont")
        self.Entry1_1.configure(foreground="#000000")
        self.Entry1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_1.configure(highlightcolor="black")
        self.Entry1_1.configure(insertbackground="black")
        self.Entry1_1.configure(selectbackground="blue")
        self.Entry1_1.configure(selectforeground="white")
        self.Entry1_1.configure(show='*')

        #Username Label
        self.Label2 = tk.Label(self.top)
        self.Label2.place(relx=0.242, rely=0.471, height=22, width=75)
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#160A26")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Georgia} -size 11")
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(text='''Username''')

        #Password Label
        self.Label2_1 = tk.Label(self.top)
        self.Label2_1.place(relx=0.533, rely=0.471, height=22, width=75)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(anchor='w')
        self.Label2_1.configure(background="#160A26")
        self.Label2_1.configure(compound='left')
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(font="-family {Georgia} -size 11")
        self.Label2_1.configure(foreground="#ffffff")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text='''Password''')

        #LOGIN BUTTON
        self.Button2 = tk.Button(self.top)
        self.Button2.place(relx=0.467, rely=0.714, height=34, width=97)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#008040")
        self.Button2.configure(compound='left')
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Button2.configure(foreground="#ffffff")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''LOGIN''')
        self.Button2.configure(command=self.login_entry)


def start_up():
    Login_support.main()

if __name__ == '__main__':
    Login_support.main()




