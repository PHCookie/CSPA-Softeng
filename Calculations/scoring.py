def getscore(dataset):
   #1. PAYMENT HISTORY -----------------------------------------------------| (feature 7)

    # 1( Loan Amount , Credit balance) How many payments made
    loan_amount = dataset["Current Loan Amount"]
    monthly_debt = dataset["Monthly Debt"]

    #1.a Monthly Percentage Paid from Overall Loan
    cal= (monthly_debt/loan_amount) * 100
    # processing it to a logarithmic scoring value
    calc_value = (2 ** (-1/cal)) * 90

    #1.b Years of Credit History
    years_ch = dataset["Years of Credit History"]
    years_ch = (1.8 ** (-1/years_ch)) * 140

    #FINAL SCORE FOR PAYMENT HISTORY
    final_minor1_score=round(calc_value + years_ch, 2)

    #END OF PAYMENT HISTORY--------------------------------------------------|


    #2. AMOUNTS OWED --------------------------------------------------------| (feature 8)

    value1 = dataset["Current Loan Amount"]
    value2 = dataset["Maximum Open Credit"]

    #2.a Current Loan Amount
    # current loan amount has the highest feature importance
    loan = (1.8 ** (-1/value1)) * 135

    #2.b Credit Limit Percentage
    limit = value1 / value2 * 100
    # Processing through arithmetic value
    credlim = (round(2100000000/(20000000+(( limit ) ** 4)))) + 90

    #FINAL SCORE FOR PAYMENT HISTORY
    final_minor2_score = credlim + loan

    #END OF AMOUNTS OWED ----------------------------------------------------|


    #3. LENGTH OF CREDIT HISTORY---------------------------------------------| (feature 9)

    #Ignore delinquent above 84
    deduct_delinquent = dataset[dataset["Months since last delinquent"] <= 1000 ]
    added = deduct_delinquent.replace(0, 900)
    deducted = round(15600/(160+(added["Months since last delinquent"] ** 2)))

    #1.2 Years of credit history converted to points 1yr=2.67
    years = years_ch * 2.67
    # limiting score
    years = (7 ** (1/-years)) * 160.6            

    #FINAL SCORE FOR LENGTH OF CREDIT HISTORY
    final_minor3_score = years - (deducted/2)

    #END OF LENGTH OF CREDIT HISTORY-----------------------------------------| (feature 10)


    #4 NEW CREDIT / CREDIT MIX-----------------------------------------------|

    final_minor4_score = (((5 ** (-2/dataset["Number of Open Accounts"])) * 10)+20) * 2

    #END OF NEW CREDIT / CREDIT MIX------------------------------------------|


    #5 STARTING SCORE--------------------------------------------------------|

    #Total of all scores
    Credit_score = final_minor1_score + final_minor2_score + final_minor3_score + final_minor4_score
    format_Credit_score = round(Credit_score)

    #Saving scores to CSV
    dataset["payhis"] = final_minor1_score
    dataset["amtowed"] = final_minor2_score
    dataset["lenofcrhis"] = final_minor3_score
    dataset["newcred"] = final_minor4_score
    dataset["Score"] = format_Credit_score

    return dataset
