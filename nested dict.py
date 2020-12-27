n=int(input("Enter the value for n: "))
d1={}
dv={}
for i in range (0,n):
    k=input("Enter key: ")
    v1=input("Enter Address: ")
    v2=input("Enter phone number: ")
    v3=input("Enter email: ")
    dv={'address':v1,'phone number':v2,'email':v3}
    d1[k]=dv
    

print(d1)
    
