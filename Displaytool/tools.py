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
    print(f"\n{Fore.GREEN}[D] {Fore.WHITE}About the CSPA.")
    print(f"\n{Fore.RED}[E] {Fore.WHITE}Exit.")
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

                

