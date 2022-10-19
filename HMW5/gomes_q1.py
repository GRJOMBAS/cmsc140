#Q1: AlTeRnAtInG CaSePermalink

def altCase(string):
    alternateStr = ""
    upperCase = True
    for char in string :
        if upperCase:
            alternateStr += char.upper() 
        else: 
            alternateStr += char.lower()
        if char.isalpha():
            upperCase = not upperCase
    return alternateStr


string = "Hello class!!"
newString = altCase(string)
print(newString)