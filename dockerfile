FROM python:3.8

WORKDIR /App
COPY . .

RUN pip3 install -r requirements.txt

ENV PYTHONPATH /App

RUN apt update && apt install -y sqlite3

WORKDIR ./spothero_alembic

RUN alembic upgrade head

WORKDIR ../

CMD [ "python", "./spothero_api/Lib/flask/app.py"]