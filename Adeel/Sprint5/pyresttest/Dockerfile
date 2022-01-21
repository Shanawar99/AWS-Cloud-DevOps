FROM python:2-alpine

LABEL Author="Z.d. Peacock <zdp@thoomtech.com>"

# This needs to be set otherwise pycurl won't link correctly
ENV PYCURL_SSL_LIBRARY=openssl


################ Nesseccery libraries for pyresttest ##############

RUN apk add --no-cache --update openssl curl \
    && apk add --no-cache --update --virtual .build-deps build-base python-dev curl-dev \
    && pip install jmespath jsonschema pyresttest \
    && apk del .build-deps


##############  setting up work directory ###################

WORKDIR /tests

################## copying the test file in image ##############

COPY . /tests

################ for tests ########################

ENTRYPOINT ["pyresttest"]