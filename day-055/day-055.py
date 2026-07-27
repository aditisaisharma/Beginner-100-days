#Day 55 - Aditi Sai Sharma - July 27, 2026

#defining functions
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
