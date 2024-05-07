def encrypt(message, key):
    key_binary = ''.join([format(ord(char), '08b') for char in key])
    ciphertext = ''
    for i in range(len(message)):
        message_char_binary = format(ord(message[i]), '08b')
        result = ''
        for j in range(8):
            result += str(int(message_char_binary[j]) ^ int(key_binary[j]))
        ciphertext += chr(int(result, 2))
    return ciphertext

def decrypt(ciphertext, key):
    key_binary = ''.join([format(ord(char), '08b') for char in key])
    decrypted_message = ''
    for i in range(len(ciphertext)):
        ciphertext_char_binary = format(ord(ciphertext[i]), '08b')
        result = ''
        for j in range(8):
            result += str(int(ciphertext_char_binary[j]) ^ int(key_binary[j]))
        decrypted_message += chr(int(result, 2))
    return decrypted_message


try:
    with open("text.txt") as file:
        message = file.read()
    with open("key.txt") as file:
        key = file.read()

    if len(message) != len(key):
        raise ValueError("Length of message and key must be the same")

    print("Key:", key)

    encrypted_message = encrypt(message, key)
    print("Encrypted text:", encrypted_message)

    decrypted_message = decrypt(encrypted_message, key)
    print("Decrypted text:", decrypted_message)

    with open("result.txt", 'w', encoding='utf-8') as output_file:
        output_file.write(f"Original Text: {message}\n")
        output_file.write(f"Encrypted Text: {encrypted_message}\n")
        output_file.write(f"Decrypted Text: {decrypted_message}\n")

except ValueError as e:
    print(f"Error: {e}")
