def fact(n):
    p=1
    for i in range(1,n+1):
        p=p*i
    print("Factorial of the no. is: ",p)

n=int(input("Enter a no.: "))
fact(n)

