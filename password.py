pwd=input("enter the passwords")
p=pwd.split(",")
l=[]

for i in p:
     i=i.strip()
     if  len(i)<6 or len(i)>12:
            continue
     up,low,no,ch=0,0,0,0
     for j in i:
         if j.isupper():
               up+=1
         elif j.islower():
            low+=1
         elif j.isdigit():
            no+=1
         elif j in "$#@":
            ch+=1
     if up>0 and low>0 and no>0 and ch>0:
        l.append(i)
print(l)
    
