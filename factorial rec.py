def recur_fact(n):
        if (n==0):
                return 1
        elif (n==1):
                return n
        elif (n<0):
                return "Sorry, Factorial doesn't exist."
        else:
                return n*recur_fact(n-1)
