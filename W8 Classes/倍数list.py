def mysum(a,b,limit):
    sum=0
    ls=[]
    if type(a) == int and type(b) == int and a>0 and b>0:
        for i in range(1,limit):
            if a*i<limit:
                sum+=a*i
                ls.append(a*i)
        for i in range(1,limit):
            if b*i<limit and b*i not in ls:
                sum+=b*i
        return sum

    else:
        return 'Wrong input'
    
print mysum(2,4,12)

