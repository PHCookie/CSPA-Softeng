#LIBRARIES
import numpy as np
import pandas as pd
import math
from types import FrameType
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
#Color Text
import colorama
from colorama import Back, Fore, Style
#Progress Bars
from alive_progress import alive_bar
import time

#-------------------INTRODUCTION--------------------#
colorama.init(autoreset=True)
#A. Header
print(Back.BLACK +"|--------------------WELCOME TO--------------------|")
print(Back.BLACK +f"|-----------------------{Fore.RED}C{Fore.BLUE}S{Fore.CYAN}P{Fore.GREEN}A-{Fore.WHITE}----------------------|")
print(Back.BLACK +"|---------------------ALGORITHM--------------------|")
print(Back.BLACK +"|--------------------------------------------------|")
print(Back.BLACK +f"|{Fore.GREEN}By: CS Warriors{Fore.WHITE}-----------------------------------|")
print("\n")

#B. Loading Program Progress Bar

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

#C. #####-----CATEGORIZING SCORES-----#####
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

#E.########-----LOAN STATUS BAR and BAR CHART-----######## (NOT CHECKED)
# #-----LOAN STATUS BAR-----#
# coffvalue = score_range[score_range['Loan'] == 0]['Loan'].count()
# fpaidvalue = score_range[score_range['Loan'] == 1]['Loan'].count()
# data = {"Counts":[coffvalue, fpaidvalue] }
# statusDF = pd.DataFrame(data, index=["Charged Off", "Fully Paid"])
# statusDF.plot(kind='bar', title="Status of the Loan")
# plt.show()

# #-----BAR CHART-----#
# Category = ['Poor','Fair','Good','Very Good','Exceptional']
# Number_of_Customer = [len(poor), len(fair), len(good), len(verygood),len(exceptional)]

# plt.bar(Category, Number_of_Customer)
# plt.title('Credit Scores Categorization')
# plt.xlabel('Category')
# plt.ylabel('Number of Customer')
# plt.show()

#F.###-----DECISION TREE ALGORITHM---###
#Converting scores from float to integer
# y_cols = score_range["Loan"]
# x_cols = ['Current Loan Amount', 'Years in current job', 'Monthly Debt','Years of Credit History', 'Months since last delinquent','Number of Open Accounts', 'Current Credit Balance', 'Maximum Open Credit']

# X = score_range[x_cols]# Features
# y = y_cols # Target variable

# #Split dataset into training set and test set
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% test

# # Create Decision Tree classifer object
# clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)

# # Train Decision Tree Classifer
# clf = clf.fit(X_train,y_train)

# #Predict the response for test dataset
# y_pred = clf.predict(X_test)

# # Model Accuracy, how often is the classifier correct?
# print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

# #Libraries for graphing
# from sklearn.tree import export_graphviz 
# from six import StringIO
# from IPython.display import Image  
# import pydotplus
# import os
# os.environ["PATH"] += os.pathsep + 'C:\Program Files\Graphviz/bin/'

# dot_data = StringIO()
# export_graphviz(clf, out_file=dot_data,  
#                 filled=True, rounded=True,  
#                 special_characters=True, feature_names = x_cols,class_names=['0','1'])
# graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
# graph.write_png('dtm.png')
# Image(graph.create_png())

#G. Options list to command
def options_list():
    print("\n\nPLEASE CHOOSE AN OPTION!")
    print(f"\n\n{Fore.GREEN}[A] {Fore.WHITE}View Customer Loan Info.")
    print(f"\n{Fore.GREEN}[B] {Fore.WHITE}Show Credit Score.")
    print(f"\n{Fore.GREEN}[C] {Fore.WHITE}Check Credit Score Bar Graph.")
    print(f"\n{Fore.GREEN}[D] {Fore.WHITE}View Decision Tree.")
    print(f"\n{Fore.GREEN}[E] {Fore.WHITE}About the CSPA.")
    print(f"\n{Fore.RED}[F] {Fore.WHITE}Exit.")
#display options list
options_list()

#H Ask for option and validate if valid input or not (Should be at the end)
while True:
    try:
        input1 = input("\nSelect Option:") 

        if input1 == "A":
            print(f"\n{Fore.GREEN}You've Choosen option A")
            break
        elif input1 == "B":
            print(f"\n{Fore.GREEN}You've Choosen option B")
            break
        elif input1 == "C":
            print(f"\n{Fore.GREEN}You've Choosen option C")
            break
        elif input1 == "D":
            print(f"\n{Fore.GREEN}You've Choosen option D")
            break
        elif input1 == "E":
            print(f"\n{Fore.GREEN}You've Choosen option E")
            break
        elif input1 == "F":
            print(f"\n{Fore.GREEN}You've Choosen option F")
            exitinput = input("\nAre you sure you want to exit? (Y/N):") 
            if exitinput == "N":
                print(f"\n{Fore.GREEN}Returning...\n\n")
                options_list()
                continue
            else:
                print(f"\n{Fore.RED}Closing...\n\n")
                break
        #H.1 IF outside the options, then ask again
        else:
            input1 != "A" or "B" or "C" or "D" or "E" or "F"
            print(f"\n{Fore.RED}Input is invalid.{Fore.GREEN} Please only choose on the options provided.")
            continue
    except:
        continue

#-------------------END OF INTRODUCTION-------------#