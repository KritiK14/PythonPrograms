def summ(n):
    if (n==1):
        return 1
    else:
        return n+summ(n-1)

x=int(input("Enter a no. to claculate the sum of 'n' integers: "))
print(summ(x))
