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

df = pd.read_csv('data/new_credit_train.csv')

# replace NaN values with 0
df= df.fillna(0)
#Filter  Credit Scores Greater than 0
filter_score = df[df["Score"] > 0]
score_range = filter_score[(filter_score["Score"] > 0) & (filter_score["Score"] <= 850)] 


#####-----CATEGORIZING SCORES-----#####
#1. Poor Credit Scores
poor_score = filter_score[(filter_score["Score"] > 0) & (filter_score["Score"] <= 579)]  
poor = poor_score["Score"]
poor_id = poor_score["Customer ID"]
# print("POOR CREDIT SCORES:")
# print(poor)
# print("Number of Customers:",len(poor))

#2. Fair Credit Scores
fair_score = filter_score[(filter_score["Score"] >= 580) & (filter_score["Score"] <= 669)]  
fair = fair_score["Score"]
fair_id = fair_score["Customer ID"]
# print("FAIR CREDIT SCORES:")
# print(fair)
# print("Number of Customers:",len(fair))

#3. Good Credit Scores
good_score = filter_score[(filter_score["Score"] >= 670) & (filter_score["Score"] <= 739)]  
good = good_score["Score"]
good_id = good_score["Customer ID"]
# print("GOOD CREDIT SCORES:")
# print(good)
# print("Number of Customers:",len(good))

#4. VERY GOOD Credit Scores
verygood_score = filter_score[(filter_score["Score"] >= 740) & (filter_score["Score"] <= 799)]  
verygood = verygood_score["Score"]
verygood_id = verygood_score["Customer ID"]
# print("VERY GOOD CREDIT SCORES:")
# print(verygood)
# print("Number of Customers:",len(verygood))

#5. Exceptional Credit Scores
exceptional_score = filter_score[(filter_score["Score"] >= 800) & (filter_score["Score"] <= 850)]  
exceptional = exceptional_score["Score"]
exceptional_id = exceptional_score["Customer ID"]
# print("EXCEPTIONAL CREDIT SCORES:")
# print(exceptional)
# print("Number of Customers:",len(exceptional))
# print("Total:",len(exceptional) + len(verygood) + len(good) + len(fair) + len(poor) )

##-----BAR CHART-----#####
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