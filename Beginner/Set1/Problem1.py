#Code to check whether a number is positive,negative or zero with exceptional handling.
num = input()
try:
    n = int(num)
    if n==0:
        print("Zero")
    elif n>0:
        print("Positive")
    else:
        print("Negative")
except:
    print("Invalid Input")
