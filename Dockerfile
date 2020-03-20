FROM ubuntu:18.04

RUN apt update && apt upgrade -y && apt install -y python3 python3-pip pandoc mongodb

RUN pip3 install pyTelegramBotAPI pypandoc BeautifulSoup4 pymongo

COPY ./src /app

CMD python3 /app/main.py