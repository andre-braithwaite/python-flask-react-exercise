FROM python:3.10-bullseye

WORKDIR /app

ENV FLASK_APP=server.py

ENV FLASK_ENV=development

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "server.py"]