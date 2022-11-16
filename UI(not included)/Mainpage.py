import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from tkinter import *
import Mainpage_support
from PIL import Image, ImageTk

#### IMPORTING Dataset


class MAINPAGE:
    #For switching Frames
    def switch(self, Frame):
        Frame.tkraise()
        
    def __init__(self, top=None):
        
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("1200x700+97+15")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0,  0)
        top.title("CSPA Application Software V1.0")
        top.configure(background="#160A26")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        #--------------------------BUTTON FRAME----------------------------------------------
        self.BUTTONFRAME = tk.Frame(self.top)
        self.BUTTONFRAME.place(relx=0.0, rely=0.0, relheight=1.003
                , relwidth=0.053)
        self.BUTTONFRAME.configure(relief='groove')
        self.BUTTONFRAME.configure(borderwidth="0.5")
        self.BUTTONFRAME.configure(relief="groove")
        self.BUTTONFRAME.configure(background="#670288")
        self.BUTTONFRAME.configure(highlightbackground="#d9d9d9")
        self.BUTTONFRAME.configure(highlightcolor="black")

        #BUTTON 1 - IMAGE BUTTON
        self.first_button=ImageTk.PhotoImage(Image.open('icon/member.png').resize((135,138),Image.ANTIALIAS))
        #BUTTON 1 - MEMBERLIST
        self.Button1 = tk.Button(self.BUTTONFRAME)
        self.Button1.place(relx=0.0, rely=0.014, height=60, width=60)
        self.Button1.configure(image=self.first_button)
        self.Button1.configure(background="#670288")
        self.Button1.configure(borderwidth=0)
        self.Button1.configure(command=lambda:self.switch(self.MEMBERLISTFRAME))
        
        #BUTTON 2 - IMAGE BUTTON
        self.second_button=ImageTk.PhotoImage(Image.open('icon/aboutcsdata.png').resize((70,73),Image.ANTIALIAS))
        #BUTTON 2 - ABOUT CC DTA
        self.Button2 = tk.Button(self.BUTTONFRAME)
        self.Button2.place(relx=0.0, rely=0.142, height=60, width=60)
        self.Button2.configure(background="#670288")
        self.Button2.configure(image=self.second_button)
        self.Button2.configure(borderwidth=0)
        self.Button2.configure(command=lambda:self.switch(self.ABOUTCCDTA))

        #BUTTON 3 - IMAGE BUTTON
        self.third_button=ImageTk.PhotoImage(Image.open('icon/visualization.png').resize((90,60),Image.ANTIALIAS))
        #BUTTON 3 - DATA VISUALIZATION
        self.Button3 = tk.Button(self.BUTTONFRAME)
        self.Button3.place(relx=0.0, rely=0.271, height=60, width=60)
        self.Button3.configure(background="#670288")
        self.Button3.configure(image=self.third_button)
        self.Button3.configure(borderwidth=0)
        self.Button3.configure(command=lambda:self.switch(self.DATAVIS))

        #BUTTON 4 - IMAGE BUTTON
        self.fourth_button=ImageTk.PhotoImage(Image.open('icon/aboutdataset.png').resize((90,60),Image.ANTIALIAS))
        #BUTTON 4 - ABOUT DATASET
        self.Button4 = tk.Button(self.BUTTONFRAME)
        self.Button4.place(relx=0.0, rely=0.41, height=60, width=60)
        self.Button4.configure(background="#670288")
        self.Button4.configure(image=self.fourth_button)
        self.Button4.configure(borderwidth=0)
        self.Button4.configure(command=lambda:self.switch(self.ABOUTDATA))

        #BUTTON 5 - IMAGE BUTTON
        self.fifth_button=ImageTk.PhotoImage(Image.open('icon/decisiontree.png').resize((80,90),Image.ANTIALIAS))
        # BUTTON 5 - DECISION TREE
        self.Button5 = tk.Button(self.BUTTONFRAME)
        self.Button5.place(relx=0.0, rely=0.54, height=60, width=60)
        self.Button5.configure(background="#670288")
        self.Button5.configure(image=self.fifth_button)
        self.Button5.configure(borderwidth=0)
        self.Button5.configure(command=lambda:self.switch(self.DECISION))
        #--------------------------ENF OFBUTTON FRAME----------------------------------------------
       
        #--------------------------ABOUT CC DTA FRAME----------------------------------------------
        self.ABOUTCCDTA = tk.Frame(self.top)
        self.ABOUTCCDTA.place(relx=0.067, rely=0.014, relheight=0.979
                , relwidth=0.923)
        self.ABOUTCCDTA.configure(relief='groove')
        self.ABOUTCCDTA.configure(borderwidth="1")
        self.ABOUTCCDTA.configure(relief="groove")
        self.ABOUTCCDTA.configure(background="#4f4f4f")
        self.ABOUTCCDTA.configure(highlightbackground="#d9d9d9")
        self.ABOUTCCDTA.configure(highlightcolor="black")
        
        self.Label2 = tk.Label(self.ABOUTCCDTA)
        self.Label2.place(relx=0.076, rely=0.041, height=70, width=920)
        self.Label2.configure(anchor='center')
        self.Label2.configure(background="gray")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(font=('Arial', 20, 'bold'))
        self.Label2.configure(text='''About Credit Score and Decision - Tree Algorithm''')
        
        ###--Paragraph Canva for Credit Score Detail----###
        self.canva1= tk.Canvas(self.ABOUTCCDTA)
        self.canva1.place(relx=0.076, rely=0.205, height=500, width=450)
        self.canva1.configure(bg="gray")
        self.canva1.create_text(230, 60, text="What are Credit Scores?", fill="white", font=('Constantia 19 bold'))
        self.canva1.create_text(230, 161, 
        text="     A credit score is a numerical expression based on a level\nanalysis of a person's credit files, to represent the creditwort-\nhiness of anindividual."
        , fill="white", font=('Arial 12 '))
        self.canva1.create_text(230, 261, 
        text="FICO Credit Scoring System is used in this Application Soft-\nware. The base FICO Scores range from 300 - 850, and FIC-\nO defines the 'good'range from 670 to 739. FICO's industry-\nspeci-fic creditscores have a different range --250 to 900. Ho-\nwever, the middle categories have the same groupings and a\n'good' industry-specific FICO Scoreis still 670 to 739."
        , fill="white", font=('Arial 12 '))
        ###-----------END of Canva CS Detail-----------###
        
        ###--Paragraph Canva for Decision Tree Model----###
        self.canva2= tk.Canvas(self.ABOUTCCDTA)
        self.canva2.place(relx=0.50, rely=0.205, height=500, width=450)
        self.canva2.configure(bg="gray")
        self.canva2.create_text(227, 60, text="What is Decision Tree Algorithm?", fill="white", font=('Constantia 19 bold'))
        self.canva2.create_text(230, 161, 
        text="     Decision Tree is to create a training model that can use to\npredict the class or value of the target variable by learning si-\nmple decision rules inferred from prior data (data set)."
        , fill="white", font=('Arial 12 '))
        self.canva2.create_text(225, 251, 
        text="A significant advantage of a decision tree is that it forces the\nconsideration of all possible outcomes of a decision and tra-\nces each each path to a conclusion. It creates a comprehen-\nsive analysis of the consequences along each branch and id-\nentifies decision nodes that needs further analysis."
        , fill="white", font=('Arial 12 '))
         ###-----------END of Canva Decision Tree Model-----------###
        #--------------------------END OF CC Data Frame----------------------------------------------
        
        #----------------------------DATA VISUALIZATION FRAME----------------------------------
        self.DATAVIS = tk.Frame(self.top)
        self.DATAVIS.place(relx=0.067, rely=0.014, relheight=0.979
                , relwidth=0.923)
        self.DATAVIS.configure(relief='groove')
        self.DATAVIS.configure(borderwidth="1")
        self.DATAVIS.configure(relief="groove")
        self.DATAVIS.configure(background="#4f4f4f")
        self.DATAVIS.configure(highlightbackground="#d9d9d9")
        self.DATAVIS.configure(highlightcolor="black")

        self.Label3 = tk.Label(self.DATAVIS)
        self.Label3.place(relx=0.076, rely=0.041, height=70, width=920)
        self.Label3.configure(anchor='center')
        self.Label3.configure(background="gray")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#ffffff")
        self.Label3.configure(font=('Arial', 20, 'bold'))
        self.Label3.configure(text='''Data Visualization and Modelling''')
        #--------------------------END OF DATA VISUALIZATION FRAME-------------------------------
        
        #--------------------------ABOUT DATA FRAME----------------------------------------------
        self.ABOUTDATA = tk.Frame(self.top)
        self.ABOUTDATA.place(relx=0.067, rely=0.014, relheight=0.979
                , relwidth=0.923)
        self.ABOUTDATA.configure(relief='groove')
        self.ABOUTDATA.configure(borderwidth="1")
        self.ABOUTDATA.configure(relief="groove")
        self.ABOUTDATA.configure(background="#4f4f4f")
        self.ABOUTDATA.configure(highlightbackground="#d9d9d9")
        self.ABOUTDATA.configure(highlightcolor="black")
        
        self.Label4 = tk.Label(self.ABOUTDATA)
        self.Label4.place(relx=0.076, rely=0.041, height=70, width=920)
        self.Label4.configure(anchor='center')
        self.Label4.configure(background="gray")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#ffffff")
        self.Label4.configure(font=('Arial', 20, 'bold'))
        self.Label4.configure(text='''About Dataset''')
        
        ###--Paragraph Canva for Dataset Information----###
        self.canva3= tk.Canvas(self.ABOUTDATA)
        self.canva3.place(relx=0.076, rely=0.205, height=500, width=350)
        self.canva3.configure(bg="gray")
        ###--END OF Canva Dataset Information----###
        
        ###--Paragraph Canva for Dataset Content----###
        self.canva4= tk.Canvas(self.ABOUTDATA)
        self.canva4.place(relx=0.411, rely=0.205, height=500, width=550)
        self.canva4.configure(bg="gray")
        ###Displaying   
         ###--END OF Canva Dataset Content----###
        #--------------------------END OF ABOUT DATA FRAME----------------------------------------------
        
        #--------------------------DECISION-TREE FRAME----------------------------------------------
        self.DECISION = tk.Frame(self.top)
        self.DECISION.place(relx=0.067, rely=0.014, relheight=0.979
                , relwidth=0.923)
        self.DECISION.configure(relief='groove')
        self.DECISION.configure(borderwidth="1")
        self.DECISION.configure(relief="groove")
        self.DECISION.configure(background="#4f4f4f")
        self.DECISION.configure(highlightbackground="#d9d9d9")
        self.DECISION.configure(highlightcolor="black")
        
        self.Label5 = tk.Label(self.DECISION)
        self.Label5.place(relx=0.076, rely=0.041, height=70, width=920)
        self.Label5.configure(anchor='center')
        self.Label5.configure(background="gray")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#ffffff")
        self.Label5.configure(font=('Arial', 20, 'bold'))
        self.Label5.configure(text='''Decision - Tree Model''')
        #--------------------------END OF DECISION-TREE FRAME----------------------------------------------
         
        #--------------------------MEMBER LIST FRAME----------------------------------------------
        self.MEMBERLISTFRAME = tk.Frame(self.top)
        self.MEMBERLISTFRAME.place(relx=0.067, rely=0.014, relheight=0.979
                , relwidth=0.923)
        self.MEMBERLISTFRAME.configure(relief='groove')
        self.MEMBERLISTFRAME.configure(borderwidth="1")
        self.MEMBERLISTFRAME.configure(relief="groove")
        self.MEMBERLISTFRAME.configure(background="#4f4f4f")
        self.MEMBERLISTFRAME.configure(highlightbackground="#d9d9d9")
        self.MEMBERLISTFRAME.configure(highlightcolor="black")
        
        self.Label1 = tk.Label(self.MEMBERLISTFRAME)
        self.Label1.place(relx=0.076, rely=0.041, height=70, width=920)
        self.Label1.configure(anchor='center')
        self.Label1.configure(background="gray")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(font=('Arial', 23, 'bold'))
        self.Label1.configure(text='''Member's Credit Score and Loan Status''')
        
        self.Label1_1 = tk.Label(self.MEMBERLISTFRAME)
        self.Label1_1.place(relx=0.076, rely=0.041, height=70, width=920)
        self.Label1_1.configure(anchor='center')
        self.Label1_1.configure(background="gray")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(foreground="#ffffff")
        self.Label1_1.configure(font=('Arial', 23, 'bold'))
        self.Label1_1.configure(text='''Member's Credit Score and Loan Status''')
        #--------------------------END OF MEMBER LIST FRAME----------------------------------

def start_up():
    Mainpage_support.main()

if __name__ == '__main__':
    Mainpage_support.main()




