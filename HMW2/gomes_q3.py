yearOfBirth = int(input("Hello. What year were you born?: "))
birthday = input("Have you already had a birthday this year?: ")
if birthday == "Yes" or birthday == "yes" or birthday == "Y" or birthday == "y":
    print("You are", 2022 - yearOfBirth, "years old.")
elif birthday == "No" or birthday == "N" or birthday == "no" or birthday == "n":
    print("You are", 2021 - yearOfBirth, "years old.")
else:
    print("Please write yes or no")