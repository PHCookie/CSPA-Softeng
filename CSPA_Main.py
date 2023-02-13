#LIBRARIES
import pandas as pd
import os
#Color Text
import colorama
from colorama import Back, Fore
#Progress Bars
from alive_progress import alive_bar
import time
#Delay output
from time import sleep
import csv
#importing made-modules
import Calculations.scoring as cal 
import Calculations.classification as classi
import Displaytool.tools as tool
from csv import DictWriter

#######-----------HEADER---------------########
colorama.init(autoreset=True)
print(Back.BLACK +"|--------------------WELCOME TO--------------------|")
print(Back.BLACK +f"|-----------------------{Fore.RED}C{Fore.BLUE}S{Fore.CYAN}P{Fore.GREEN}A-{Fore.WHITE}----------------------|")
print(Back.BLACK +"|---------------------ALGORITHM--------------------|")
print(Back.BLACK +"|--------------------------------------------------|")
print(Back.BLACK +f"|{Fore.GREEN}By: CS Warriors{Fore.WHITE}-----------------------------------|")
print("\n")
#######-----------END OF HEADER---------------########

#######-----------LOADING PROGRESS BAR--------########
#A. LOADING BAR
print("Loading Program :\n")
with alive_bar(100) as bar:
    for i in range(100):
        time.sleep(.050)
        if i == 30:
            print(f"{Fore.GREEN}[30%]{Fore.WHITE}Checking Libraries..")
        if i == 50:
            print(f"{Fore.GREEN}[50%]{Fore.WHITE}Checking Resources..")
        if i == 75:
            print(f"{Fore.GREEN}[75%]{Fore.WHITE}Optimizing..")
        if i == 99:
            print(f"{Fore.GREEN}[100%]{Fore.WHITE}Program Successfully Loaded")
        bar()

#B. IMPORTING DATASET LOADING BAR
print("\nImporting Dataset :\n")
with alive_bar(100) as bar:
    for x in range(100):
        time.sleep(.090)
        if x == 25:
            print(f"{Fore.GREEN}[25%]{Fore.WHITE}Checking Dataset..")
            # Checking
            dataset = pd.read_csv('data/Origin COOP.csv')
            #To display values in 2 decimal places
            pd.options.display.float_format = '{:.2f}'.format

        if x == 50:
            print(f"{Fore.GREEN}[50%]{Fore.WHITE}Importing..")
            
            #Cleaning
            df = dataset[dataset["Current Loan Amount"] < 999999 ]
            clean_dataset = df.drop_duplicates(subset='Customer ID')

        if x == 75:
            print(f"{Fore.GREEN}[75%]{Fore.WHITE}Perform Calculations..")

            #get calculation
            scored = cal.getscore(dataset)
            #get classification
            final = classi.byRandomForest(scored)


        if x == 99:
            ###-----ADDING NEW COLUMNS WITH CALCULATED VALUES TO CSV-----###
            ###------------SAVING CALCULATED CSV WITH SCORES-------------###
 
            #to display all output values
            pd.set_option("display.max_rows", None, "display.max_columns", None)

            # replace NaN values with 0
            final= final.fillna(0)

            final.to_csv('data/Dataset_Scored.csv', index=False)

            print(f"{Fore.GREEN}[100%]{Fore.WHITE}Dataset Successfully loaded")
        bar()

print(Fore.GREEN +"\n\n|---------------------SUCCESSFULLY LOADED--------------------|")
#######-----------END OF LOADING PROGRESS BAR--------########

######------ Options list to command------######
tool.options_list()
Exit = False
#2. Ask for option and validate if valid input or not.
while Exit == False:
    try:
        input1 = input("\nSelect Option:") 

        if input1.capitalize() == "A":
            ###---Loan Info---###
            print(f"\n{Fore.GREEN}You've Choosen option A")
            print(f"\n{Fore.GREEN}CUSTOMER ID LIST:")

            #1. Display CUSTOMER ID
            with open('data/Dataset_Scored.csv', newline='') as csvfile:
                newdataset1 = csv.DictReader(csvfile)
                print("Customer ID")
                print("--------------------")
                for row in newdataset1:
                    print(row['Customer ID'])
                tool.askidshow()

            #4. Display options after the while loop ended
            sleep(2.60)
            tool.options_list()
            continue
        elif input1.capitalize() == "B":
            ###---Show CScore---###
            print(f"\n{Fore.GREEN}You've Choosen option B\n\n")
            print(f"\n{Fore.GREEN}CREDIT SCORES LIST:")
            #1.display
            with open('data/Dataset_Scored.csv', newline='') as csvfile:
                newdataset2 = csv.DictReader(csvfile)
                print("Customer ID | Credit Score | Class Score")
                print("---------------------------------")
                for row in newdataset2:
                    print(row['Customer ID'],"   ", row['Score'],"   ",row['Class Score'])
            
        elif input1.capitalize() == "C": 
            ###---CScore BAR Graph---###
            print(f"\n{Fore.GREEN}You've Choosen option C")
            print(f"\n{Fore.GREEN}BAR GRAPH:")
            Number_of_Customer = classi.obtain(pd.read_csv('data/Dataset_Scored.csv'))
            tool.bar_chart(Number_of_Customer)
            print(f"\n{Fore.RED}Graph Exited. Returning...\n\n")
            sleep(2.00)

            tool.options_list()
            continue

        elif input1.capitalize() == "E": 
            ###---About CSPA---###
            print(f"\n{Fore.GREEN}You've Choosen option E")
            print(f"\n{Fore.WHITE}CSPA by CSWarriors V.1")
            osCommandString = "notepad.exe About_CSPA.txt"
            os.system(osCommandString)

        elif input1.capitalize() == "D":
            ###---New Data---###
            print(f"\n{Fore.GREEN}You've Choosen option D")

            field_names = [['Customer ID', 'Current Loan Amount', 'Current Credit Balance',
                'Monthly Debt', 'Years in current job','Years of Credit History',
                'Number of Open Accounts', 'Months since last delinquent', 'Maximum Open Credit'],]

            with open('data/Dataset_Scored.csv','a', newline='') as csvfile:    

                # Gather new user data
                dict = tool.newuser(dataset.iloc[-1,0])
               
                # Pass the dictionary as an argument to the Writerow()
                dictwriter_object = DictWriter(csvfile, fieldnames=field_names[0])
                dictwriter_object.writerow(dict)

            dataset = pd.read_csv('data/Dataset_Scored.csv')
            #get calculations
            scored = cal.getscore(dataset)

            #get classification
            final = classi.byCSPA(scored)
            final.to_csv('data/Dataset_Scored.csv', index=False)
        
        elif input1.capitalize() == "F":

            print(f"\n{Fore.GREEN}You've Choosen option F")
            exitinputE = input("\nAre you sure you want to exit? (Y/N):") 
            if exitinputE.capitalize() == "N":
                print(f"\n{Fore.GREEN}Returning...\n\n")
                tool.options_list()
                continue
            elif exitinputE.capitalize() == "Y":
                print(f"\n{Fore.RED}Closing...\n\n")
                Exit == True
                break
            else:
                print(f"\n{Fore.RED}Invalid input, returning... \n\n")
        #H.1 IF outside the options, then ask again
        else:
            input1 != "A" or "B" or "C" or "D" or "E" or "F"
            print(f"\n{Fore.RED}Input is invalid.{Fore.GREEN} Please choose only on the options provided.")
            continue
    except:
        continue
