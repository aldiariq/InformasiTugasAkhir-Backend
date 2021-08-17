FROM python:3.8

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
ENV FLASK_ENV=production 
CMD ["flask", "run", "--host=0.0.0.0"]