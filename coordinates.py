dir=input("enter directions")
l=dir.split(",")
x,y=0,0
n=[]
for i in range(len(l)):
    n.append(l[i][-1])
x=x+int(n[0])-int(n[1])
y=y+int(n[2])-int(n[3])
p=int((x**2+y**2)**(0.5))
print(p)

