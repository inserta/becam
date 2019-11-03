FROM python:3.7
LABEL author="jfalconcardenas@gmail.com"


#Environment variables
ENV USER=develop
ENV HOME_DIR=home/develop
ENV SHELL=/bin/bash

ARG environment


#Create user
RUN mkdir /tmp/requirements && mkdir -p /$HOME_DIR && \
    useradd -ms $SHELL $USER && chown -R $USER:$USER /$HOME_DIR

#Install packages necesary
COPY ./requirements/ /tmp/requirements/
RUN pip install -r /tmp/requirements/${environment}.txt



#Add code flask and package to application
ADD ./project /$HOME_DIR

#Entry-point


#USER $USER
WORKDIR /$HOME_DIR
