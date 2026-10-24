n=int(input("enter how many nos you want"))
import math
l=[]
for i in range(n):
    no=int(input("enter a number"))
    l.append(no)
for j in l:
    print(math.floor(((2*50*j)/20)**(0.5)))

   