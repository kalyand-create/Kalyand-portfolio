sample=input("enter some letters and words")
letters,numbers=0,0
for i in sample:
    if i.isdigit():
        numbers+=1
    elif i.isalpha():
        letters+=1
print("letters",letters,"numbers",numbers)
