#Day 10 - Aditi Sai Sharma - June 12, 2026

def hello(to="troublemaker!"):
    print("hello,", to)

hello()

name = input("what is your name? ").title().strip()

hello(name)

purpose = input("what brings you here today? fun or work?")

if purpose == "fun":
    print("cool! lets play a game.")
else:
    print("oops! wrong answer. choose again")
    purpose = input("what brings you here today? fun or work?")
    

number = input("choose a number between 0-10")
if number >10:
    print("troublemaker! choose a number between 0-10")
elif number <0:
    print("nah ah! troublemaker, choose a number between 0-10")
elif number >=5:
    print("alright!")






