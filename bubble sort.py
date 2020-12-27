def bubble():
    y=[]
    m=int(input("Enter the amount of numbers to sort: "))
    for x in range(m):
        x=int(input("Enter the Number: "))
        y.append(x)
    n=len(y)
    for i in range(n-1):
        for j in range (n-i-1):
            if y[j]>y[j+1]:
                y[j],y[j+1]=y[j+1],y[j]
    print("The sorted list is: ",y)
bubble()

