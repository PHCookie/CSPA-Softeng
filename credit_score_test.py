import numpy as np
import pandas as pd

# Columns: Loan ID,Customer ID,Loan Status,Current Loan Amount,Term,Credit Score,Annual Income,Years in current job,Home Ownership,Purpose,Monthly Debt,Years of Credit History,Months since last delinquent,Number of Open Accounts,Number of Credit Problems,Current Credit Balance,Maximum Open Credit,Bankruptcies,Tax Liens
dataset = pd.read_csv('data/credit_train.csv')
print(dataset[dataset["Loan Status"] == "Fully Paid"])

# Calcuation:
# Payment history (35%)
# Accounts owed (30%)
# Length of credit history (15%)
# Credit mix (10%)
# New credit (10%)
