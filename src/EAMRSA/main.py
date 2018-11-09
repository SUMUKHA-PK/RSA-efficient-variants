import math 
import numpy as np
import sys
import os
import random
sys.path.append((os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir))))
# print(sys.path)
from check_prime import check_prime
from inverse import multiplicative_inverse


#Taking user input for security parameters. These can also be defined for each test case separately
# n = int(input('Enter the security parameter \'n\': '))
# b = int(input('Enter the value of parameter \'b\': '))
# k = int(input('Enter the value of parameter \'k\': '))
# c = int(input('Enter the value of parameter \'c\': '))


def run(n,k,b,c,pt):

    def exponent(a,b,c):
        a=a%c
        temp = 1
        for i in range(b):
            temp = temp * a
            temp%=c
        return temp

    # Eulers phi function
    def phi(arr):
        N = 1 
        for i in arr:
            N*=(i-1)
        return N

    bits_len = n//b

    max_val = pow(2,bits_len)-1


    primes_p = []  # List for the 'b' primes

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

    print('phi(N) = ',end="")
    print(phi(primes_p))

    #Fixed constant co-prime to (primes-1)
    E = 65537

    #Vectors holding the public and private keys
    e = np.zeros(shape=(b*k),dtype=int)
    d = np.zeros(shape=(b*k),dtype=int)

    D = multiplicative_inverse(E,phi(primes_p))

    print('Value of d is : ',end="")
    print(D)

    # List for the values of 'r' = D mod(primes-1)
    r = np.zeros(b,dtype=int)

    for i in range(b):
        r[i] = D % (primes_p[i]-1)
    print("Array r: ")
    print(r)

    #Generation of the public and private keys
    for i in range(b):
        for j in range(k-1):
            y = random.randint(0,pow(2,n))
            e[i*k +j] = y
    
    for i in range(b):
        for j in range(k-1):
            y = random.randint(0,pow(2,c))
            d[i*k +j] = y
    
    print("Array d: ") 
    print(d)

    print("Array e: ")
    print(e)

    # List to adjust the conditions of the generated lists of priv and pub keys
    product = np.zeros(shape=(b*k),dtype=int)

    for i in range(b):
        for j in range(k-1):
            product[i*k+j] = (e[i*k +j]*d[i*k +j])

    for i in range(b):
        temp_sum = 0 
        for j in range(k):
            temp_sum +=product[i*k +j]
        for kk in range(sys.maxsize):
            if(r[i]==((temp_sum + kk)%(primes_p[i]-1))):
                temp_val = kk
                break
        product[i*k + k-1] = temp_val
   
    print("Array product: ")
    print(product)

    for i in range(b):
        e[i*k +k-1] = 1
        d[i*k +k-1] = product[i*k+k-1]

    print("Array d: ") 
    print(d)

    print("Array e: ")
    print(e)

    # p_text = input("Enter the plain text message: ")
    p_text = pt
    cipher_text = [(ord(char) ** E) % (N) for char in p_text]

    print("Plain text is ",end="--> ")
    print(p_text)
    print("The cipher text is: ",end="--> ")
    print(cipher_text)

    cipher_text_message = np.zeros(shape=((b*k),len(cipher_text)),dtype=int)  # Z

    for i in range(b):
        for j in range(k):        
            for kk in range(len(cipher_text)):
                cipher_text[kk]%=N
                cipher_text_message[i*k + j][kk] = (exponent(cipher_text[kk],e[i*k +j],N)) 
                cipher_text_message[i*k + j][kk]%=N

    print("Cipher text message is: ",end="--> ")
    print(cipher_text_message)

    #Decryption begins

    y = np.zeros(shape=(b),dtype=int)

    for i in range(b):
        y[i] = N / primes_p[i]
    
    print("The list y : ",end = "-->")
    print(y)

    y_inverse = np.zeros(shape=(b),dtype=int)

    for i in range(b):
        y_inverse[i] = multiplicative_inverse(y[i],primes_p[i])
    
    print("The list y inv : ",end = "-->")
    print(y_inverse)
    
    n_vec = np.zeros(shape=(b),dtype=int)

    for i in range(b):
        n_vec[i] = y[i]*y_inverse[i]
    
    print("The list nvec : ",end = "-->")
    print(n_vec)

    M = np.zeros(shape=((b),len(cipher_text)),dtype=int)

    for kk in range(len(cipher_text)):
        for i in range(b):
            temp = 1
            for j in range(k):
                temp = temp * exponent(cipher_text_message[i*k+j][kk],d[i*k+j],primes_p[i])
                temp = temp % (primes_p[i])
            M[i][kk] = temp
    
    print("The array M: ")
    print(M)

    mess_vec = np.zeros(shape=(len(cipher_text)),dtype=int)

    for i in range(len(cipher_text)):
        temp = 0
        for j in range(b):
            temp = temp + M[j][i]*n_vec[j]
        mess_vec[i] = temp
    
    print("The list messvec : ",end = "-->")
    print(mess_vec)

    decrypted_data = [chr(char % N) for char in mess_vec]

    print(decrypted_data)

# run(n,k,b,c)

