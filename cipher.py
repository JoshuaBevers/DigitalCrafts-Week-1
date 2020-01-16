# Alphabet
alph = "abcdefghijklmnopqrstuvwxyz"
# Code to decrypt
ciph = "lbh zhfg hayrnea jung lbh unir yrnearq"
#Placeholder
output =  []
finalString = ""
num1 = 0
num2 = 0

# Creating dictionary
dict = {
    0 : "a",
    1 : "b",
    2 : "c",
    3 : "d",
    4 : "e",
    5 : "f",
    6 : "g",
    7 : "h",
    8 : "i",
    9 : "j",
    10 : "k",
    11 : "l",
    12 : "m",
    13 : "n",
    14 : "o",
    15 : "p",
    16 : "q",
    17 : "r",
    18 : "s",
    19 : "t",
    20 : "u",
    21 : "v",
    22 : "w",
    23 : "x",
    24 : "y",
    25 : "z"
}

for str in ciph:
    
    num1 = alph.find(str) + 13
    if num1 >= 26:
        num1 = num1 - 26
       
    num2 = dict[abs(num1)]
    output += num2

finalString = ''.join(output)
print(finalString)
