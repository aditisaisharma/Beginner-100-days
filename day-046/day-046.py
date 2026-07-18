#Day 46 - Aditi Sai Sharma - July 18, 2026

def hello():
    print("hello")

name = input("whats your name?" ) 
hello()
print(name)

#2 hello, to - name same line
def hello(to):
    print("hello,", to)

name = input("whats your name? ")
hello(name)

#3 default value
def hello(to="world"):
    print("hello,", to)

hello()
name = input("what is your name? ")
hello(name)

#defining and calling fx
def main():
    name = input("whats your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()

#Scope - refers to a variable only existing in the context in which you defined it.
#Calculator.py - square

def main():
    x = int(input("whats x? "))
    print("x squared is", square(x))

def square(n):
    return n*n

main()

#exponential power

def main():
    x = int(input("whats x? "))
    n = int(input("whats n? "))
    print("x to the power n is,", pow(x, n) )

main()