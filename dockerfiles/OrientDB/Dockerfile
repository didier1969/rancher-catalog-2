############################################################
# Dockerfile to run an OrientDB (Graph) Container
############################################################

FROM openjdk:8-jdk-alpine

MAINTAINER Didier Stadelmann

ENV ORIENTDB_DOWNLOAD_URL https://s3.us-east-2.amazonaws.com/orientdb3/releases/3.0.1/orientdb-tp3-3.0.1.tar.gz

RUN apk add --update tar curl \
    && rm -rf /var/cache/apk/*

#download distribution tar, untar and delete databases
RUN mkdir /orientdb && \
  wget  $ORIENTDB_DOWNLOAD_URL \
  && tar -xvzf orientdb-tp3-3.0.1.tar.gz -C /orientdb --strip-components=1 \
  && rm orientdb-tp3-3.0.1.tar.gz \
  && rm -rf /orientdb/databases/*


ENV PATH /orientdb/bin:$PATH

VOLUME ["/orientdb/backup", "/orientdb/databases", "/orientdb/config"]

WORKDIR /orientdb

#OrientDb binary
EXPOSE 2424

#OrientDb http
EXPOSE 2480

# Default command start the server
CMD ["server.sh"]
