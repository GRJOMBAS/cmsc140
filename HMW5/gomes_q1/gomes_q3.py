import re

rYes = re.compile(r'^(?:Yes|y|yes|Y)$')
rNo = re.compile(r'^(?:No|N|no|n)$')
yearOfBirth = int(input("Hello. What year were you born?: "))

while(True):
    birthday = input("Have you already had a birthday this year?: ")
    if re.search(rYes, birthday):
        print("You are", 2022 - yearOfBirth, "years old.")
        break
    elif re.search(rNo, birthday):
        print("You are", 2021 - yearOfBirth, "years old.")
        break
    else:
        print("Please write yes or no")