FROM ubuntu:16.04

MAINTAINER c2w2m2 juchang0308@gmail.com

RUN apt-get clean
RUN apt-get update
RUN apt-get install -y xinetd 
RUN apt-get install -y python2.7

ENV TERM=linux

RUN useradd attack
RUN mkdir /home/attack
WORKDIR /home/attack

ADD main.py /home/attack
ADD flag /home/attack
ADD flag /
ADD attack /etc/xinetd.d

RUN chmod 460 /home/attack/*
RUN chown attack:root /home/attack/*
RUN chmod +x /home/attack/main.py

RUN echo "attack 2222/tcp" >> /etc/services
EXPOSE 2222

CMD ["/usr/sbin/xinetd","-dontfork"]