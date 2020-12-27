print("IMPLEMENTATION OF QUEUE")
s=[]
c="y"
while (c=='y'):
            print ("1. INSERT.")
            print("2. DELETE.")
            print("3. Display.")
            choice=int(input("Enter your Choice: "))
            if choice in range(1,4):
                if choice == 1:
                     a=input("Enter any no.: ")
                     s.append(a)
                elif choice==2:
                    if s==[]:
                        print("Queue is empty")
                    else:
                        print("Deleted element  is : ",s[0])
                        s.pop(0)
                elif choice==3:
                     l=len(s)
                     for i in range(0,l):
                         print(s[i])
                else:
                    print("WRONG INPUT")
            c=input("Do you want to continue or not? ")
