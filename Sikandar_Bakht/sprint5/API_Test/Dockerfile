FROM thoom/pyresttest
COPY ./ /usr/src/app
WORKDIR /usr/src/app
ENTRYPOINT ["pyresttest"]
CMD ["https://ky3yjof2g9.execute-api.us-east-1.amazonaws.com", "test.yml"]