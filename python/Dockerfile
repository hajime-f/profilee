FROM python:3.11
WORKDIR /code
ADD requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /code/
