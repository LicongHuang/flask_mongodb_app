FROM python:3
ENV PYTHONUNBUFFERED 1
#ENV MONGODB "mongodb+srv://userReadOnly:7ZT817O8ejDfhnBM@minichallenge.q4nve1r.mongodb.net/"
EXPOSE 8080
RUN mkdir /src
WORKDIR /src
ADD requirements.txt /src/
RUN pip3 install -r requirements.txt
ADD . /src/

ENTRYPOINT ["python3", "application.py"]
