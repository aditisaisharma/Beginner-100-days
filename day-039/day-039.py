#Day 39 - Aditi Sai Sharma - July 11, 2026

#boolean value - True/False (capital T and capital F)
print("hi")   

def main():
    x = int(input("whats x? "))
    if is_even(x):
        print("even")
    else:
        print("odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()
