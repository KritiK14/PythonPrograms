def sumdigit(n):
    y=str(n)
    l=list(y)
    i=0
    s=0
    for i in y:
        i=int(i)
        s=s+i
    print("The sum is: ",s)
