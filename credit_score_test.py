#LIBRARIES
import numpy as np
import pandas as pd
import math
from types import FrameType
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation

###-----CLEANING/ORGANIZING DATASET-----###
# Columns: Loan ID,Customer ID,Loan Status,Current Loan Amount,Term,Credit Score,Annual Income,Years in current job,Home Ownership,Purpose,Monthly Debt,Years of Credit History,Months since last delinquent,Number of Open Accounts,Number of Credit Problems,Current Credit Balance,Maximum Open Credit,Bankruptcies,Tax Liens
dataset = pd.read_csv('data/credit_train.csv')
#Remove unwanted values "999999999"
clean_dataset = dataset[dataset["Current Loan Amount"] < 99999999 ]
#to display all values
pd.set_option("display.max_rows", None, "display.max_columns", None)

###-----INDEXING VALUES---###
# --------Payment history (35%)--------
#1.Payment information on credit cards, retail accounts, installment loans, mortgages and other types of accounts
first_value = clean_dataset["Monthly Debt"]
second_value = clean_dataset["Years of Credit History"]
#2.How overdue delinquent payments are today or may have become in the past and #3.The amount of time that's passed since delinquencies, adverse public records or collection items were introduced
delinquent = clean_dataset['Months since last delinquent']
#4.The number of accounts that are being paid as agreed
accounts = clean_dataset["Number of Open Accounts"]
# ------Accounts owed (30%)-----------
account_owed = clean_dataset["Current Credit Balance"]
#------Length of credit history (15%)-------------
credit_history = clean_dataset["Years of Credit History"]
# ---------Credit mix (10%) or New Credit(10%)------------
minor4_score = accounts

####----GENERATING SCORES----####
#To display values in 2 decimal places
pd.options.display.float_format = '{:.2f}'.format

#1.Payment History
loan_amount = clean_dataset["Current Loan Amount"]
payment = loan_amount + account_owed
calc_value = payment / first_value
# print(calc_value)

# print(years)
#Job years years = 1 point
job = clean_dataset["Years in current job"]
minor1_score = calc_value + accounts + second_value + job

#FINAL SCORE FOR PAYMENT HISTORY
final_minor1_score=round(minor1_score, 2)
# print(final_minor1_score)

#2. Accounts Owed
value1 = account_owed 
value2 = clean_dataset["Maximum Open Credit"]
value3 = clean_dataset["Current Credit Balance"]
p_borrow = (value3 / value2) 
score2 = 255 * (1 - p_borrow) 
# print(score2)
#FINAL SCORE FOR ACCOUNTS OWED
final_minor2_score = score2 
# print(final_minor2_score)


#3. Length of Credit History
#Ignore delinquent above 84
deduct_delinquent = clean_dataset[clean_dataset["Months since last delinquent"] <= 84 ] 
deducted = deduct_delinquent["Months since last delinquent"] * 1.54
# print(deducted)
added = deducted.replace(0, 127.5)
# print(added)
final_delinquent = deducted + added
# print(final_delinquent)
#FINAL SCORE FOR LENGTH OF CREDIT HISTORY
#1.2 Years of credit history converted to points 1yr=2.67
years = second_value * 2.67
final_minor3_score = years + final_delinquent

#4 New credit or Credit Mix
final_minor4_score = accounts 

#5 Standard Starting Credit Score 

starting_score = 300
#total of all scores
Credit_score = starting_score + final_minor1_score + final_minor2_score + final_minor3_score + final_minor4_score
format_Credit_score = round(Credit_score)
# print (format_Credit_score)
# exceptional_score = (format_Credit_score <= 739) & (format_Credit_score >= 670)
# print(exceptional_score)  

###-----ADDING NEW COLUMNS WITH CALCULATED VALUES TO CSV-----###
# dataset["Score"] = format_Credit_score
# dataset.to_csv("data/new_credit_train.csv", index=False)


#####-----REPLACE NaN VALUES WITH 0-----####
#dataset= dataset.fillna(0)
# ####-----FILTER CREDIT SCORES BETWEEN 0 - 850-----#####
# filter_score = dataset[dataset["Score"] > 0]
# score_range = filter_score[(filter_score["Score"] > 0) & (filter_score["Score"] <= 850)] 


# # #####-----CATEGORIZING SCORES-----#####
# #1. Poor Credit Scores
# poor_score = filter_score[(filter_score["Score"] > 0) & (filter_score["Score"] <= 579)]  
# poor = poor_score["Score"]
# poor_id = poor_score["Customer ID"]
# print("POOR CREDIT SCORES:")
# print(poor)
# # print("Number of Customers:",len(poor))

# #2. Fair Credit Scores
# fair_score = filter_score[(filter_score["Score"] >= 580) & (filter_score["Score"] <= 669)]  
# fair = fair_score["Score"]
# fair_id = fair_score["Customer ID"]
# print("FAIR CREDIT SCORES:")
# print(fair)
# print("Number of Customers:",len(fair))

# #3. Good Credit Scores
# good_score = filter_score[(filter_score["Score"] >= 670) & (filter_score["Score"] <= 739)]  
# good = good_score["Score"]
# good_id = good_score["Customer ID"]
# print("GOOD CREDIT SCORES:")
# print(good)
# print("Number of Customers:",len(good))

# #4. VERY GOOD Credit Scores
# verygood_score = filter_score[(filter_score["Score"] >= 740) & (filter_score["Score"] <= 799)]  
# verygood = verygood_score["Score"]
# verygood_id = verygood_score["Customer ID"]
# print("VERY GOOD CREDIT SCORES:")
# print(verygood)
# print("Number of Customers:",len(verygood))

# #5. Exceptional Credit Scores
# exceptional_score = filter_score[(filter_score["Score"] >= 800) & (filter_score["Score"] <= 850)]  
# exceptional = exceptional_score["Score"]
# exceptional_id = exceptional_score["Customer ID"]
# print("EXCEPTIONAL CREDIT SCORES:")
# print(exceptional)
# print("Number of Customers:",len(exceptional))
# print("Total:",len(exceptional) + len(verygood) + len(good) + len(fair) + len(poor) )

# ####-----BAR CHART-----#####
# Category = ['Poor','Fair','Good','Very Good','Exceptional']
# Number_of_Customer = [len(poor),len(fair),len(good),len(verygood),len(exceptional)]

# plt.bar(Category, Number_of_Customer)
# plt.title('Credit Scores Categorization')
# plt.xlabel('Category')
# plt.ylabel('Number of Customer')
# plt.show()

# ###-----DECISION TREE ALGORITHM---###
# #Converting scores from float to integer
# f_cols = score_range["Score"]
# #reshaping 1d to 2d array
# feature_cols= f_cols.values.reshape(-1,1)

# # print(feature_cols)
# #split dataset in features and target variable
# dtm_loan = score_range["Loan"]
# X = feature_cols # Features
# y = dtm_loan # Target variable


# # Split dataset into training set and test set
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
#                 special_characters=True)
# graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
# graph.write_png('dtm.png')
# Image(graph.create_png())
