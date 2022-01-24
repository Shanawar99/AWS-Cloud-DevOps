From python:2-alpine
ENV PYCURL_SSL_LIBRARY=openssl

RUN apk add --no-cache --update openssl curl 
RUN apk add --no-cache --update --virtual .build-deps build-base python-dev curl-dev 
RUN pip install jmespath jsonschema pyresttest 
RUN apk del .build-deps

WORKDIR /Irfan

COPY . /Irfan/

ENTRYPOINT [ "pyresttest" ]

