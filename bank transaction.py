money=input("enter your money")
l=money.split(",")
bank=0
for i in l:
    if i[0]=="D":
        bank=bank+int(i[1:])
    elif i[0]=="W":
        bank=bank-int(i[1:])
print(bank)