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

def progress_bar(progress, total, color = colorama.Fore.GREEN):
    percent = 100 * (progress/ float(total))
    bar = '▰' * int(percent) + '-' * (100 - int(percent))
    print(color + f"\r|{bar}| {percent:.3f}%", end="\r")

print("Loading Program :")
numbers = [x * 5 for x in range(1000, 2000)]
results = []

progress_bar(0, len(numbers))
for i, x in enumerate(numbers):
    results.append(math.factorial(x))
    progress_bar(i+1,len(numbers))
print("\nLoading Program : DONE\n")

#C. Importing Dataset Progress Bar
print("Importing Data:")

numbers2 = [x * 5 for x in range(2000, 3000)]
results2 = []

progress_bar(0, len(numbers2))
for j, y in enumerate(numbers2):
    results2.append(math.factorial(y))
    progress_bar(j+1,len(numbers2))
print("\nImporting Data: DONE\n")

#D. Options to command
print(Fore.GREEN +"|---------------------SUCCESSFULLY LOADED--------------------|")
print("\n\nPLEASE CHOOSE AN OPTION!")
print(f"\n\n{Fore.GREEN}[A] {Fore.WHITE}View Customer Loan Info.")
print(f"\n{Fore.GREEN}[B] {Fore.WHITE} Show Credit Score.")
print(f"\n{Fore.GREEN}[C] {Fore.WHITE} Check Credit Score Bar Graph.")
print(f"\n{Fore.GREEN}[D] {Fore.WHITE} View Decision Tree.")
print(f"\n{Fore.GREEN}[E] {Fore.WHITE} About the CSPA.")
print(f"\n{Fore.RED}[F] {Fore.WHITE} Exit.")

#-------------------END OF INTRODUCTION-------------#

###-----CLEANING/ORGANIZING DATASET-----###
# Columns: Customer ID,Current Loan Amount,Annual Income,Years in current job,Monthly Debt,Years of Credit History,Months since last delinquent,Number of Open Accounts,Number of Credit Problems,Current Credit Balance,Maximum Open Credit.
dataset = pd.read_csv('data/testsmalldata/shortcredit_train.csv')
#Remove unwanted values "999999999"
df = dataset[dataset["Current Loan Amount"] < 99999999 ]

#- --> not checked yet <---
# drop all empty credit scores 
# df = df[df['Credit Score'].notna()]

#drop all duplicates
clean_dataset = df.drop_duplicates(subset='Customer ID')
# clean_dataset.dropna(thresh = clean_dataset.shape[0]*0.2, how = 'all', axis = 1, inplace = True)

#to display all values
# pd.set_option("display.max_rows", None, "display.max_columns", None)  #btw is this supposed to be for pd or "clean_dataset"?
# print(clean_dataset)

####----GENERATING SCORES----####
#To display values in 2 decimal places
pd.options.display.float_format = '{:.2f}'.format

#1.PAYMENT HISTORY
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

#2. AMOUNTS OWED
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

#3. LENGTH OF CREDIT HISTORY
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

#4 NEW CREDIT / CREDIT MIX
final_minor4_score = accounts 

#5 STARTING SCORE
starting_score = 300

#Total of all scores
Credit_score = starting_score + final_minor1_score + final_minor2_score + final_minor3_score + final_minor4_score
format_Credit_score = round(Credit_score)
# print (format_Credit_score)
# exceptional_score = (format_Credit_score <= 739) & (format_Credit_score >= 670)
# print(exceptional_score)  

##-----ADDING NEW COLUMNS WITH CALCULATED VALUES TO CSV-----###
# dataset["Score"] = format_Credit_score
# dataset.to_csv("data/new_credit_train.csv", index=False)


# ####-----REPLACE NaN VALUES WITH 0-----####
# dataset= dataset.fillna(0)

# ####-----FILTER CREDIT SCORES BETWEEN 1 - 850-----#####
# filter_score = dataset[dataset["Score"] > 0]
# score_range = filter_score[(filter_score["Score"] > 0) & (filter_score["Score"] <= 850)] 


# # #####-----CATEGORIZING SCORES-----#####
# #1. Poor Credit Scores
# poor_score = filter_score[(filter_score["Score"] > 0) & (filter_score["Score"] < 400)]  
# poor = poor_score["Score"]
# poor_id = poor_score["Customer ID"]
# print("POOR CREDIT SCORES:")
# # # print(poor)
# print("Number of Customers:",len(poor))

# #2. Fair Credit Scores
# fair_score = filter_score[(filter_score["Score"] >= 400) & (filter_score["Score"] <= 570)]  
# fair = fair_score["Score"]
# fair_id = fair_score["Customer ID"]
# print("FAIR CREDIT SCORES:")
# # print(fair)
# print("Number of Customers:",len(fair))

# #3. Good Credit Scores
# good_score = filter_score[(filter_score["Score"] >= 571) & (filter_score["Score"] <= 730)]  
# good = good_score["Score"]
# good_id = good_score["Customer ID"]
# print("GOOD CREDIT SCORES:")
# #print(good)
# print("Number of Customers:",len(good))

# #4. VERY GOOD Credit Scores
# verygood_score = filter_score[(filter_score["Score"] >= 731) & (filter_score["Score"] <= 830)]  
# verygood = verygood_score["Score"]
# verygood_id = verygood_score["Customer ID"]
# print("VERY GOOD CREDIT SCORES:")
# # print(verygood)
# print("Number of Customers:",len(verygood))

# #5. Exceptional Credit Scores
# exceptional_score = filter_score[(filter_score["Score"] >= 831) & (filter_score["Score"] <= 850)]  
# exceptional = exceptional_score["Score"]
# exceptional_id = exceptional_score["Customer ID"]
# print("EXCEPTIONAL CREDIT SCORES:")
# # print(exceptional)
# print("Number of Customers:",len(exceptional))
# Total = len(exceptional) + len(verygood) + len(good) + len(fair) + len(poor)
# print("Total", Total)

# #-----BAR CHART-----#####
# Category = ['Poor','Fair','Good','Very Good','Exceptional']
# Number_of_Customer = [len(poor),len(fair),len(good),len(verygood),len(exceptional)]

# plt.bar(Category, Number_of_Customer)
# plt.title('Credit Scores Categorization')
# plt.xlabel('Category')
# plt.ylabel('Number of Customer')
# plt.show()

# #-----LOAN STATUS BAR-----##
#Counting 1 and O
# coffvalue = score_range[score_range['Loan'] == 0]['Loan'].count()
# fpaidvalue = score_range[score_range['Loan'] == 1]['Loan'].count()
# data = {"Counts":[coffvalue, fpaidvalue] }
# statusDF = pd.DataFrame(data, index=["Charged Off", "Fully Paid"])
# statusDF.plot(kind='bar', title="Status of the Loan")
# plt.show()

#-----DECISION TREE ALGORITHM---###
#Assigning columns for x and y
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
