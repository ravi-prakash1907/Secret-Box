FROM python:3.6

# MAINTAINER Shekhar Gulati "1907prakash.ravi@gmail.com"
COPY ./src /app

#COPY ./test /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["source env/bin/activate & python3 app.py"]
#CMD ["python3 app.py"]

#ENTRYPOINT ["python"]
#CMD ["app.py"]