# Subir tudo server e client
    `docker compose up`

# Acessar o client
    `docker exec -it ssh-client bash`

# Enviar o arquivo "file_to_send.txt" encriptado com a chave PGP pública para o server via SFTP
    `python send_file.py`

# Acessar o server
    `docker exec -it ssh-server bash`

# Descriptografar o arquivo recebido usando a chave PGP privada
    `python decrypt_file.py`

# O arquivo desencriptado estará em ./in
    `cat ./in/decrypted_file.txt`