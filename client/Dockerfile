FROM python:latest

RUN apt-get update && apt-get install -y ssh python3-pgpy

WORKDIR /root

COPY . .

RUN pip install -r requirements.txt

CMD [ "tail", "-f", "/dev/null" ]