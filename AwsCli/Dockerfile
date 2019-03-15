FROM alpine:3.7
WORKDIR /app

RUN apk update && \
    apk -Uuv add groff less python py-pip && \
    pip install awscli

ADD /home/deboraarzu/Desktop/Repos /root/.aws
VOLUME /home/deboraarzu/Desktop/Repos /root/.aws

ENTRYPOINT ["aws", "s3", "ls"]