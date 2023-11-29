# Program to 
#
# Date Written: Nov 16th, 2023 - Nov 28th, 2023
# Author: Riley Hiron

'''
The One  Stop  Insurance  Companyneeds  a  program  to  enter  and  calculate  new  insurance  policy information for its customers. Allow the program to repeat to allow the user to enter as many customers as they want.  Add at least 3 functions to the program.  I will accept the FormatValues library as a function option –but you need to add a new function to the library.

Set  up  the  following  default  values  for the  next  policy  number,  the  basic  premium,  the  discount  for additional  cars,  the  cost  of  extra  liability  coverage,  the  cost  of  glass  coverage,  the  cost  for  loaner  car coverage, the HST rate, and the processing fee for monthly payments. The values are 1944, , 869.00, .25, 130.00, 86.00, 58.00, .15, and 39.99 respectfully.

The user will input the customer’sfirst and last name, address, city, province(validate using a list to make sure the province is valid), postal code,and phone number.  They will also enter the number of cars being insured,and  options  for  extra  liability  up  to  $1,000,000  (enter  Y  for  Yes  or  N  for  No),  optional  glass coverage (Y or N), and optional loaner car (Y or N).Finally enter a value to indicate if they want to pay in full or monthly (Fullor Monthlyor Down Pay–use a list to validate). If the enter Down Pay allow them to enter  the  amount  of  the  down  payment.   Finally  enter  the  date  and  cost  of  all  previous  claims  for  the customer –press Enter to finish.  Add at least 2-3 claims and store the values in lists.  Convert the first and last name, the city, and the payment Methodto title case and the Y/N values upper case.  No validations required –other than those specified -but go for it if you want.Be careful when testing -enter values that are valid for each input.

Insurance  premiums  are  calculated  using  a  basic  rate  of  $869.00  for  the  first  automobile,  with  each additional automobile offered at a discount of 25%. If the user enters a Y for any of the options, the costs are $130.00 per car for extra liability, $86.00 per car for glass coverage, and $58.00 per car for the loaner car option. All these values are added together for the total extra costs. The total insurance premiumis the premium plus the total extra costs. HST is calculated at 15% on the total insurancepremium, and the total cost is the total insurance premium plus the HST. Customers canpay for their insurance in full or in 8  monthly  payments,  with  or  without  a  downpayment.  Calculate  the  monthly  payment  by  adding  a processing  fee  of $39.99  to  the  total costand  dividing  the  total cost  by 8.If  the  user  entered  a  down payment, determine the monthly payment based on the total price less the downpayment with the same processing feeover the same 8 months.  The invoice date is the current date,and the firstpayment date is the first day of the next month.

***** 
'''
# Imports
import datetime
import Formats as FF


# Constants
POLICY_NUMBER = 1944
BASIC_PREMIUM = 869.00
DISCOUNT = .25
EXTRA_LIABILITY = 130.00
GLASS_COVERAGE = 86.00
LOANER_CAR = 58.00
HST = .15
PROCESSING_FEE = 39.99
ALLOWED_NAME_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'-"
ALLOWED_PROV = ["AB", "BC", "MB", "NB", "NL", "NS", "NT", "NU", "ON", "PE", "QC", "SK", "YT"]
PAYMENT_TYPES = ["Full", "Monthly", "Down Pay"]
NUM_SUFFIXS = ["st", "nd", "rd", "th"]
NUM_EXEPTIONS = [11, 12, 13]
CUR_DATE = datetime.datetime.now()

# Functions
def Num_Suffix(Number):
    if Number in NUM_EXEPTIONS:
        return NUM_SUFFIXS[3]
    elif Number % 10 == 1:
        return NUM_SUFFIXS[0]
    elif Number % 10 == 2:
        return NUM_SUFFIXS[1]
    elif Number % 10 == 3:
        return NUM_SUFFIXS[2]
    else:
        return NUM_SUFFIXS[3]

# Inputs
while True:
    while True:
        # Validating First Name (Must be letters, apostrophes, and hyphens, cannot be blank) changed to title case
        Cust_F_Name = input("Enter customers first name: ").title()
        if Cust_F_Name == "":
            print("First Name cannot be blank - please re-enter")
        elif set(Cust_F_Name).issubset(ALLOWED_NAME_CHARS):
            break
        else:
            print("First Name can only contain letters, apostrophes, and hyphens - please re-enter")
    while True:
        # Validating Last Name (Must be letters, apostrophes, and hyphens, cannot be blank) changed to title case
        Cust_L_Name = input("Enter Customers last name: ").title()
        if Cust_L_Name == "":
            print("Last Name cannot be blank - please re-enter")
        elif set(Cust_L_Name).issubset(ALLOWED_NAME_CHARS):
            break
        else:
            print("Last Name can only contain letters, apostrophes, and hyphens - please re-enter")
    Street_Address = input("Enter Customers street address: ").title()
    City = input("Enter Customers city: ").title()
    while True:
        # Validating Province (Must be in alllowed province list, cannot be blank) changed to upper case
        Prov = input("Enter Customers province (XX): ").upper()
        if Prov in ALLOWED_PROV:
            break
        else:
            print("Province must be one of the following: AB, BC, MB, NB, NL, NS, NT, NU, ON, PE, QC, SK, YT - please re-enter")
    while True:
        # Validating Postal Code (Must be in format X9X9X9) changed to upper case
        Postal_Code = input("Enter Customers postal code (X9X9X9): ").upper()
        if (Postal_Code[::2].isalpha() and Postal_Code[1::2].isdigit() and len(Postal_Code) == 6):
            break
        else:
            print("Postal code must be in the format X9X9X9 - please re-enter")
    while True:
        # Validating Phone Number (Must be 10 digits long, cannot be blank, must be digits)
        Phone_Num = input("Enter Customers phone number (9999999999): ")
        if Phone_Num.isdigit() and len(Phone_Num) == 10:
            break
        elif Phone_Num == "":
            print("Phone number cannot be blank - please re-enter")
        elif len(Phone_Num) != 10:
            print("Phone number must be 10 digits long - please re-enter")
        else:
            print("Phone number can only contain digits - please re-enter")
    while True:
        # Validating Number of Cars (Must be greater than 0, cannot be blank) changed to Integer
        # Using try/except to catch inputs that arent integers and re-prompting as to not throw an error
        try:
            Num_Of_Cars = int(input("Enter the number of cars you have: "))
            if Num_Of_Cars == "":
                print("Number of cars cannot be blank - please re-enter")
            elif Num_Of_Cars > 0:
                break
            else:
                print("Number of cars must be greater than 0 - please re-enter")
        except ValueError:
            print("Invalid input - please enter a valid number for the number of cars")
    while True:
        # Validating Extra Liability (Must be Y or N, cannot be blank) changed to upper case
        Extra_Liability = input("Do you want extra liability coverage? (Y/N): ").upper()
        if Extra_Liability == "Y" or Extra_Liability == "N":
            break
        else:
            print("Invalid input - please enter 'Y' for Yes or 'N' for No")

    while True:
        # Validating Glass Coverage (Must be Y or N, cannot be blank) changed to upper case
        Glass_Coverage = input("Do you want glass coverage? (Y/N): ").upper()
        if Glass_Coverage == "Y" or Glass_Coverage == "N":
            break
        else:
            print("Invalid input - please enter 'Y' for Yes or 'N' for No")

    while True:
        # Validating Loaner Car (Must be Y or N, cannot be blank) changed to upper case
        Loaner_Car = input("Do you want loaner car coverage? (Y/N): ").upper()
        if Loaner_Car == "Y" or Loaner_Car == "N":
            break
        else:
            print("Invalid input - please enter 'Y' for Yes or 'N' for No")
    while True:
        # Validating Payment Method (Must be in payment types list, cannot be blank) changed to title case
        Payment_Method = input("How would you like to pay? (Full/Monthly/Down Pay): ").title()
        if Payment_Method == PAYMENT_TYPES[2]:
            while True:
                try:
                    # using try/except to catch inputs that arent floats and re-prompting as to not throw an error
                    Down_Payment = float(input("Enter the amount of your down payment: "))
                except ValueError:
                    print("Invalid input - please enter a valid number for the down payment")
                    Down_Payment = 0.00
                if Down_Payment > 0:
                    break
                else:
                    print("Down payment must be greater than 0 - please re-enter")
            break
        elif Payment_Method == PAYMENT_TYPES[0] or Payment_Method == PAYMENT_TYPES[1]:
            Down_Payment = 0.00
            break
        else:
            print("Invalid input - please enter 'Full' for Full, 'Monthly' for Monthly, or 'Down Pay' for Down Payment")

    while True:
        try:
            # Validating Number of Claims (Must be greater than or equal to 0, cannot be blank) changed to Integer
            Num_Of_Claims = int(input("Enter the number of previous claims you have: "))
            if Num_Of_Claims >= 0:
                break
            else:
                print("Number of claims must be greater than or equal to 0 - please re-enter")
        except ValueError:
            print("Invalid input - please enter a valid number for the number of claims")
    P_Claims_Cost = []
    P_Claims_Date = []
    Claim_Counter = 1
    while Num_Of_Claims > 0:
        while True:
            try:
                # using try/except to catch inputs that arent floats and re-prompting as to not throw an error
                P_Claims_Cost.append(float(input("Enter the cost of the " + str(Claim_Counter) + Num_Suffix(Claim_Counter) + " claim: ")))
                break
            except ValueError:
                print("Invalid input - please enter a valid number for the cost of the claim")
        while True:
            try:
                # using try/except to catch inputs that arent dates and re-prompting as to not throw an error
                P_Claims_Date.append(datetime.datetime.strptime(input("Enter the date of the " + str(Claim_Counter) + Num_Suffix(Claim_Counter) + " claim (DD/MM/YYYY): "), "%d/%m/%Y"))
                break
            except ValueError:
                print("Invalid input - please enter a valid date for the date of the claim")
        Claim_Counter += 1
        Num_Of_Claims -= 1
    # Calculations
    Insurance_Premium = BASIC_PREMIUM + (BASIC_PREMIUM * DISCOUNT * (Num_Of_Cars - 1))
    Extras_Cost = 0
    if Extra_Liability == "Y":
        Extras_Cost += EXTRA_LIABILITY * Num_Of_Cars
    if Glass_Coverage == "Y":
        Extras_Cost += GLASS_COVERAGE * Num_Of_Cars
    if Loaner_Car == "Y":
        Extras_Cost += LOANER_CAR * Num_Of_Cars
    Total_Insurance_Premium = Insurance_Premium + Extras_Cost
    HST_Cost = Total_Insurance_Premium * HST
    Total_Cost = Total_Insurance_Premium + HST_Cost
    if Payment_Method == PAYMENT_TYPES[0]:
        Monthly_Payment =  0
    elif Payment_Method == PAYMENT_TYPES[1]:
        Monthly_Payment = (Total_Cost + PROCESSING_FEE) / 8
    elif Payment_Method == PAYMENT_TYPES[2]:
        Monthly_Payment = (Total_Cost - Down_Payment) / 8
    Invoice_Date = CUR_DATE.strftime("%d/%m/%Y")
    First_Payment_Date = (CUR_DATE + datetime.timedelta(days=31)).replace(day=1)
    First_Payment_Date = First_Payment_Date.strftime("%d/%m/%Y")
    # Outputs
    print("\n\n")
    print(f"{'One Stop Insurance':^50}")
    print(f"{'Customer Invoice':^50}")
    print(f"{'-' * 51}")
    print(f"{'Policy Number:':<25} {POLICY_NUMBER:>25}")
    print(f"{'-' * 51}")
    print(f"{'Customer Information':^50}")
    print(f"{'-' * 51}")
    print(f"{'Name:':<25} {Cust_F_Name + ' ' + Cust_L_Name:>25}")
    print(f"{'Address:':<25} {Street_Address:>25}")
    print(f"{'City:':<25} {City:>25}")
    print(f"{'Province:':<25} {Prov:>25}")
    print(f"{'Postal Code:':<25} {Postal_Code:>25}")
    print(f"{'Phone Number:':<25} {Phone_Num:>25}")
    print(f"{'-' * 51}")
    print(f"{'Insurance Information':^50}")
    print(f"{'-' * 51}")
    print(f"{'Number of Cars:':<25} {Num_Of_Cars:>25}")
    print(f"{'Extra Liability:':<25} {Extra_Liability:>25}")
    print(f"{'Glass Coverage:':<25} {Glass_Coverage:>25}")
    print(f"{'Loaner Car:':<25} {Loaner_Car:>25}")
    print(f"{'-' * 51}")
    print(f"{'Payment Information':^50}")
    print(f"{'-' * 50}")
    print(f"{'Payment Method:':<25} {Payment_Method:>25}")
    print(f"{'Down Payment:':<25} {Down_Payment:>25.2f}")
    print(f"{'Monthly Payment:':<25} {Monthly_Payment:>25.2f}")
    print(f"{'-' * 51}")
    print(f"{'Costs':^50}")
    print(f"{'-' * 51}")
    # Calculated values
    print(f"{'Insurance Premium:':<25} {Insurance_Premium:>25.2f}")
    print(f"{'Extras Cost:':<25} {Extras_Cost:>25.2f}")
    print(f"{'Total Insurance Premium:':<25} {Total_Insurance_Premium:>25.2f}")
    print(f"{'HST:':<25} {HST_Cost:>25.2f}")
    print(f"{'Total Cost:':<25} {Total_Cost:>25.2f}")
    print(f"{'-' * 51}")
    print(f"{'Invoice Date:':<25} {Invoice_Date:>25}")
    print(f"{'First Payment Date:':<25} {First_Payment_Date:>25}")
    print(f"{'-' * 51}")
    print(f"{'Claim #  Claim Date        Amount':^51}")
    print(f"{'-' * 33:^51}")
    # Claim values
    for i in range(len(P_Claims_Cost)):
        print(f"           {i + 1}.     {P_Claims_Date[i].strftime('%Y-%m-%d')}    {FF.Format_Currency(P_Claims_Cost[i]):>10}")
    print("\n")

    while True:
        # Checking if user wants to enter another customer (Must be Y or N, cannot be blank) changed to upper case
        Continue = input("Would you like to enter another customer? (Y/N): ").upper()
        if Continue == "Y" or Continue == "N":
            break
        else:
            print("Invalid input - please enter 'Y' for Yes or 'N' for No")
    if Continue == "N":
        break
    else:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    

