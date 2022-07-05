import pgpy


def decrypt_message():
    pub_key, _ = pgpy.PGPKey.from_file('pgp_key.asc')
    encrypted_message = pgpy.PGPMessage.from_file('./in/encrypted_file.txt')
    with open('./in/decrypted_file.txt', 'w') as f:
        decrypted_message = pub_key.decrypt(encrypted_message)
        f.write(decrypted_message.message)

if __name__ == '__main__':
    decrypt_message()