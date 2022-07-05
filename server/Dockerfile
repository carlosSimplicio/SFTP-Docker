FROM python:latest

RUN apt-get update && apt-get install -y openssh-server python3-pgpy

WORKDIR /root

RUN mkdir .ssh \
    && mkdir in \
    && mkdir out

COPY . .
COPY sshd_config /etc/ssh/sshd_config
COPY ssh_key.pub .ssh/ssh_key.pub

RUN cat .ssh/ssh_key.pub >> .ssh/authorized_keys && \
    chmod 700 .ssh && \
    chmod 600 .ssh/* && \
    chmod +x start_server.sh

RUN pip install -r requirements.txt

EXPOSE 22