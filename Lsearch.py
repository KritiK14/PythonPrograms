def lsearch(l,x):
    for i in range(len(l)):
        if (l[i]==x):
            return i+1
    return -1
