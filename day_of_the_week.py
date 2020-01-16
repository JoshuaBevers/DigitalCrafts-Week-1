
user_input = int(input("Day 0-6: "))


#ran this with a switch statement. Ifs are boring here.
#Next is ternary for the next assignement.
def switch(arguement):
    switcher = {
        1: "Monday",
        2: "Tuesday,",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    print( switcher.get(arguement, "Invalid Day"))

switch(user_input)

# The next assignment
def ternary(day):
    print(' It is a weekend. Sleep in. ' if day >= 6 else 'time to work')
    

ternary(user_input)