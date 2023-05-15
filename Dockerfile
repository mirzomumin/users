FROM python:3.11
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /user
WORKDIR /user
COPY requirements.txt /user/
RUN apt-get update -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /user/