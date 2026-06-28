#Day 26 - Aditi Sai Sharma - June 28, 2026

#Calculator
  
#Program 1
print(1+2)

#Strings concantate to 12
print("1"+"2")

#Program 3  3 variables
x = input("whats x? ")
y = input("whats y? ")
z=x+y
print(z)

#Program 4 2 variables

print(x+y)

#Program 5  all in one
print(int(input("whats x? ")) + int(input("whats y? ")))

#Program 6 Floats(decimal) and round off
x = float(input("whats x? "))
y = float(input("whats y? "))
z = round(x+y)
print(z)

#Program 7 adding commas in numbers using f string
x = float(input("whats x? "))
y = float(input("whats y? "))
z = round(x+y)
print(f"{z:,}")

#Program 8 division
x = float(input("whats x? "))
y = float(input("whats y? "))
z = x/y
print(z)

#Program 9 division and round off

z = round(x/y, 2)
print(z)

#Program 10 round off 2nd approach

z = x/y
print(f"{z:.2f}")

#Program 11 multiplication
x = float(input("whats x? "))
y = float(input("whats y? "))
z = x*y
print(f"{z:.2f}")

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
