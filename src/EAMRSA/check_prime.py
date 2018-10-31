import math

def check_prime(a):
# Function to check whether a given number is prime or not
    flag=1
    if(a==1):                                             # If the number is 1, it is not prime
        flag=0
    else:
        # Standard algorithm for finding whether a number is prime or not, using modulo until its square root and eliminating possibility if its divisble
        for i in range(2,math.ceil(math.sqrt(a))+1):      
            if(a%i==0):
                flag=0
    return flag
