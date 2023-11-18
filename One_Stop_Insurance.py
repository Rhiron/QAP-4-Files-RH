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
import Formats as FM

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
CUR_DATE = datetime.datetime.now()



# Inputs
while True:
    # Creating an empty dictionary to store customer information
    Customer_Info = {}

    # Gathering Customers First name ending program if blank. Validations(Must be letters, apostrophes, and hyphens)
    while True:
        Cust_F_Name = input("Enter customers first name (Leave Blank to End Program): ").title()
        if set(Cust_F_Name).issubset(ALLOWED_NAME_CHARS):
            break
        elif Cust_F_Name == "":
            break
        else:
            print("First Name can only contain letters, apostrophes, and hyphens - please re-enter")
    Customer_Info['First Name'] = Cust_F_Name
    if Cust_F_Name == "":
        print('''\n\n========================================================
||            Program has been terminated             ||
|| Thank you for using the One Stop Insurance Company ||
||                 Have a nice day!                   ||
========================================================\n\n''')
    # Gathering Customers Last name.  Validations(Must be letters, apostrophes, and hyphens)
    while True:
        Cust_L_Name = input("Enter Customers last name: ").title()
        if set(Cust_L_Name).issubset(ALLOWED_NAME_CHARS):
            break
        elif Cust_L_Name == "":
            print("Last Name cannot be blank - please re-enter")
        else:
            print("Last Name can only contain letters, apostrophes, and hyphens - please re-enter")
    Customer_Info['Last Name'] = Cust_L_Name
    Street_Address = input("Enter Customers street address: ").title()
    Customer_Info['Street Address'] = Street_Address
    City = input("Enter Customers city: ").title()
    Customer_Info['City'] = City
    # Gathering Customers province.  Validations(Must be in the list of allowed provinces)
    while True:
        Prov = input("Enter Customers province (XX): ").upper()
        if Prov in ALLOWED_PROV:
            break
        else:
            print("Province must be one of the following: AB, BC, MB, NB, NL, NS, NT, NU, ON, PE, QC, SK, YT - please re-enter")
    Customer_Info['Province'] = Prov
    # Gathering Customers postal code.  Validations(Must be in the format X9X9X9)
    while True:
        Postal_Code = input("Enter Customers postal code (X9X9X9): ").upper()
        if (Postal_Code[::2].isalpha() and Postal_Code[1::2].isdigit()):
            break
        else:
            print("Postal code must be in the format X9X9X9 - please re-enter")
    Customer_Info['Postal Code'] = Postal_Code
    # Gathering Customers phone number.  Validations(Must be 10 digits long and must be all digits)
    while True:
        Phone_Num = input("Enter Customers phone number (9999999999): ")
        if Phone_Num.isdigit() and len(Phone_Num) == 10:
            break
        elif Phone_Num == "":
            print("Phone number cannot be blank - please re-enter")
        elif len(Phone_Num) != 10:
            print("Phone number must be 10 digits long - please re-enter")
        else:
            print("Phone number can only contain digits - please re-enter")
    Customer_Info['Phone Number'] = FM.Format_Phone_Num(Phone_Num)
    # Gathering Number of cars being insured.  Validations(Must be greater than 0)
    while True:
        # Using try/except to catch invalid inputs
        try:
            Num_Of_Cars = int(input("Enter the number of cars that are being insured: "))
            if Num_Of_Cars > 0:
                break
            else:
                print("Number of cars must be greater than 0 - please re-enter")
        except ValueError:
            print("Invalid input - please enter a valid number for the number of cars")
    Customer_Info['Number of Cars'] = Num_Of_Cars
    # Checking if the customer wants extra liability coverage.  Validations(Must be Y or N)
    while True:
        Extra_Liability = input("Does the customer want extra liability coverage? (Y/N): ").upper()
        if Extra_Liability == "Y" or Extra_Liability == "N":
            break
        else:
            print("Invalid input - please enter Y or N")
    Customer_Info['Extra Liability Coverage'] = Extra_Liability
    # Checking if the customer wants glass coverage.  Validations(Must be Y or N)
    while True:
        Glass_Coverage = input("Does the customer want glass coverage? (Y/N): ").upper()
        if Glass_Coverage == "Y" or Glass_Coverage == "N":
            break
        else:
            print("Invalid input - please enter Y or N")
    Customer_Info['Glass Coverage'] = Glass_Coverage
    # Checking if the customer wants loaner car coverage.  Validations(Must be Y or N)
    while True:
        Loaner_Car = input("Does the customer want loaner car coverage? (Y/N): ").upper()
        if Loaner_Car == "Y" or Loaner_Car == "N":
            break
        else:
            print("Invalid input - please enter Y or N")
    Customer_Info['Loaner Car Coverage'] = Loaner_Car
    # Checking how the customer wants to pay.  Validations(Must be Full, Monthly, or Down Pay)
    while True:
        Payment_Method = input("How is the customer paying? (Full/Monthly/Down Pay): ").title()
        if Payment_Method in PAYMENT_TYPES:
            # If Customer wants down payment then asking for the amount.  Validations(Must be greater than 0)
            if Payment_Method == PAYMENT_TYPES[2]:
                while True:
                    # Using try/except to catch invalid inputs
                    try:
                        Down_Payment = float(input("Enter the amount of the down payment: "))
                        if Down_Payment > 0:
                            break
                        else:
                            print("Down payment must be greater than 0 - please re-enter")
                    except ValueError:
                        print("Invalid input - please enter a valid number for the down payment")
            break
        else:
            print("Invalid input - please enter Full, Monthly, or Down Pay")
    Customer_Info['Payment Method'] = Payment_Method
    # Gathering the Number of previous claims.  Validations(Must be greater than or equal to 0)
    while True:
        try:
            Num_Of_Claims = int(input("Enter the number of previous claims the customer has made: "))
            if Num_Of_Claims >= 0:
                break
            else:
                print("Number of claims must be greater than or equal to 0 - please re-enter")
        except ValueError:
            print("Invalid input - please enter a valid number for the number of claims")
    Customer_Info['Number of Claims'] = Num_Of_Claims
    # Creating empty lists to store the previous claims information
    Claim_Costs = []

    # Print out the customer information
    print(Customer_Info)
    


# Calculations


# Output

