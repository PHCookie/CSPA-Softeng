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

df = pd.read_csv('data/orig_credit_train.csv')
#Filter  Credit Scores Greater than 0
filter_score = df[df["Credit Score"] > 0]
# score_range = filter_score[filter_score["Credit Score"] > 850] 




#####-----CATEGORIZING SCORES-----#####
#1. Poor Credit Scores
poor_score = filter_score[(filter_score["Credit Score"] > 0) & (filter_score["Credit Score"] <= 579)]  
poor = poor_score["Credit Score"]
poor_id = poor_score["Customer ID"]
# print("POOR CREDIT SCORES:")
# print(poor)
# print("Number of Customers:",len(poor))

#2. Fair Credit Scores
fair_score = filter_score[(filter_score["Credit Score"] >= 580) & (filter_score["Credit Score"] <= 669)]  
fair = fair_score["Credit Score"]
fair_id = fair_score["Customer ID"]
# print("FAIR CREDIT SCORES:")
# print(fair)
# print("Number of Customers:",len(fair))

#3. Good Credit Scores
good_score = filter_score[(filter_score["Credit Score"] >= 670) & (filter_score["Credit Score"] <= 739)]  
good = good_score["Credit Score"]
good_id = good_score["Customer ID"]
# print("GOOD CREDIT SCORES:")
# print(good)
# print("Number of Customers:",len(good))

#4. VERY GOOD Credit Scores
verygood_score = filter_score[(filter_score["Credit Score"] >= 740) & (filter_score["Credit Score"] <= 799)]  
verygood = verygood_score["Credit Score"]
verygood_id = verygood_score["Customer ID"]
# print("VERY GOOD CREDIT SCORES:")
# print(verygood)
# print("Number of Customers:",len(verygood))

#5. Exceptional Credit Scores
exceptional_score = filter_score[(filter_score["Credit Score"] >= 800) & (filter_score["Credit Score"] <= 850)]  
exceptional = exceptional_score["Credit Score"]
exceptional_id = exceptional_score["Customer ID"]
# print("EXCEPTIONAL CREDIT SCORES:")
# print(exceptional)
# print("Number of Customers:",len(exceptional))
# print("Total:",len(exceptional) + len(verygood) + len(good) + len(fair) + len(poor) )

###-----BAR CHART-----#####
Category = ['Poor','Fair','Good','Very Good','Exceptional']
Number_of_Customer = [len(poor),len(fair),len(good),len(verygood),len(exceptional)]

plt.bar(Category, Number_of_Customer)
plt.title('Credit Scores Categorization')
plt.xlabel('Category')
plt.ylabel('Number of Customer')
plt.show()