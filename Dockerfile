FROM python:3.6

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app  # specifying the working dir inside the container

COPY ./spa/requirements.txt ./   
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install mysqlclient
RUN pip install pyjwt

# copy current dir's content to container's WORKDIR root i.e. all the contents of the web app
COPY ./spa .