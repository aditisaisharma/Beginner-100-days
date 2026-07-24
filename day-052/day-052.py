#Day 52 - Aditi Sai Sharma - July 24, 2026

print("hi")
score = int(input("score(0-100): "))


def calcgrade(score):
    if score >= 90 and <= 100:
        print("A: PASS!")
    elif score >=80:
        print("B: PASS!")
    elif score>=70:
        print("C: PASS!")
    elif score >=60:
        print("D: PASS!")
    elif score >=0:
        print("F: FAIL!")
    else:
        ("error: invalid score.")

calcgrade(score)