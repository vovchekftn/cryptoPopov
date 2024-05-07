import random
import math

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def generate_prime():
    while True:
        num = random.randint(100, 1000)
        if is_prime(num):
            return num

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_keys():
    p = generate_prime()
    q = generate_prime()
    n = p * q
    phi = (p - 1) * (q - 1)

    while True:
        e = random.randint(2, phi - 1)
        if gcd(e, phi) == 1:
            break

    d = mod_inverse(e, phi)

    return ((e, n), (d, n))

def encrypt(message, public_key):
    e, n = public_key
    encrypted_msg = [pow(ord(char), e, n) for char in message]
    return encrypted_msg

def decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted_msg = [chr(pow(char, d, n)) for char in encrypted_message]
    return ''.join(decrypted_msg)

message = "Encrypted message"
public_key, private_key = generate_keys()
encrypted_message = encrypt(message, public_key)
print("Encrypted message:", encrypted_message)
decrypted_message = decrypt(encrypted_message, private_key)
print("Decrypted message:", decrypted_message)
