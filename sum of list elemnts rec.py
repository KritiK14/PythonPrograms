n=int(input("Enter the no. of elements: "))
l=[]
for i in range(0,n):
    x=int(input("Enter the element: : "))
    l.append(x)
print(l)

def suml(l,m=len(l)):
    if (len(l)==1):
        return l[0]
    elif(len(l)==0):
        return 0
    else:
        return l[0]+suml(l[1: ],m)
print("The sum of all the elements of the list is: ",suml(l))
