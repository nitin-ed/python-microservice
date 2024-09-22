# LAYER 1 : Base Image
FROM python:3.10-slim-bullseye

# ENV variables
ENV JWT_SECRET=test_secret
ENV MYSQL_HOST=""
ENV MYSQL_USER=""
ENV MYSQL_PASSWORD=""
ENV MYSQL_DB=""
ENV MYSQL_PORT=""

# Install dependencies for mysqlclient
RUN apt-get update && \
    apt-get install -y default-libmysqlclient-dev build-essential pkg-config && \
    apt-get clean

# LAYER 2 :
RUN apt-get update \
    && apt-get install -y --no-install-recommends --no-install-suggests \
       build-essential \
       default-libmysqlclient-dev \
       libsqlite3-dev \  
    && pip install --no-cache-dir --upgrade pip

# LAYER 3 :
WORKDIR /app
COPY ./requirements.txt /app

# 
RUN pip install --no-cache-dir --requirement /app/requirements.txt
COPY . /app

EXPOSE 5000

CMD ["python3", "server.py"]


