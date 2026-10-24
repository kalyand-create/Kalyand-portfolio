nos=(input("enter the binary nos you want to enter"))
l=nos.split(",")
for i in l:
    binary=int(i,2)
    if binary%5==0:
        print(i)

    
