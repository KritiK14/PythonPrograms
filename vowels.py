str=input("enter a string= ")
count=0
vowels='aAeEIioOuU'
for ctr in str:
    if ctr in vowels:
        count=count+1
if count>0:
    print("No. of vowels are ",count)
else:
    print("no vowels")
    
