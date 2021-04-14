# https://stackoverflow.com/questions/61751752/cant-install-python-pip-to-docker-container
FROM python:3

RUN apt-get update -y && apt-get install -y build-essential
COPY . /app
WORKDIR /app 
RUN pip install -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]