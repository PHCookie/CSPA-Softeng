def getscore(dataset):
    # 1( Loan Amount , Credit balance) How many payments made
    loan_amount = dataset["Current Loan Amount"]
    monthly_debt = dataset["Monthly Debt"]
    cal= (monthly_debt/loan_amount) * 100
    calc_value = (2 ** (-1/cal)) * 82
    #1.a Years of Credit History 1yr= 1point
    years_ch = dataset["Years of Credit History"] #120
    years_ch = (1.8 ** (-1/years_ch)) * 122

    #1.b Job years years = 1 point
    job = dataset["Years in current job"] 
    job = (3 ** (-1/job)) * 52
    #1.c Accounts: Types of accounts considered for credit payment history
    accounts = dataset["Number of Open Accounts"]
    accounts = round((1.05 ** (-1/accounts)) * 50)

    #FINAL SCORE FOR PAYMENT HISTORY
    minor1_score = calc_value + accounts + years_ch + job 
    final_minor1_score=round(minor1_score, 2)

    #END OF PAYMENT HISTORY--------------------------------------------------|

    #2. AMOUNTS OWED --------------------------------------------------------|
    value1 = dataset["Current Loan Amount"]
    value2 = dataset["Maximum Open Credit"]

    #FINAL SCORE FOR ACCOUNTS OWED
    final_minor2_score = (round(2100000000/(20000000+(((value1 / value2) * 100) ** 4)))) + 140
            
    #END OF AMOUNTS OWED ----------------------------------------------------|

    #3. LENGTH OF CREDIT HISTORY---------------------------------------------|
    #Ignore delinquent above 84
    deduct_delinquent = dataset[dataset["Months since last delinquent"] <= 1000 ]
    added = deduct_delinquent.replace(0, 900)
    deducted = round(15600/(160+(added["Months since last delinquent"] ** 2)))
    #1.2 Years of credit history converted to points 1yr=2.67
    years = years_ch * 2.67

    #FINAL SCORE FOR LENGTH OF CREDIT HISTORY
    final_minor3_score = (7 ** (1/-years)) * 140.6 - (deducted/2)

    # print(final_minor3_score)
    #END OF LENGTH OF CREDIT HISTORY-----------------------------------------|

    #4 NEW CREDIT / CREDIT MIX-----------------------------------------------|
    final_minor4_score = (((5 ** (-2/dataset["Number of Open Accounts"])) * 10)+30) * 2 

                
    #END OF NEW CREDIT / CREDIT MIX------------------------------------------|

    #5 STARTING SCORE--------------------------------------------------------|

    #Total of all scores
    Credit_score = final_minor1_score + final_minor2_score + final_minor3_score + final_minor4_score + 20
    format_Credit_score = round(Credit_score)
    #print (format_Credit_score)

            
    dataset["payhis"] = final_minor1_score
    dataset["amtowed"] = final_minor2_score
    dataset["lenofcrhis"] = final_minor3_score
    dataset["newcred"] = final_minor4_score
    dataset["Score"] = format_Credit_score
    return dataset