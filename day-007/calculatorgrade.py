#Day 7 - Aditi Sai Sharma - June 9, 2026

#addition (or subtraction, division, multiplication)
x = 9 #or x = float(input("whats x? "))
y = 5.4646465678 #or y = float(input("whats y? "))
z = (x+y)
print(z)

print(f'{z:.5f}') #round using f-string

def main():
    print("x to the power y is ", pow(x ,y))
main()

def calc():
    print("x squared is ", square(x))

def square(n):
    return n*n
calc()

def rec():
    print("sqaureroot of x is ", root(x))
def root(n):
    return pow(n ,1/2)
rec()

# GRADE CALCULATOR:

score = float(input("what is your score in the range 0-100? "))


def grade(score):
    if score >=90:
        print("A")
    elif score >=80:
        print("B")
    elif score >=70:
        print("c")
    elif score >=60:
        print("D")
    else: print("F")


grade(score)

