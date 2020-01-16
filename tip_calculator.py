# build a tip calculator
# The goal of this bit is to 'reach for the sword'
# I'm practicing functions, arguments, and calls in python

# get the total amount of the bill
bill = float(input("How much was the total bill? : "))

# prompt the user for the level of service

service = input("What was your level of service \n bad? \n Fair? \n good? \n Please type in one of the above suggestions: ")

def calculate(bill, service):
    tip = bill * good_service(service)
    print(tip)
    totalbill = bill + tip
    print(round(totalbill, 2))
    return totalbill

# get the various level of services.
def good_service(service):
    while (True):
        try:  
            if service == "bad":
                break
                return .1
            if service == "good":
                break
                return .15
            if service == "fair":
                break
                return .2
            else:
                print("that is not a valid service. Please run the program again.")
        except:
            print("This failed ingracefully.")

THEBILL = calculate(bill, service)

#assignment two, Split the check

def splitTheCheck():
    split = input("would you like to split the check? Y/N : ")
    if split == "y":
        splits = input("how many ways?")
        return splits
    else:
        print("Your total is " + str(THEBILL))

def splitCalculate(split):
    newbill = float(THEBILL) / float(split)
    print("Your new total is: " + str(newbill))

# splits the check
num_of_splits = splitTheCheck()

#calculates the total from the number of splits
splitCalculate(num_of_splits)


# the simple way of solving this problem.
# This lacks certain UI perks or hints that are provided in the above example. E.G displaying the level of services available.
# If the user doesn't enter a valid service level below, it doesn't tell you what when wrong.

bill = float(input("What is the total off the bill? \n"))
tip = input("What is the level of service?")
split = input("How many ways are you splitting the bill?")

print("the total tip is: " + str(tip))
service2 = .1 if tip == "bad" else .15 if tip == "good" and tip != "fair" else "This is not a valid selection."
print()