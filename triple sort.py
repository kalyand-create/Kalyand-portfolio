t=input("enter details of people:")
l=t.split(",")
n,a,s=[],[],[]
n.extend(l[::3])
a.extend(l[1::3])
s.extend(l[2::3])
big=[]
for i in range(int(len(l)/3)):
    tup=()
    li=list(tup)
    li.append(n[i])
    li.append(a[i])
    li.append(s[i])
    tu=tuple(li)
    big.append(tu)
big.sort()
print(big)








