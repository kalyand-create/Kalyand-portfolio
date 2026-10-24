r=int(input("no of rows"))
c=int(input("enter no of columns"))
array=[]


for i in range(r):
    row=[]
    for j in range(c):
        row.append(i*j)
    array.append(row)          
print(array)