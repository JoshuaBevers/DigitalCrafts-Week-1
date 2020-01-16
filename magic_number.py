import random
#prompt the user for a number
# compare that number to a predefined number.
# if the numbers don't match, prompt the user for another number

def pickNumber():
    user_input = int(input("What number am I thinking of? : "))
    return user_input



MAGICNUMBER = random.randint(1,10)


def game():
   
    while(True) :
        user_input = pickNumber()
        if (user_input == MAGICNUMBER):
            print("HOLY MEGANUMBERS! You're Right!")
            break
        else:
            print("Nope. You egg.")

game()