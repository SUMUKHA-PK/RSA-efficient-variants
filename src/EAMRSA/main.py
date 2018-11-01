import math 
import numpy as np
import sys
import os
import random
sys.path.append((os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir))))
from check_prime import check_prime
from inverse import multiplicative_inverse

#Taking user input for security parameters. These can also be defined for each test case separately
n = int(input('Enter the security parameter \'n\': '))
b = int(input('Enter the value of parameter \'b\': '))
k = int(input('Enter the value of parameter \'k\': '))
c = int(input('Enter the value of parameter \'c\': '))


def run(n,k,b,c):
    bits_len = n//b

    max_val = pow(2,bits_len)-1


    primes_p = []

    for i in range(2,max_val+1):
        if(check_prime(i)):
            primes_p.append(i)

    j = 0 
    l = len(primes_p)

    while(j!=(l-b)):
        primes_p.remove(primes_p[0])
        j+=1

    print('\'b\' primes of bit length floor(n/b) are: ',end="")
    print(primes_p)

    N = 1

    for i in primes_p:
        N*=i

    print('Product of floor(n/b) primes are: ',end="")
    print(N)

    def phi(arr):
        N = 1 
        for i in arr:
            N*=(i-1)
        return N

    print('phi(N) = ',end="")
    print(phi(primes_p))

    E = 65537

    e = np.zeros(shape=(b,k))
    d = np.zeros(shape=(b,k))

    D = multiplicative_inverse(E,phi(primes_p))

    print('Value of d is : ',end="")
    print(D)

    r = np.zeros(b,dtype=int)

    for i in range(b):
        r[i] = D % (primes_p[i]-1)
    print("Array r: ",end="")
    print(r)

    for i in range(b):
        for j in range(k-1):
            e[i][j] = random.randint(0,sys.maxsize)
    
    for i in range(b):
        for j in range(k-1):
            d[i][j] = random.randint(0,sys.maxsize)
    
    product = np.zeros(shape=(b,k),dtype=int)

    for i in range(b):
        for j in range(k):
            product[i][j] = (e[i][j]*d[i][j])%(primes_p[i] - 1)

    for i in range(b):
        temp_sum = 0 
        for j in range(k):
            temp_sum +=product[i][j]
        for kk in range(sys.maxsize):
            if(r[i]==((temp_sum + kk)%(primes_p[i]-1))):
                temp_val = kk
                break
        product[i][k-1] = temp_val
     
    print(d)

    print(e)

    print(product)

    p_text = input("Enter the plain text message: ")

    cipher_text = [(ord(char) ** E) % (N) for char in p_text]

    print("Plain text is ",end="--> ")
    print(p_text)
    print("The cipher text is: ",end="--> ")
    print(cipher_text)

    # for i in range(b):
    #     for i in range(k):
            
    cipher_text_message = np.zeros(shape=(b,k))  # Z

    for i in range(b):
        for j in range(k):
            cipher_text_message[i][j] = (cipher_text[j]**e[i][j]) % N 

    print("Cipher text message is: ",end="--> ")
    print(cipher_text_message)



run(n,k,b,c)

