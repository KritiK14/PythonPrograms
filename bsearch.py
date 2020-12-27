def bsearch(L,t,f=0,l=0):
    l=len(L)
    while (f<=l):
        mid=(f+l)//2
        if(L[mid]<t):
            f=mid+1
        elif(L[mid]>t):
            l=mid-1
        else:
            return mid
    return -1
