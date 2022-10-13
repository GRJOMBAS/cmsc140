import re

""" print("Exercise 2:")
newDirectory = "-".join("C:MyDocuments\Classes\Intro to Python\Week5".split())
print(newDirectory) """

fruit = "apples"
num = 7

#print("I have %s %s."(num, fruit))

print(f'I have {num +1} {fruit}')

print(fruit.upper())
print(fruit.isupper())
print(fruit.lower())

spaceString = "    Hello!    ."
print(spaceString.lstrip())
print(spaceString.rstrip())
print(spaceString.strip())

emails = ['acacia.ackles@lawrence.edu',
    'scott.corry@lawrence.edu',
    'deanna.donohue@lawrence.edu',
    'mmore500@msu.edu',
    'elizabeth.k.sattler@lawrenc.edu']

regex1 = re.compile(r'[a-z]+\.([a-z]+.)?[a-z]+@lawrence.edu$')
for email in emails:
    if re.search(regex1, email):
        print(f"{email} is a valid address.")

print(regex1)

def isValidFile():
    fileRegex = re.compile()