# Load libraries
import numpy as np
import pandas as pd
import math
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation

df = pd.read_csv('data/new_credit_train.csv')
dff = df.dropna()

# replace NaN values with 0
df= df.fillna(0)

#clean_dataset = df[df["Calculated Credit Score"] != 0 ]
#scores = df["Calculated Credit Score"]

#split dataset in features and target variable
feature_cols = ['Bankruptcies']
X = df[feature_cols] # Features
y = df.Loan # Target variable

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% test

# Create Decision Tree classifer object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

#Libraries for graphing
from sklearn.tree import export_graphviz 
from six import StringIO
from IPython.display import Image  
import pydotplus
import os
os.environ["PATH"] += os.pathsep + 'C:\Program Files\Graphviz/bin/'

dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True,feature_names = feature_cols,class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('test.png')
Image(graph.create_png())