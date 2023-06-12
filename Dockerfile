FROM python:3.9

RUN mkdir -p /docker/app/game_bot/
WORKDIR /docker/app/game_bot/

COPY . /docker/app/game_bot/
RUN pip install -r requirements.txt

