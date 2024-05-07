#криптосистема RSA
import random
def is_prime(n):
    for i in range(2,n):
        if (n % i) == 0:
            return False
    return True
def euler_func(p, q):
    return (p - 1) * (q - 1)
def extended_euclidean_algorithm(a, b):
    if a == 0 :
        return b, 0, 1
    gcd,x1,y1 = extended_euclidean_algorithm(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y
def modular_inverse(num, mod):
    return extended_euclidean_algorithm(num, mod)[1] % mod
def generate_keys(bit_length):
    half_bit_length = bit_length // 2
    while True:
        p = random.randint(2**(half_bit_length-1), 2**half_bit_length-1)
        if is_prime(p):
            break
    while True:
        q = random.randint(2**(half_bit_length-1), 2**half_bit_length-1)
        if is_prime(q) and p != q:
            break
    n = p * q
    phi = euler_func(p, q)
    while True:
        e = random.randint(3, phi - 1)
        if extended_euclidean_algorithm(e, phi)[0] == 1:
            break
    pub_key = (e, n)
    d = modular_inverse(e, phi)
    priv_key = (d, n)
    return pub_key, priv_key
def rsa_encrypt(public_key, plain_text):
    e, n = public_key
    return [pow(ord(char), e, n) for char in plain_text]
def rsa_decrypt(private_key, encrypted_text):
    d, n = private_key
    decrypted_text = [chr(pow(char, d, n)) for char in encrypted_text]
    return ''.join(decrypted_text)
keys = generate_keys(12)
initial_text = "HELLO WORLD"
encrypted_text = rsa_encrypt(keys[0], initial_text)
decrypted_text = rsa_decrypt(keys[1], encrypted_text)
print("Ключі - ", keys)
print("Початковий текст - ", initial_text)
print("Зашифрований текст - ", encrypted_text)
print("Розшифрований текст - ", decrypted_text)
