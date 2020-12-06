import math
import random
import sys
import time
from Crypto.PublicKey import RSA
from random import randrange, getrandbits


def eratoSieve(n):
    primes = [] 
    multiples = []

    for i in range(2, n+1):
        if i not in multiples:
            primes.append(i)
            for j in range(i*i, n+1, i):
                multiples.append(j)

    x = [x for x in primes if n  / x in primes]

    return x[0]

def getPrimeFactors(n):
    while n % 2 == 0:
        primeFactors = 2
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            primeFactors = i
            n = int(n / i)

    if n > 2:
        primeFactors = n
    
    return primeFactors

def pollardRho(n): 
    if (n == 1): 
        return n 
  
    if (n % 2 == 0): 
        return 2
  
    x = (random.randint(0, 2) % (n - 2)) 
    y = x 
    c = (random.randint(0, 1) % (n - 1)) 
    d = 1

    while (d == 1): 
        x = (pow(x, 2, n) + c + n)%n 
        y = (pow(y, 2, n) + c + n)%n
        y = (pow(y, 2, n) + c + n)%n 
        d = math.gcd(abs(x - y), n)
        if (d == n): 
            return pollardRho(n)

    return d

def generate_RSA(bits):
    new_key = RSA.generate(bits, e=65537)
    public_key = new_key.publickey().exportKey("PEM") 
    private_key = new_key.exportKey("PEM") 

    print("\n", public_key)
    print("\n", private_key)
    print("\nn = ", new_key.n)
    print("\np = ", new_key.p)
    print("\nq = ", new_key.q)
    print("\ne = ", new_key.e)
    print("\nd = ", new_key.d)
    print("\nu = ", new_key.u)

def isPrime(n, k):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2

    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True
def generatePrimeCandidate(length):
    p = getrandbits(length)
    p |= (1 << length - 1) | 1
    return p

def generatePrimeNumber(length):
    p = 4

    while not isPrime(p, 256):
        p = generatePrimeCandidate(length)
    return p

def multipliInverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi

def generatePrivKey(p, q, e):

    n = p * q

    phi = (p - 1) * (q - 1)

    g = math.gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = math.gcd(e, phi)

    d = multipliInverse(e, phi)

    return d

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def decimalToBinary(n):  
    return bin(n).replace("0b", "") 

def chooseOption():
    print("\n\n 1 - Generate both keys by provided \
libraries Crypto and show all components\n \
including prime numbers")
    print("\n 2 - Generate modulus n with smaller \
key size and actually decrypt n to two\n \
prime number factors p and q")
    print("\n 3 - Show credits")
    print("\n 4 - Exit program\n")

    option = input(" -> Choose 1, 2, 3 or 4 and \
write as number: ")

    if option == "1":
        option1()

    elif option == "2":
        while True:
            try:
                bits = int(input("\n -> Choose key \
 length in bits (at least 16) and write as integer"  
" (128)\n   or 1 to return: "))
                if(bits == 1):
                    chooseOption()
                elif(bits >= 16):
                    break
                else:
                    print("\nThat was no valid \
integer greater then 16!")
            except ValueError:
                print("\nThat was no valid integer \
greater then 16!")

        option2(bits)

    elif option == "3":
        credits()
    elif option == "4":
        sys.exit()
    else:
        print("\n\n\n\n    Wrong character!")
        chooseOption()

def option1():
    print("\n\n Choose key length in bits:")
    print("\n 1 - 1024b\n 2 - 2048b\n 3 - 3072b\n\
 4 - Return")

    option = input("\n -> Choose option of key \
length and write as number: ")

    if option == "1":
        generate_RSA(bits=1024)
    elif option == "2":
        generate_RSA(bits=2048)
    elif option == "3":
        generate_RSA(bits=3072)
    elif option == "4":
        chooseOption()
    else:
        print("\n\n    Wrong character!")
        option1()

def option2(bits):
    if(bits % 2 == 0):
        p = generatePrimeNumber(int((bits/2)+3))
        q = generatePrimeNumber(int((bits/2)-3))
    else:
        p = generatePrimeNumber(int((bits/2)+4))
        q = generatePrimeNumber(int((bits/2)-3))
    
    if(len(str((decimalToBinary(p*q)))) == bits):
        option21(p, q)
                
    else:
        option2(bits)
    
def option21(p,q):
    n = p * q
    (p-1) * (q-1)
    e = random.randint(1, lcm((p-1),q-1))

    print("\n Randomly generated components: ")
    print("\n n = ", n)
    print("\n e = ", e)
    print("\n p = ", p)
    print("\n q = ", q)
    print("\n\n 1 - Pollard's Rho algorithm")
    print("\n 2 - Sieve of Eratosthenes")
    print("\n 3 - Brute force algorithm")

    option = input("\n -> Choose algorithm which \
you prefer to factorize n and write it as number: ")

    if option == "1":
        p1 = pollardRho(n)        
        q1 = int(n / p1)
        if(p1 > q1):
            p = p1
            q = q1
        else:
            p = q1
            q = p1

        print("\n d = ", generatePrivKey(p, q, e))
        print("\n p = ", p)
        print("\n q = ", q)

    elif option == "2":
        q = eratoSieve(n)
        p = int(n / q)

        print("\n d = ", generatePrivKey(p, q, e))
        print("\n p = ", p)
        print("\n q = ", q)

    elif option == "3":
        p = getPrimeFactors(n)
        q = int(n / p)

        print("\n d = ", generatePrivKey(p, q, e))
        print("\n p = ", p)
        print("\n q = ", q)

    else:
        print("\n\n    Wrong character!")
        option21()
        
def credits():
    print("\n\n", 79*"=")
    print("\n",28*"="," Applied Cryptography ",27*"=")
    print("\n",23*"="," RSA Communication Breach Tool ",23*"=")
    print("\n", 79*"=")
    print("\n\n",34*" ","Tomáš Glos")
    print("\n",33*" ","Alois Kunert")
    print("\n",33*" ","Tomáš Závada")
    print("\n",34*" ","Jakub Volf")
    print("\n\n", 79*"=")
    print("\n",33*"="," 2020/2021 ",33*"=")
    print("\n",79*"=")

    time.sleep(5)
    chooseOption()


if __name__ == '__main__':
    
    print("\n\n\n\n", 79*"=")
    print("\n", 23*"=", " RSA Communication Breach Tool ", 23*"=")
    print("\n", 79*"=")
    
    chooseOption()

    print("\n\n", 79*"=")
    print("\n",36*"=", " END ", 36*"=")
    print("\n",79*"=")
