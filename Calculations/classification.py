import pandas as pd

# Using Machine Learning 'Random Forest' for Score Classing -
# Less transparent, accuracy 74% tested with online dataset
def byRandomForest(dataset):

    from sklearn.model_selection import train_test_split
    
    # Used as the basis/FICO accurate data 
    df = pd.read_csv('data/FICODATA_modified.csv')
    # USed as the current data to predict
    testingFrame = dataset
    
    # Using Generated Credit Score as class indicator
    header = ['payhis','amtowed','lenofcrhis','newcred']
    
    X = df[header]
    y = df["FICO Score"]

    # Processing Model
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=14)
    from sklearn.ensemble import RandomForestClassifier
    rf_model = RandomForestClassifier(n_estimators=50, random_state=14)
    rf_model.fit(X_train, y_train)

    from sklearn import metrics

    # Dataset Class Score Prediction
    preddata = testingFrame[header]
    result = rf_model.predict(preddata)
    
    #Saving to CSV
    testingFrame["Class Score"] = result

    return testingFrame



# Using the'CSPA scoring' ranges for Score Classing -
# More transparent, accuracy 66% tested with online dataset
def byCSPA(dataset):
    
        #######-----------SCORE CATEGORIZATION---------------########
    #Create new score column
    dataset['CSPA Score'] = ''

    #Filter  Credit Scores Greater than 0 and less than 850.(FICO score range)
    filter_score = dataset[(dataset["Score"] > 0)]
    filter_score = filter_score[(filter_score["Score"] > 0) & (filter_score["Score"] <= 990)] 

    #5. Exceptional Credit Scores
    filter_score['CSPA Score'] = filter_score['CSPA Score'].mask(filter_score["Score"] >= 831, filter_score['CSPA Score'].replace('',"Exceptional"))

    #4. VERY GOOD Credit Scores
    filter_score['CSPA Score'] = filter_score['CSPA Score'].mask(filter_score["Score"] >= 731, filter_score['CSPA Score'].replace('', "Very Good"))


    #3. Good Credit Scores
    filter_score['CSPA Score'] = filter_score['CSPA Score'].mask(filter_score["Score"] >= 571, filter_score['CSPA Score'].replace('',"Good"))


    #2. Fair Credit Scores
    filter_score['CSPA Score'] = filter_score['CSPA Score'].mask(filter_score["Score"] >= 400, filter_score['CSPA Score'].replace('',"Fair"))


    #1. Poor Credit Scores
    filter_score['CSPA Score'] = filter_score['CSPA Score'].mask(filter_score["Score"] > 0, filter_score['CSPA Score'].replace('',"Poor"))

    return filter_score



# Count each class amount. Used only for Graphing
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


