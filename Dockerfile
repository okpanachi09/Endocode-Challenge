# the base image
FROM alpine:latest
# copy all the contents to the docker image
COPY . /app
# set the working directory => any command that you execute is gonna be executed from here
WORKDIR /app
# RUN execute commands 
RUN apk add make python3 py3-pip
RUN cd /app
RUN pip install .
# entry point command
CMD python3 /app/src/main.py