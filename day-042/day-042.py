#Day 42 - Aditi Sai Sharma - July 14, 2026

#bugged

score = input("whats your score from 0-100? ").strip()

if score >=0:
    float(score)
elif score <=100:
    float(score)


def grade(score):

    if score >=90:
        print("A")
    elif score >=80:
        print("B")
    elif score >=70:
        print("C")
    elif score >=60:
        print("D")
    elif score >=0:
        print("F")
    elif score >100:
        print("Please put a score between 0-100", grade(score), sep="$")
    elif score <0:
        print("Please put a score between 0-100", grade(score), sep="$")
    else:
        print("That's not a number.", grade(score), sep="$")


grade(score)
