with open('madlib_read_file.txt') as f:
    flat_list=[word for line in f for word in line.split()]
    emptyString = ""
    addTo = ""
    for word in flat_list:
        addTo = " "
        if word == "(adjective)":
            newWord = input("Please enter an adjective")
            addTo += newWord
        if word == "(Noun)":
            newWord = input("please enter a noun")
            addTo += newWord
        if word == "(Verb, past tense)":
            newWord = input("please enter a Verb, past tense.")
            addTo += newWord
        if word == "(adverb)":
            newWord = input("Please enter an adverb")
            addTo += newWord
        if word == "verb":
            newWord = input("Please enter a verb")
            addTo += newWord

        elif word == " ":
            addTo += " "
        else:
            addTo += word
        emptyString += addTo
    
    
    print(emptyString)
            
    
#known issues with code. Does not remove the tags that the if statements search for. WIP.

