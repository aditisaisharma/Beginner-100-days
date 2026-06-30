#Day 28 - Aditi Sai Sharma - June 30, 2026

#match:

name = input("what is your name? ")

match name:
    case "amby":
        print("sea blue green")
    case "lilly" | "aditi" | "karim":
        print("brown")
    case "carter":
        print("brown")
    case "ella":
        print("blue")
    case _:
        print("who?")
    