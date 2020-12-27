def bsearch(L,t,f=0,l=0):
    l=len(L)
    if (f>l):
        return -1
    if (l==0):
        l=len(L)
    mid=(f+l)//2
    if(L[mid]<t):
        return bsearch (L,t,mid+1,l)
    if(L[mid]>t):
        return bsearch(L,t,f,mid-1)
    else:
        return mid

