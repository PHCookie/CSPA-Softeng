import pandas as pd

    # Using Random Forest Generates a 67% accuracy.
def byRandomForest(dataset):

    from sklearn.model_selection import train_test_split
    df = pd.read_csv('data/FICODATA_modified.csv')
    testingFrame = dataset

    X = df.drop(["Customer ID", "FICO Score","Score","newcred"], axis=1)
    y = df["FICO Score"]


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=14)
    from sklearn.ensemble import RandomForestClassifier
    rf_model = RandomForestClassifier(n_estimators=50, random_state=14)
    rf_model.fit(X_train, y_train)

    #predictions = rf_model.predict(X_test)
    from sklearn import metrics
    # Model Accuracy, how often is the classifier correct?
    #print("Accuracy:",metrics.accuracy_score(y_test, predictions))


    preddata = testingFrame.drop(["Customer ID", "Current Loan Amount",
                                  "Months since last delinquent" ,"newcred", "Score"], axis=1)


    result = rf_model.predict(preddata)
    testingFrame["Class Score"] = result

    return testingFrame

def obtain(dataset):

    #1. Poor Credit Scores
    poor = dataset[(dataset["Class Score"] == "Poor")]  

    #2. Fair Credit Scores 
    fair = dataset[(dataset["Class Score"] == "Fair")]  

    #3. Good Credit Scores 
    good = dataset[(dataset["Class Score"] == "Good")]

    #4. VERY GOOD Credit Scores   
    verygood = dataset[(dataset["Class Score"] == "Very Good")]    

    #5. Exceptional Credit Scores]    
    exceptional = dataset[(dataset["Class Score"] == "Exceptional")]  

    Total = [len(poor), len(fair), len(good), len(verygood),len(exceptional)]
    
    return Total


def byCSPA(dataset):

        #######-----------SCORE CATEGORIZATION---------------########
    #Filter  Credit Scores Greater than 0 and less than 850.(FICO score range)
    filter_score = dataset[(dataset["Score"] > 0)]
    filter_score = filter_score[(filter_score["Score"] > 0) & (filter_score["Score"] <= 990)] 

    #5. Exceptional Credit Scores
    filter_score['Class Score'] = filter_score['CSPA Score'].mask(filter_score["Score"] >= 831, filter_score['CSPA Score'].replace(0,"Exceptional"))

    #4. VERY GOOD Credit Scores
    filter_score['Class Score'] = filter_score['CSPA Score'].mask(filter_score["Score"] >= 731, filter_score['CSPA Score'].replace(0, "Very Good"))


    #3. Good Credit Scores
    filter_score['Class Score'] = filter_score['CSPA Score'].mask(filter_score["Score"] >= 571, filter_score['CSPA Score'].replace(0,"Good"))


    #2. Fair Credit Scores
    filter_score['Class Score'] = filter_score['CSPA Score'].mask(filter_score["Score"] >= 400, filter_score['CSPA Score'].replace(0,"Fair"))


    #1. Poor Credit Scores
    filter_score['Class Score'] = filter_score['CSPA Score'].mask(filter_score["Score"] > 0, filter_score['CSPA Score'].replace(0,"Poor"))

    return dataset


