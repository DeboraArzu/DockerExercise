FROM alpine:3.7
WORKDIR /app

RUN apk update
RUN apk -Uuv add groff less python py-pip
RUN pip install awscli

COPY /home/deboraarzu/Desktop/Repos /root/.aws
VOLUME /home/deboraarzu/Desktop/Repos /root/.aws

ENTRYPOINT ["aws", "s3", "ls"]