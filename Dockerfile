FROM python:3.8.1

COPY . /chat-sentiment-api

WORKDIR /chat-sentiment-api

#RUN python3 -m nltk.downloader punkt

RUN pip3 install -r requirements.txt

CMD ["python3","api.py"]