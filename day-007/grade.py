#Day 7 - Aditi Sai Sharma - June 9, 2026

#GRADE CALCULATOR

score = float(input("what is your score in the range 0-100? "))


def grade(x):
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