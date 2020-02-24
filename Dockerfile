FROM python:3.8.1

COPY . /chat-sentiment-api

WORKDIR /chat-sentiment-api

RUN pip install -r requirements.txt

CMD ["python3","api.py"]