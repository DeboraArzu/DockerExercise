FROM alpine:latest

WORKDIR /app

RUN apk add docker && \
    apk add py-pip && \
    pip install docker-compose

#install the magic wrapper
ADD ./wrapdocker /usr/local/bin/wrapdocker
RUN chmod +x /usr/local/bin/wrapdocker

#define additional metadata
VOLUME /var/run/docker.sock:/var/run/docker.sock