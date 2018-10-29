import math 

n = int(input('Enter the security parameter \'n\': '))
b = int(input('Enter the value of parameter \'b\': '))
k = int(input('Enter the value of parameter \'k\': '))
c = int(input('Enter the value of parameter \'c\': '))

bits_len = n//b

max_val = pow(2,bits_len)-1

def check_prime(a):
    flag=1
    if(a==1):
        flag=0
    else:
        for i in range(2,math.ceil(math.sqrt(a))+1):
            if(a%i==0):
                flag=0
    return flag

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

e = 65537

def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1* x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    return d + phi

d = multiplicative_inverse(e,phi(primes_p))

print('Value of d is : ',end="")
print(d)