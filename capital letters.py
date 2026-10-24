lines=[]
while True:
    line=input("enter a sentence")
    if line:
        lines.append(line.upper())
    else:
        break
    
for i in lines:
    print(i)

