import numpy as np
import pandas as pd

# Columns: Loan ID,Customer ID,Loan Status,Current Loan Amount,Term,Credit Score,Annual Income,Years in current job,Home Ownership,Purpose,Monthly Debt,Years of Credit History,Months since last delinquent,Number of Open Accounts,Number of Credit Problems,Current Credit Balance,Maximum Open Credit,Bankruptcies,Tax Liens
dataset = pd.read_csv('data/credit_train.csv')

#Remove unwanted values "999999999"
clean_dataset = dataset[dataset["Current Loan Amount"] < 99999999 ]

#Paid and Chargedoff data
paid_dataset = clean_dataset[dataset["Loan Status"] == "Fully Paid"]
chargedoff_dataset = clean_dataset[dataset["Loan Status"] == "Charged Off"]

# Calculation:
# --------Payment history (35%)--------

# ------Accounts owed (30%)-----------
account_owed = clean_dataset["Current Loan Amount"]
#print(account_owed)

#------Length of credit history (15%)-------------
credit_history = clean_dataset["Years of Credit History"]
#print(credit_history)


#loop to get chistory on each spec row
#for x in range(100000):
    #ch = credit_history.iloc[x]
    #print(ch)

# ---------Credit mix (10%)------------

# ---------New credit (10%)------------
