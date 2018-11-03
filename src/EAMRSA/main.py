import math 
import numpy as np
import sys
import os
import random
sys.path.append((os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir))))
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)))+"\\BMRSA")
print(sys.path)
from check_prime import check_prime
from inverse import multiplicative_inverse
from crt import crt

print(crt(2,3))
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

    e = np.zeros(shape=(b*k),dtype=int)
    d = np.zeros(shape=(b*k),dtype=int)

    D = multiplicative_inverse(E,phi(primes_p))

    print('Value of d is : ',end="")
    print(D)

    r = np.zeros(b)

    for i in range(b):
        r[i] = D % (primes_p[i]-1)
    print("Array r: ")
    print(r)

    for i in range(b):
        for j in range(k-1):
            y = random.randint(0,pow(2,n))
            e[i*k +j] = y
    
    for i in range(b):
        for j in range(k-1):
            y = random.randint(0,pow(2,c))
            d[i*k +j] = y
    
    product = np.zeros(shape=(b*k),dtype=int)

    for i in range(b):
        for j in range(k):
            product[i*k+j] = (e[i*k +j]*d[i*k +j])%(primes_p[i] - 1)

    for i in range(b):
        temp_sum = 0 
        for j in range(k):
            temp_sum +=product[i*k +j]
        for kk in range(sys.maxsize):
            if(r[i]==((temp_sum + kk)%(primes_p[i]-1))):
                temp_val = kk
                break
        product[i*k + k-1] = temp_val
   
    print("Array d: ") 
    print(d)

    print("Array e: ")
    print(e)

    print("Array product: ")
    print(product)

    for i in range(b):
        y = random.randint(0,pow(2,n))
        e_rand = y
        e[i*k +k-1] = e_rand
        d[i*k +k-1] = multiplicative_inverse(e_rand,(primes_p[i]-1))

    print("Array d: ") 
    print(d)

    print("Array e: ")
    print(e)

    p_text = input("Enter the plain text message: ")

    cipher_text = [(ord(char) ** E) % (N) for char in p_text]

    print("Plain text is ",end="--> ")
    print(p_text)
    print("The cipher text is: ",end="--> ")
    print(cipher_text)

    # for i in range(b):
    #     for i in range(k):
            
    cipher_text_message = np.zeros(shape=((b*k),len(cipher_text)),dtype=int)  # Z

    for i in range(b):
        for j in range(k):        
            for kk in range(len(cipher_text)):
                cipher_text[kk]%=N
                cipher_text_message[i*k + j][kk] = ((cipher_text[kk])**e[i*k +j]) 
                cipher_text_message[i*k + j][kk]%=N

    print("Cipher text message is: ",end="--> ")
    print(cipher_text_message)



run(n,k,b,c)

