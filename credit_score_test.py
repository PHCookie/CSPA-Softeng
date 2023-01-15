#LIBRARIES
import numpy as np
import pandas as pd
import math
from types import FrameType
import matplotlib.pyplot as plt
from matplotlib import image as mpimg
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
#Color Text
import colorama
from colorama import Back, Fore, Style
#Progress Bars
from alive_progress import alive_bar
import time
#Delay output
from time import sleep
import csv
#Show png
from PIL import Image
########-----OPTIONS LIST-----########
def options_list():
    print("\n\nPLEASE CHOOSE AN OPTION!")
    print(f"\n\n{Fore.GREEN}[A] {Fore.WHITE}View Customer Info.")
    print(f"\n{Fore.GREEN}[B] {Fore.WHITE}Show Credit Score.")
    print(f"\n{Fore.GREEN}[C] {Fore.WHITE}Check Credit Score Bar Graph.")
    print(f"\n{Fore.GREEN}[D] {Fore.WHITE}About the CSPA.")
    print(f"\n{Fore.RED}[E] {Fore.WHITE}Exit.")
########-----END OF OPTIONS LIST-----########


########-----LOAN  BAR CHART-----######## (NOT CHECKED)
def bar_chart():
    Category = ['Poor','Fair','Good','Very Good','Exceptional']
    Number_of_Customer = [len(poor), len(fair), len(good), len(verygood),len(exceptional)]
    plt.bar(Category, Number_of_Customer)
    plt.title('Credit Scores Categorization')
    plt.xlabel('Category')
    plt.ylabel('Number of Customer')
    plt.show()
#######-----------END OF BAR CHART-----------########

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
            dataset = pd.read_csv('data/testsmalldata/shortcredit_train.csv')
            #To display values in 2 decimal places
            pd.options.display.float_format = '{:.2f}'.format

        if x == 50:
            print(f"{Fore.GREEN}[50%]{Fore.WHITE}Importing..")
            #Remove unwanted values "999999999"
            df = dataset[dataset["Current Loan Amount"] < 99999999 ]
            #- --> not checked yet <---
            # drop all empty credit scores 
            # df = df[df['Credit Score'].notna()]
            #drop all duplicates
            clean_dataset = df.drop_duplicates(subset='Customer_ID')
        
        #ALL Calculations Goes here
        if x == 75:
            print(f"{Fore.GREEN}[75%]{Fore.WHITE}Perform Calculations..")

            #1.PAYMENT HISTORY-------------------------------------------------------|
            # 1( Loan Amount , Credit balance) How many payments made
            loan_amount = clean_dataset["Current Loan Amount"]
            monthly_debt = clean_dataset["Monthly Debt"]
            calc_value = loan_amount / monthly_debt
            # print(calc_value)
            #1.a Years of Credit History 1yr= 1point
            years_ch = clean_dataset["Years of Credit History"]
            #1.b Job years years = 1 point
            job = clean_dataset["Years in current job"]
            #1.c Accounts: Types of accounts considered for credit payment history
            accounts = clean_dataset["Number of Open Accounts"]
            #1.d The amount of time that's passed since delinquencies.
            delinquent = clean_dataset['Months since last delinquent']

            #FINAL SCORE FOR PAYMENT HISTORY
            minor1_score = calc_value + accounts + years_ch + job + delinquent
            final_minor1_score=round(minor1_score, 2)
            # print(final_minor1_score)
            #END OF PAYMENT HISTORY--------------------------------------------------|

            #2. AMOUNTS OWED --------------------------------------------------------|
            value1 = clean_dataset["Current Credit Balance"]
            value2 = clean_dataset["Maximum Open Credit"]
            p_borrow = (value1 / value2) 
            # print(p_borrow)
            # 30% of 850 = 255
            score2 = 255 * (1 - p_borrow) 
            # print(score2)

            #FINAL SCORE FOR ACCOUNTS OWED
            final_minor2_score = score2 
            # print(final_minor2_score)
            #END OF AMOUNTS OWED ----------------------------------------------------|

            #3. LENGTH OF CREDIT HISTORY---------------------------------------------|
            #Ignore delinquent above 84
            deduct_delinquent = clean_dataset[clean_dataset["Months since last delinquent"] <= 84 ] 
            deducted = deduct_delinquent["Months since last delinquent"] * 1.54
            # print(deducted)
            added = deducted.replace(0, 127.5)
            # print(added)
            final_delinquent = deducted + added
            # print(final_delinquent)
            #1.2 Years of credit history converted to points 1yr=2.67
            years = years_ch * 2.67

            #FINAL SCORE FOR LENGTH OF CREDIT HISTORY
            final_minor3_score = years + final_delinquent
            #END OF LENGTH OF CREDIT HISTORY-----------------------------------------|

            #4 NEW CREDIT / CREDIT MIX-----------------------------------------------|
            final_minor4_score = accounts 
            #END OF NEW CREDIT / CREDIT MIX------------------------------------------|

            #5 STARTING SCORE--------------------------------------------------------|
            starting_score = 300

            #Total of all scores
            Credit_score = starting_score + final_minor1_score + final_minor2_score + final_minor3_score + final_minor4_score
            format_Credit_score = round(Credit_score)
            #print (format_Credit_score)

        if x == 99:
            ###-----ADDING NEW COLUMNS WITH CALCULATED VALUES TO CSV-----###
            ###------------SAVING CALCULATED CSV WITH SCORES-------------###
            dataset["Score"] = format_Credit_score
            dataset.to_csv("data/testsmalldata/calculated_shortcredit_train.csv", index=False)
            #to display all output values
            pd.set_option("display.max_rows", None, "display.max_columns", None)

            #NOW LOADING THE NEW DATASET WITH SCORES
            newDF = pd.read_csv('data/testsmalldata/calculated_shortcredit_train.csv', header=0)
            # replace NaN values with 0
            newDF= newDF.fillna(0)

            print(f"{Fore.GREEN}[100%]{Fore.WHITE}Dataset Successfully loaded")
        bar()
print(Fore.GREEN +"\n\n|---------------------SUCCESSFULLY LOADED--------------------|")
#######-----------END OF LOADING PROGRESS BAR--------########

#######-----------SCORE CATEGORIZATION---------------########
#Filter  Credit Scores Greater than 0 and less than 850.(FICO score range)
filter_score = newDF[newDF["Score"] > 0]
score_range = filter_score[(filter_score["Score"] > 0) & (filter_score["Score"] <= 850)] 

#1. Poor Credit Scores
poor_score = filter_score[(filter_score["Score"] > 0) & (filter_score["Score"] < 400)]  
poor = poor_score["Score"]
poor_id = poor_score["Customer_ID"]
# print("POOR CREDIT SCORES:")
# # print(poor)
# print("Number of Customers:",len(poor))

#2. Fair Credit Scores
fair_score = filter_score[(filter_score["Score"] >= 400) & (filter_score["Score"] <= 570)]  
fair = fair_score["Score"]
fair_id = fair_score["Customer_ID"]
# print("FAIR CREDIT SCORES:")
# # # print(fair)
# print("Number of Customers:",len(fair))

#3. Good Credit Scores
good_score = filter_score[(filter_score["Score"] >= 571) & (filter_score["Score"] <= 730)]  
good = good_score["Score"]
good_id = good_score["Customer_ID"]
# print("GOOD CREDIT SCORES:")
# # # print(good)
# print("Number of Customers:",len(good))

#4. VERY GOOD Credit Scores
verygood_score = filter_score[(filter_score["Score"] >= 731) & (filter_score["Score"] <= 830)]  
verygood = verygood_score["Score"]
verygood_id = verygood_score["Customer_ID"]
# print("VERY GOOD CREDIT SCORES:")
# # # print(verygood)
# print("Number of Customers:",len(verygood))

#5. Exceptional Credit Scores
exceptional_score = filter_score[(filter_score["Score"] >= 831) & (filter_score["Score"] <= 850)]  
exceptional = exceptional_score["Score"]
exceptional_id = exceptional_score["Customer_ID"]
# print("EXCEPTIONAL CREDIT SCORES:")
# print(exceptional)
# print("Number of Customers:",len(exceptional))
Total = len(exceptional) + len(verygood) + len(good) + len(fair) + len(poor)
# print("Total", Total)
#######-----------END OF SCORE CATEGORIZATION---------------########



######------ Options list to command------######
options_list()

#1. For viewing customer ID function
def askidshow():
    iddf = pd.read_csv('data/testsmalldata/calculated_shortcredit_train.csv')
    askinputid = input(f"{Fore.GREEN}\nPlease enter Customer ID:")
    print("\n")
    askinputid = int(askinputid)
    if askinputid >=1 and askinputid <=122:
        print(newDF.iloc[askinputid-1])
        print("\n")
    else:
        print("Sorry! That ID does not exist.")

#2. Ask for option and validate if valid input or not.
while True:
    try:
        input1 = input("\nSelect Option:") 

        if input1 == "A":
            ###---Loan Info---###
            print(f"\n{Fore.GREEN}You've Choosen option A")
            print(f"\n{Fore.GREEN}CUSTOMER ID LIST:")
            #1. Display CUSTOMER ID
            with open('data/testsmalldata/calculated_shortcredit_train.csv', newline='') as csvfile:
                newdataset1 = csv.DictReader(csvfile)
                print("Customer ID")
                print("--------------------")
                for row in newdataset1:
                    print(row['Customer_ID'])
            #2. Ask for input in which Customer info to show
            askidshow()
            #3. While loop for viewing other Customer ID
            while True:
                try:
                    askinputA = input(f"\n {Fore.GREEN}Do you want to view other Customer ID? (Y/N):")
                    if askinputA == "Y":
                        askidshow()
                        continue
                    elif askinputA == "N":
                        print(f"\n{Fore.GREEN}Returning...\n\n")
                        break
                    else:
                        askinputA != "Y" or "N" 
                        print(f"\n{Fore.RED}Input is invalid.{Fore.GREEN} Please choose only on the options provided.")
                        continue
                except:
                    break
            #4. Display options after the while loop ended
            sleep(2.60)
            options_list()
            continue
        elif input1 == "B":
            ###---Show CScore---###
            print(f"\n{Fore.GREEN}You've Choosen option B\n\n")
            print(f"\n{Fore.GREEN}CREDIT SCORES LIST:")
            #1.display
            with open('data/testsmalldata/calculated_shortcredit_train.csv', newline='') as csvfile:
                newdataset2 = csv.DictReader(csvfile)
                print("Customer ID | Credit Score")
                print("---------------------------------")
                for row in newdataset2:
                    print(row['Customer_ID'], row['Score'])
            #2.Ask input
            askinputB = input(f"\n {Fore.GREEN}Do you want to choose another option? (Y/N):") 
            if askinputB == "Y":
                print(f"\n{Fore.GREEN}Returning...\n\n")
                sleep(1.70)
                options_list()
                continue
            elif askinputB == "N":
                print(f"\n{Fore.RED}Closing...\n\n")
                break
            else:
                print(f"\n{Fore.RED}Invalid input, terminating program..\n\n")
                break
            
        elif input1 == "C": 
            ###---CScore BAR Graph---###
            print(f"\n{Fore.GREEN}You've Choosen option C")
            print(f"\n{Fore.GREEN}BAR GRAPH:")
            #1. Call bar chart function
            bar_chart()
            print(f"\n{Fore.GREEN}Graph Exited. Returning...\n\n")
            #2. Delay output(to be readable)
            sleep(2.00)
            #3. Call Options list
            options_list()
            continue
        elif input1 == "D": 
            ###---About CSPA---###
            print(f"\n{Fore.GREEN}You've Choosen option D")
            print(f"\n{Fore.WHITE}CSPA by CSWarriors V.1")
            break
        elif input1 == "E":
            print(f"\n{Fore.GREEN}You've Choosen option E")
            exitinputE = input("\nAre you sure you want to exit? (Y/N):") 
            if exitinputE == "N":
                print(f"\n{Fore.GREEN}Returning...\n\n")
                options_list()
                continue
            elif exitinputE == "Y":
                print(f"\n{Fore.RED}Closing...\n\n")
                break
            else:
                print(f"\n{Fore.RED}Invalid input, terminating program..\n\n")
                break
        #H.1 IF outside the options, then ask again
        else:
            input1 != "A" or "B" or "C" or "D" or "E"
            print(f"\n{Fore.RED}Input is invalid.{Fore.GREEN} Please choose only on the options provided.")
            continue
    except:
        continue

