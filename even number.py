for i in range(1000,3001):
    num=str(i)
    for j in num:
        if int(j)%2!=0:
            break
    else:
        print(i)
