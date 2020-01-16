# Returns the bill total
def getBill() :
    #gets the input
    bill = input("Please enter the total for the bill. \n Total: ")
    #validates bill
    newBill = validateGetBill(bill)
    return newBill

# Validates the data for getBillTotal
def validateGetBill(bill):
    validatedBill = validateFloat(bill)
    if validatedBill == True:
        newBill = float(bill)
        return newBill
    if validatedBill == False:
        print("I'm sorry. '" + str(bill)+ "' is not a valid input. Please enter a valid number for the bill.")
        exit(1)

def validateFloat(Float):
    try:
        float(Float)
        return True
    except ValueError:
        return False

# Returns the input for question for service
def getServiceInput():
    # Gets service
    service = input("Please provide a service report. Good = 20% tip, fair = 15% tip, bad = 10% tip. \n Service feedback: ")
    # Validate service
    validateGetServiceInput(service)
    return service

# Validates Service
def validateGetServiceInput(service):
    validatedString = validateString(service)
    if validatedString == True:
        return service

def validateString(service):
    try:
        float(service)
        print("I'm sorry. '" + str(service)+ "' is not a valid input. Please enter a valid input for a service")
        exit(1)
    except ValueError:
        return False

# Gets tip percent and returns it to run()
def getTipPercent(service):
    tip = getPercent(service)
    validatedFloat = validateFloat(tip)
    return tip

def getPercent(service):
    if service.lower() == "good":
        return .2
    if service.lower() == "fair":
        return .15
    if service.lower() == "bad":
        return .1

# Determines how many times the check should be split.
def splitTheCheck():
    numberofSplits = input("How many ways would you like to split the check?")
    validatedNumberofSplits = validateNumberofSplits(numberofSplits)
    return validatedNumberofSplits

def validateNumberofSplits(Splits):
    checkedSplits = validateFloat(Splits)
    if checkedSplits == True:
        return int(Splits)
    if validateFloat(Splits) == False:
        print("I'm sorry. That is not a valid input for the number of splits.")
        exit(1)

def calculate(bill, tipPercent, NoOfSplits):
    # Calcualted the tip
    tip =  bill * tipPercent
    print("The tip for the bill is: " + str(tip) + "$")
    # Calculates the tippedBill
    tippedBill = bill + tip
    print("The total bill is: " + str(tippedBill)+ "$")
    # The reason I do it this way it to allow for future math service. E.G five star rating discounts.
    splitCheck = tippedBill / NoOfSplits
    print("After splitting the check '" + str(NoOfSplits) + "' ways. Each person needs to pay: " + str(splitCheck))

# defines the run program
def run():
    # Gets the bill
    bill = getBill()
    # Gets service
    service = getServiceInput()
    # Gets tip percent based on service
    tipPercent = getTipPercent(service)
    #calculates the number of times to be split
    NoOfSplits = splitTheCheck()
    # Caculates the total bill and prints the results and it goes along
    calculate(bill, tipPercent, NoOfSplits)
  
#runs the program
run()