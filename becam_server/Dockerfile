FROM python:3.6.9-alpine3.10

LABEL author="jfalconcardenas@gmail.com"


#Environment variables
ENV USER=develop
ENV HOME_DIR=home/develop
ENV SHELL=/bin/sh

ARG environment


#Create user
RUN mkdir /tmp/requirements && mkdir -p /$HOME_DIR && \
    addgroup -S $USER && adduser -S $USER -G $USER && \
    chown -R $USER:$USER /$HOME_DIR

# #Install packages necesary
# COPY ./requirements/ /tmp/requirements/
# RUN pip install -r /tmp/requirements/${environment}.txt



#Add code
ADD . /$HOME_DIR

#Entry-point


#USER $USER
WORKDIR /$HOME_DIR