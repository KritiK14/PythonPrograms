dn={}
n=int(input("How many names? "))
if (n>0):
    for i in range(1,n+1):
        name=input("Enter name: ")
        ph=int(input("Enter ph no.: "))
        dn[name]=ph
    m=input("Enter the name to be searched: ")
    if m in dn:
        print(dn[m])
    else:
        print("User not found")
else:
    print("invalid value")




                   
              
      
