n = input()
li = 'aeiouAEIOU'
if len(n)>1 or n.isalpha()==False:
    print("invalid")
elif n in li:
    print("Vowel")
else:
    print("Consonant")
