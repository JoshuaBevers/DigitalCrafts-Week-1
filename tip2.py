
bill = float(input("What is the total off the bill? \n"))
service = input("What is the level of service?")
tip = .1 if service == "bad" else .2 if service == "good" and service != "fair"  else .15
total = bill * tip
print("the total tip is: " + str(total))
split = float(input("How many ways are you splitting the bill?"))
print("The split totals are: " + str(total / split))

# This was to conform closer to what the actual exercise was for the class. Not particularily happy with this one.
# service2 = .1 if tip == "bad" else .2 if tip == "good" and tip != "fair"  else .15
