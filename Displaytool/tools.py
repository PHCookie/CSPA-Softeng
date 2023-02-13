from colorama import Fore
import matplotlib.pyplot as plt
import pandas as pd
from time import sleep


########-----OPTIONS LIST-----########
def options_list():
    print("\n\nPLEASE CHOOSE AN OPTION!")
    print(f"\n\n{Fore.GREEN}[A] {Fore.WHITE}View Customer Info.")
    print(f"\n{Fore.GREEN}[B] {Fore.WHITE}Show Credit Score.")
    print(f"\n{Fore.GREEN}[C] {Fore.WHITE}Check Credit Score Bar Graph.")
    print(f"\n{Fore.GREEN}[D] {Fore.WHITE}Enter new user data.")
    print(f"\n{Fore.GREEN}[E] {Fore.WHITE}About the CSPA.")
    print(f"\n{Fore.RED}[F] {Fore.WHITE}Exit.")
########-----END OF OPTIONS LIST-----########


########-----LOAN  BAR CHART-----######## 
def bar_chart(category):
    Number_of_Customer = category
    Category = ['Poor','Fair','Good','Very Good','Exceptional']

    print("check")
    plt.bar(Category, Number_of_Customer)
    plt.title('Credit Scores Categorization')
    plt.xlabel('Category')
    plt.ylabel('Number of Customer')
    plt.show()
#######-----------END OF BAR CHART-----------########

#1. For viewing customer ID function
def askidshow():
    Exit = False

    while Exit == False:
        newdataset = pd.read_csv('data/Dataset_Scored.csv')
        askinputid = input(f"{Fore.GREEN}\nPlease enter Customer ID:")
        try:
            ifnum = int(askinputid)
            if ifnum >=1 and ifnum <=122:
                print(newdataset.iloc[ifnum-1])
                print("\n")
                print("(Press 'N' to exit anytime)")
            else:
                print("Sorry! That ID does not exist.")
            continue
        except:
            if askinputid.capitalize() == 'N':
                print(f"{Fore.RED}\nExiting... \n\n")
                Exit = True
            else:
                print("Invalid input.")
                continue

                
                
def newuser(ID):
#ask user input
    LoanAmnt = input("\nEnter customer 'Current Loan Amount':")
    CreditBal = input("\nEnter customer 'Current Credit Balance':")
    MonthDebt = input("\nEnter customer 'Monthly Debt':")
    YearsJob = input("\nEnter customer 'Years in current job':")
    CredHist = input("\nEnter customer 'Years of Credit History':")
    OpenAcc = input("\nEnter customer 'Number of Open Accounts':")
    MonthDel = input("\nEnter customer 'Months since last delinquent':")
    MaxOpCred = input("\nEnter customer 'Maximum Open Credit':")


    dict = {'Customer ID': ID+1, 'Current Loan Amount': LoanAmnt, 'Current Credit Balance': CreditBal,
            'Monthly Debt': MonthDebt, 'Years in current job': YearsJob, 'Years of Credit History': CredHist,
            'Number of Open Accounts': OpenAcc, 'Months since last delinquent': MonthDel, 'Maximum Open Credit': MaxOpCred}

 

    new = [ID+1,LoanAmnt,CreditBal,MonthDebt,YearsJob, CredHist, OpenAcc, MonthDel, MaxOpCred]
    print("\n\nPlease review input: \n", dict)
    sleep(1.50)

    while True:
    
        input1 = input("\n\nRedo information (Y/N)?: ")

        if input1.capitalize() == "Y":
            newuser(ID)

        elif input1.capitalize() == "N":
            break

        else:
            print('Wrong input.') 


    return dict

