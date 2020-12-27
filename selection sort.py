def selection(a):
    n=len(a)
    for i in range (n):
        minpos=i
        for j in range(i+1,n):
            if a[minpos]>a[j]:
                minpos=j
                a[minpos],a[i]=a[i],a[minpos]
    print(a)
            
