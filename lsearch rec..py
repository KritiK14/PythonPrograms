def lsearch(l,x,i=0):
    if (i>len(l)):
        return -1
    else:
        if (x==l[i]):
            return i+1
    return lsearch(l,x,i+1)



























