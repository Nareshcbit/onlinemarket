FROM python:alpine3.6


ARG APP_DIR='/emarket'
ENV FLASK_APP=emarket.py
ENV REDIS_HOST='192.168.0.18'
ENV DATABASE_URL='mysql+pymysql://naresh:Welcome@192.168.0.18/mydb'


RUN apk add --no-cache bash  && apk add --no-cache curl && apk add --no-cache nano

COPY . ${APP_DIR}
RUN pip install --no-cache-dir -r ${APP_DIR}/requirements.txt
WORKDIR ${APP_DIR}

EXPOSE 5000
