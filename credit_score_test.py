import numpy as np
import pandas as pd
import math

# Columns: Loan ID,Customer ID,Loan Status,Current Loan Amount,Term,Credit Score,Annual Income,Years in current job,Home Ownership,Purpose,Monthly Debt,Years of Credit History,Months since last delinquent,Number of Open Accounts,Number of Credit Problems,Current Credit Balance,Maximum Open Credit,Bankruptcies,Tax Liens
dataset = pd.read_csv('data/credit_train.csv')

#Remove unwanted values "999999999"
clean_dataset = dataset[dataset["Current Loan Amount"] < 99999999 ]

#to display all values
pd.set_option("display.max_rows", None, "display.max_columns", None)

# Calculation:

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

####----Generating Scores----####
#1.Payment History
calc_value = first_value / second_value
approx_score = calc_value / accounts
minor1_score = approx_score - delinquent
limit_minor1_score=round(minor1_score, 2)

#print(limit_minor1_score)

#2. Accounts Owed
value1 = account_owed / accounts
monthly_debt = first_value
value2 = monthly_debt / accounts
minor2_score = value1 / value2
limit_minor2_score = round(minor2_score, 2)

#print(limit_minor2_score)

#3. Length of Credit History
minor3_score = credit_history

#4 New credit or Credit Mix
minor4_score = accounts

#total of all scores
Credit_score = minor1_score + minor2_score + minor3_score + minor4_score
format_Credit_score = round(Credit_score, 2)

# Adding to csv
#dataset["Calculated CreditScore"] = format_Credit_score
#dataset.to_csv("new_credit_train.csv", index=False)


#Credit Score Correction scaled by 10
#credit_score = clean_dataset[clean_dataset["Credit Score"] < 850]
#normal_score = credit_score["Credit Score"]
#print(normal_score)
#abnormal_cscore = clean_dataset[clean_dataset["Credit Score"] > 850]
#scale_cscore = abnormal_cscore["Credit Score"] / 10
#print(scale_cscore)






