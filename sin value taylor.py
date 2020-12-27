import math
def sin(x,n):
    sine = 0
    for i in range(n):
        sign = (-1)**i
        pi=22/7
        y=x*(pi/180)
        sine = sine + ((y**(2.0*i+1))/math.factorial(2*i+1))*sign
    return sine
x=int(input("Enter the value of x in degrees:"))
n=int(input("Enter the number of terms:"))
p=round(sin(x,n),2)
print("Value of sin",x,"is: ",p)

a=math.pi
b=a/180
y=x*b
q=round(math.sin(y),2)
print("Value of sin",x,"through math module is: ",q)

if p==q:
    print("The calculated value is correct'")
else:
    print("The value is incorrect.")


