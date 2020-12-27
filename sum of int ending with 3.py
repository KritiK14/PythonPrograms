def listsum(l):
     n=0
     for i in range(0,len(l)):
         if (l[i]%10==3):
             n=n+l[i]
     print("The sum of all integers ending with 3 is: ",n)

p=int(input("Enter the no. of elements: "))
l=[]
for i in range(0,p):
    x=int(input("Enter the element: : "))
    l.append(x)
print(l)
listsum(l)
            
