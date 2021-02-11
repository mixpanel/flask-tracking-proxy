FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN apt-get -y update
RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python3", "flask_proxy/app.py"]
