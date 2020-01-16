# Returns the bill total
def getBill() :
    bill = float(input("Please enter the total for the bill. \n Total: "))
    #validates bill
    newBill = validateGetBill(bill)
    return newBill

# Validates the data for getBillTotal
def validateGetBill(bill):
    validatedBill = validateFloat(bill)
    if validatedBill == False:
        print("I'm sorry. '" + str(bill)+ "' is not a valid input. Please enter a valid number for the bill.")
        exit(1)
    return bill

def validateFloat(bill):
    try:
        float(bill)
        return bill
    except ValueError:
        return False

# Returns the input for question for service
def getServiceInput():
    # Gets service
    service = input("Please provide a service report. Good = 20% tip, fair = 15% tip, bad = 10% tip. \n Service feedback: ")
    # Validate service
    validateGetServiceInput(service)
    return service

# Validates
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

def validateFloat(tip):
    try:
        float(tip)
        return True
    except ValueError:
        return False


def calculate(bill, tipPercent):
    # Calcualted the tip
    tip =  bill * tipPercent
    print("The tip for the bill is: " + str(tip) + "$")
    # Calculates the tippedBill
    tippedBill = bill + tip
    print("The tippedBill is: " + str(tippedBill)+ "$")
    # The reason I do it this way it to allow for future math service. E.G five star rating discounts.
    totalBill = tippedBill
    return totalBill

# defines the run program
def run():
    # Gets the bill
    bill = getBill()
    # Gets service
    service = getServiceInput()
    # Gets tip percent based on service
    tipPercent = getTipPercent(service)
    # Caculates the total bill
    CALCULATEDBILL = calculate(bill, tipPercent)
    print("The TotalBill per person is: " + str(CALCULATEDBILL) + "$")


#runs the program
run()