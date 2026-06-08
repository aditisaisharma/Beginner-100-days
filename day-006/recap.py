#Day 6 - Aditi Sai Sharma - June 8, 2026

print("I'm going to figure it out, i always do")

purpose = input("why? ")

name  = input("whats your name? ")

print("was happeningggg, ", name)

for i in range(5):
    print("Aditi can do anything, she sets her mind to.")

print("hello, world")

name = name.capitalize()
print("hello,", name)

name = name.title()
print("hello,", name)

name = input("whats your name? ")
name = name.strip()
print("hello,", name)

first, middle, last = name.split(" ")
print("hello,", middle)

name = input("whats your name? ").strip().title()
print("hello,", name)

print("hello, " + first)

print("hello, ", name, sep=("*"))

print("hello, ", name, sep=("*"), end=("*"))

print("hello, 'friend'")

print("hello, \"friend\"")

print(f"hello, {name}")

def hello():
    print("hello")
hello()

def hello(to="world"):
    print("hello,", to)
hello(name)

def hello(to="world"):
    print("hello,", to)
name = input("whats your name? ")
hello(name)

def main():
    name = input("whats your name? ")
    hello(name)
    
def hello(to="world"):
    print("hello,", to)

main()

print("thankyou!", name)

