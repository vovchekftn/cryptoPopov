import random
import pickle

# Функція для збереження ключів RSA у файл
def save_keys(public_key, private_key, public_key_file="public_key2.pem", private_key_file="private_key2.pem"):
    with open(public_key_file, "wb") as f:
        pickle.dump(public_key, f)
    with open(private_key_file, "wb") as f:
        pickle.dump(private_key, f)
    print("Keys saved successfully.")

# Функція для завантаження ключів RSA з файлу
def load_keys(public_key_file="public_key.pem", private_key_file="private_key.pem"):
    try:
        with open(public_key_file, "rb") as f:
            public_key = pickle.load(f)
        with open(private_key_file, "rb") as f:
            private_key = pickle.load(f)
        print("Keys loaded successfully.")
        return public_key, private_key
    except FileNotFoundError:
        print("Key files not found.")
        return None, None

# Функція для знаходження найбільшого спільного дільника
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Функція для знаходження оберненого елемента за модулем
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Функція для перевірки числа на простоту
def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    for _ in range(k):
        a = random.randint(2, n - 1)
        if pow(a, n - 1, n) != 1:
            return False
    return True

# Генерація великого простого числа
def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num

# Генерація ключів RSA
def generate_rsa_keys(bits):
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(1, phi)
    while gcd(e, phi) != 1:
        e = random.randint(1, phi)
    d = mod_inverse(e, phi)
    return (e, n), (d, n)

# Функція для підпису повідомлення
def sign(message, private_key):
    d, n = private_key
    signature = pow(message, d, n)
    return signature

# Функція для перевірки підпису
def verify(message, signature, public_key):
    e, n = public_key
    decrypted_signature = pow(signature, e, n)
    return decrypted_signature == message

def save_signature(signature, signature_file="signature.dat"):
    with open(signature_file, "wb") as f:
        pickle.dump(signature, f)
    print("Signature saved successfully.")

def load_signature(signature_file="signature.dat"):
    try:
        with open(signature_file, "rb") as f:
            signature = pickle.load(f)
        print("Signature loaded successfully.")
        return signature
    except FileNotFoundError:
        print("Signature file not found.")
        return None


# Приклад використання
if __name__ == "__main__":
    # Генеруємо ключі RSA з 1024 бітами
    # public_key, private_key = generate_rsa_keys(1024)
    
    # Зберігаємо ключі у файли
    # save_keys(public_key, private_key)
    
    # Завантажуємо ключі з файлів
    loaded_public_key, loaded_private_key = load_keys("public_key.pem", "private_key.pem")
    # Для не валідації
    # loaded_public_key, loaded_private_key = load_keys("public_key2.pem", "private_key.pem")

    # Повідомлення, яке буде підписане
    message = 12345

    # Підписуємо повідомлення приватним ключем
    # signature = sign(message, loaded_private_key)
    # save_signature(signature)

    signature = load_signature()

    # Перевіряємо підпис за допомогою публічного ключа
    print("Signature is valid:", verify(message, signature, loaded_public_key))
