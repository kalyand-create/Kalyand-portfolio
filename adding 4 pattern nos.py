#easier way
no=int(input("enter the number you want to add"))
sum=0
summ=0
for i in range(4):
    sum=(sum*10)+no
    summ+=sum
print(summ)


#easy way
no=int(input("enter the number you want to add"))
sum=0
for i in range(1,5):
    sum=sum+((5-i)*(no)*(10**(i-1)))
print(sum)







