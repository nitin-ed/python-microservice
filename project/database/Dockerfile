# LAYER 1 : Base Image
FROM python:3.10-slim-bullseye

# ENV variables
ENV JWT_SECRET=test_secret
ENV MYSQL_HOST=""
ENV MYSQL_USER=""
ENV MYSQL_PASSWORD=""
ENV MYSQL_DB=""
ENV MYSQL_PORT=""

RUN apt-get update \
    && apt-get install -y --no-install-recommends --no-install-suggests \
       build-essential \
       default-libmysqlclient-dev \
       libsqlite3-dev \
       pkg-config \  
    && pip install --no-cache-dir --upgrade pip

WORKDIR /app
COPY ./requirements.txt /app
    
RUN pip install --no-cache-dir --requirement /app/requirements.txt
COPY . /app

EXPOSE 5001

CMD ["python3", "server.py"]