print("IMPLEMENTATION OF STACK")
s=[]
c="y"
while (c=='y'):
            print ("1. PUSH.")
            print("2. POP.")
            print("3. Display.")
            choice=int(input("Enter your Choice: "))
            if choice in range(1,4):
                if choice == 1:
                     a=input("Enter any no.: ")
                     s.append(a)
                elif choice==2:
                    if s==[]:
                        print("Stack is empty")
                    else:
                        print("Deleted element  is : ",s.pop())
                elif choice==3:
                     l=len(s)
                     for i in range(l-1,-1,-1):
                         print(s[i])
                else:
                    print("WRONG INPUT")
            c=input("Do you want to continue or not? ")
               
               
