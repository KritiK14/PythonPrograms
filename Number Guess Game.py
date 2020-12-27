import random
x=random.randrange(50,1001)
s=int(input("enter a no. between 50-1000  "))
if s==x:
    print("CONGRATULATIONS YOU'VE GUESSED RIGHT")
elif s>x:
    print(""" BOOOO! BUT YOU'VE GOT ANOTHER CHANCE , 
              ENTER AGAIN
              HINT: THE NO. IS LESS THAN WHAT YOU HAVE ASSUMED"""  )
elif s<x:
    print(""" BOOOO! BUT YOU'VE GOT ANOTHER CHANCE ,
            ENTER AGAIN,    
          HINT: THE NO. IS MORE THAN WHAT YOU HAVE ASSUMED """ )
n=int(input("enter the no  "))
R1=x-10
R2=x+10
if n==x:
    print("CONGRATULATIONS YOU'VE GUESSED RIGHT")
elif n>R2:
    print("you are far try less than", R2)
elif n<R1:
    print("you are far try more than", R1)
elif  n>R1 and n<R2:
    print("you are closer")
o=int(input("enter a no   "))
if o==x:
    print("CONGRATULATIONS YOU'VE GUESSED RIGHT")
else:
    print("""SORRY YOU LOST HEHE
              the answer is """ ,x)
    
    
    
