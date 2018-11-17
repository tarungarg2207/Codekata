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
