# Python Module for Encryption and Decryption by RSA Algorithm

import primes
from random import choice

def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

def modinv(phi, m):
    for x in range(1, m):
        if (phi * x) % m == 1:
            return x
    return None

def coprimes(phi):
    l = []
    for x in range(2, phi):
        if gcd(phi, x) == 1 and modinv(x, phi) != None:
            l.append(x)
        if len(l) > 5: break
    for x in l:
        if x == modinv(x, phi):
            l.remove(x)
    return l

def key_generator():
    p, q = primes.choose_distinct_primes()
    n = p * q
    phi = (p-1) * (q-1)  # Euler's function (totient)
    e = choice(coprimes(phi))
    d = modinv(e, phi)
    
    public_key = [e, n]
    private_key = [d, n]
    return [public_key, private_key]


def encrypt_block(m, e, n):
    c = (m**e) % n
    return c

def decrypt_block(c, d, n):
    m = (c**d) % n
    return m

# method for encryption of a message
def encrypt_string(s, public_key):
    e, n = public_key
    return ''.join([chr(encrypt_block(ord(x), e, n)) for x in list(s)])

# method for decryption of a message
def decrypt_string(s, private_key):
    d, n = private_key
    return ''.join([chr(decrypt_block(ord(x), d, n)) for x in list(s)])

