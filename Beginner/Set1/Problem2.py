n = input()
if n.isdigit() and int(n)%2==0:
    print("Even")
elif n.isdigit():
    print("Odd")
else:
    print("invalid")
