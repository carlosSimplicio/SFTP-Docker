from paramiko import SSHClient
from paramiko.client import AutoAddPolicy

import pgpy
from pgpy.constants import (
    PubKeyAlgorithm,
    KeyFlags,
    HashAlgorithm,
    SymmetricKeyAlgorithm,
    CompressionAlgorithm,
)


def generate_new_pgp_key():

    new_key = pgpy.PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 2048)
    uid = pgpy.PGPUID.new(
        'Carlos Simplicio', email='carlos.edsmoura@gmail.com'
    )
    new_key.add_uid(
        uid,
        usage={
            KeyFlags.Sign,
            KeyFlags.EncryptCommunications,
            KeyFlags.EncryptStorage,
        },
        hashes=[
            HashAlgorithm.SHA256,
            HashAlgorithm.SHA384,
            HashAlgorithm.SHA512,
            HashAlgorithm.SHA224,
        ],
        ciphers=[
            SymmetricKeyAlgorithm.AES256,
            SymmetricKeyAlgorithm.AES192,
            SymmetricKeyAlgorithm.AES128,
        ],
        compression=[
            CompressionAlgorithm.ZLIB,
            CompressionAlgorithm.BZ2,
            CompressionAlgorithm.ZIP,
            CompressionAlgorithm.Uncompressed,
        ],
    )

    with open('../server/pgp_key.asc', 'w') as f:
        f.write(str(new_key))

    with open('pgp_key_pub.asc', 'w') as f:
        f.write(str(new_key.pubkey))


def send_file():
    pgp_key, _ = pgpy.PGPKey.from_file('pgp_key_pub.asc')
    file_message = pgpy.PGPMessage.new('file_to_send.txt', file=True)
    encrypted_message = pgp_key.encrypt(file_message)
    with open('encrypted_file.txt', 'w') as f:
        f.write(str(encrypted_message))

    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy)
    client.connect(
        hostname='ssh-server',
        port=22,
        username='root',
        key_filename='ssh_key',
        look_for_keys=False,
        allow_agent=False,
    )
    with client.open_sftp() as sftp_client:
        sftp_client.put('encrypted_file.txt', './in/encrypted_file.txt')
    print('File Sent!!')


if __name__ == '__main__':
    # generate_new_pgp_key()
    send_file()
