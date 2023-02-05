# Load libraries
from types import FrameType
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation

#to display all output values
pd.set_option("display.max_rows", None, "display.max_columns", None)

df = pd.read_csv('Backup/calculated_orig_credit_train copy.csv')
df['CSPAScore'] = df['CSPAScore'].apply(lambda val: (val /10) if val>850 else val)

df= df.fillna(0)
# print(df["Credit Score"])
#Filter  Credit Scores Greater than 0
filter_score = df[df["CSPAScore"] > 0]
# score_range = filter_score[filter_score["Credit Score"] > 850] 




#######-----------SCORE CATEGORIZATION---------------########
#Filter  Credit Scores Greater than 0 and less than 850.(FICO score range)
filter_score = df[df["CSPAScore"] > 0]
score_range = filter_score[(filter_score["CSPAScore"] > 0) & (filter_score["CSPAScore"] <= 850)] 

#1. Poor Credit Scores
poor_score = filter_score[(filter_score["CSPAScore"] > 0) & (filter_score["CSPAScore"] < 400)]  
poor = poor_score["CSPAScore"]
poor_id = poor_score["Customer ID"]
# print("POOR CREDIT SCORES:")
# # print(poor)
# print("Number of Customers:",len(poor))

#2. Fair Credit Scores
fair_score = filter_score[(filter_score["CSPAScore"] >= 400) & (filter_score["CSPAScore"] <= 570)]  
fair = fair_score["CSPAScore"]
fair_id = fair_score["Customer ID"]
# print("FAIR CREDIT SCORES:")
# # # print(fair)
# print("Number of Customers:",len(fair))

#3. Good Credit Scores
good_score = filter_score[(filter_score["CSPAScore"] >= 571) & (filter_score["CSPAScore"] <= 730)]  
good = good_score["CSPAScore"]
good_id = good_score["Customer ID"]
# print("GOOD CREDIT SCORES:")
# # # print(good)
# print("Number of Customers:",len(good))

#4. VERY GOOD Credit Scores
verygood_score = filter_score[(filter_score["CSPAScore"] >= 731) & (filter_score["CSPAScore"] <= 830)]  
verygood = verygood_score["CSPAScore"]
verygood_id = verygood_score["Customer ID"]
# print("VERY GOOD CREDIT SCORES:")
# # # print(verygood)
# print("Number of Customers:",len(verygood))

#5. Exceptional Credit Scores
exceptional_score = filter_score[(filter_score["CSPAScore"] >= 831) & (filter_score["CSPAScore"] <= 850)]  
exceptional = exceptional_score["CSPAScore"]
exceptional_id = exceptional_score["Customer ID"]
# print("EXCEPTIONAL CREDIT SCORES:")
# print(exceptional)
# print("Number of Customers:",len(exceptional))
Total = len(exceptional) + len(verygood) + len(good) + len(fair) + len(poor)
# print("Total", Total)
#######-----------END OF SCORE CATEGORIZATION---------------########

Poor_percentage = (len(poor) / Total) * 100
print("Poor Percentage:", round(Poor_percentage, 2))
Fair_percentage = (len(fair) / Total) * 100
print("Fair Percentage:", round(Fair_percentage, 2))
Good_percentage = (len(good) / Total) * 100
print("Good Percentage:", round(Good_percentage, 2))
VGood_percentage = (len(verygood) / Total) * 100
print("Very Good Percentage:", round(VGood_percentage, 2))
Exceptional_percentage = (len(exceptional) / Total) * 100
print("Exceptional Percentage:", round(Exceptional_percentage, 2))

###-----BAR CHART-----#####
Category = ['Poor','Fair','Good','Very Good','Exceptional']
Number_of_Customer = [len(poor),len(fair),len(good),len(verygood),len(exceptional)]

plt.bar(Category, Number_of_Customer)
plt.title('Credit Scores Categorization')
plt.xlabel('Category')
plt.ylabel('Number of Customer')
plt.show()