#Base Image
FROM python:3.6.5-slim

# set the working directory
WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8080

# execute the Flask app
CMD ["python", "app.py"]