#LIBRARIES
import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib import image as mpimg

def bar_chart():
    Category = ['Poor','Fair','Good','Very Good','Exceptional']
    Number_of_Customer = [len(poor), len(fair), len(good), len(verygood),len(exceptional)]
    plt.bar(Category, Number_of_Customer)
    plt.title('CSPAScores Categorization')
    plt.xlabel('Category')
    plt.ylabel('Number of Customer')
    plt.show()

#NOW LOADING THE NEW DATASET WITH SCORES
newDF = pd.read_csv('Data/FICODataset_scored_CSPA_For proposal.csv', header=0)
# replace NaN values with 0
newDF= newDF.fillna(0)


#######-----------SCORE CATEGORIZATION---------------########
#Filter  CSPAScores Greater than 0 and less than 850.(CSPAScore range)
filter_score = newDF[newDF["CSPAScore"] > 0]
score_range = filter_score[(filter_score["CSPAScore"] > 0) & (filter_score["CSPAScore"] <= 850)] 

#1. Poor CSPAScores
poor_score = filter_score[(filter_score["CSPAScore"] > 0) & (filter_score["CSPAScore"] < 400)]  
poor = poor_score["CSPAScore"]
poor_id = poor_score["Customer ID"]
print("POOR CSPAScoreS:")
# print(poor)
print("Number of Customers:",len(poor))

#2. Fair CSPAScores
fair_score = filter_score[(filter_score["CSPAScore"] >= 400) & (filter_score["CSPAScore"] <= 570)]  
fair = fair_score["CSPAScore"]
fair_id = fair_score["Customer ID"]
print("FAIR CSPAScoreS:")
# # print(fair)
print("Number of Customers:",len(fair))

#3. Good CSPAScores
good_score = filter_score[(filter_score["CSPAScore"] >= 571) & (filter_score["CSPAScore"] <= 730)]  
good = good_score["CSPAScore"]
good_id = good_score["Customer ID"]
print("GOOD CSPAScoreS:")
# # print(good)
print("Number of Customers:",len(good))

#4. VERY GOOD CSPAScores
verygood_score = filter_score[(filter_score["CSPAScore"] >= 731) & (filter_score["CSPAScore"] <= 830)]  
verygood = verygood_score["CSPAScore"]
verygood_id = verygood_score["Customer ID"]
print("VERY GOOD CSPAScoreS:")
# # print(verygood)
print("Number of Customers:",len(verygood))

#5. Exceptional CSPAScores
exceptional_score = filter_score[(filter_score["CSPAScore"] >= 831) & (filter_score["CSPAScore"] <= 850)]  
exceptional = exceptional_score["CSPAScore"]
exceptional_id = exceptional_score["Customer ID"]
print("EXCEPTIONAL CSPAScoreS:")
#print(exceptional)
print("Number of Customers:",len(exceptional))
Total = len(exceptional) + len(verygood) + len(good) + len(fair) + len(poor)
# print("Total", Total)
#######-----------END OF SCORE CATEGORIZATION---------------########

#Display Bar

bar_chart()