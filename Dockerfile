FROM python:3.6.9-alpine
MAINTAINER ufsc.br
WORKDIR /app
COPY . /app

RUN apk update && apk add --no-cache libxml2-dev libxslt-dev build-base

# RUN pip --version
# RUN python --version
RUN pip install --upgrade pip
RUN pip install flask
RUN pip install flask_restful
RUN pip install marshmallow
RUN pip install "sumy[LSA]" && \
   python -c "import nltk; nltk.download('punkt')" && \
   rm -rf /root/.cache

CMD ["python","main.py"]
