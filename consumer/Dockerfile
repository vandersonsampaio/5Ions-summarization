FROM python:3.6.9-alpine
MAINTAINER ppgcc.ine.ufsc.br
WORKDIR /app
COPY . /app

RUN apk update && apk add --no-cache libxml2-dev libxslt-dev build-base

RUN pip install --upgrade pip
RUN pip install pika
RUN pip install marshmallow
RUN pip install "sumy[LSA]" && \
   python -c "import nltk; nltk.download('punkt')" && \
   rm -rf /root/.cache

CMD ["python","rabbit_consumer.py"]
