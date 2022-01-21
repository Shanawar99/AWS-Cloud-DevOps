###################################################################################
##                     DOCKERFILE FOR PYRESTTEST IMAGE                           ##
###################################################################################

#Importing python imaage from the default available images
FROM python:2-alpine
LABEL Author="Z.d. Peacock <zdp@thoomtech.com>"

# This needs to be set otherwise pycurl won't link correctly
ENV PYCURL_SSL_LIBRARY=openssl

#Installing the libraries
RUN apk add --no-cache --update openssl curl \
    && apk add --no-cache --update --virtual .build-deps build-base python-dev curl-dev \
    && pip install jmespath jsonschema pyresttest \
    && apk del .build-deps

#Setting up the work directory
WORKDIR /tests

#Copying the content in the work directory
COPY . /tests
ENTRYPOINT ["pyresttest"]

####################################### :) ############################################