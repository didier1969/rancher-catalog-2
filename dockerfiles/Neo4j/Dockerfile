FROM openjdk:8-jre-alpine

RUN addgroup -S neo4j && adduser -S -H -h /var/lib/neo4j -G neo4j neo4j

ENV NEO4J_SHA256=ea04207536c91e83e1889b04ae3276876d1a9612e7fba69dbf188bb3d5e08cdd \
    NEO4J_TARBALL=neo4j-community-3.4.0-unix.tar.gz \
    NEO4J_EDITION=community
ARG NEO4J_URI=http://dist.neo4j.org/neo4j-community-3.4.0-unix.tar.gz

RUN apk add --no-cache --quiet \
    bash \
    curl \
    tini \
    nano \
    su-exec \
    && curl --fail --silent --show-error --location --remote-name ${NEO4J_URI} \
    && echo "${NEO4J_SHA256}  ${NEO4J_TARBALL}" | sha256sum -csw - \
    && tar --extract --file ${NEO4J_TARBALL} --directory /var/lib \
    && mv /var/lib/neo4j-* /var/lib/neo4j \
    && rm ${NEO4J_TARBALL} \
    && mv /var/lib/neo4j/data /data \
    && mv /var/lib/neo4j/conf /conf \
    && mv /var/lib/neo4j/logs /logs \
    && chown -R neo4j:neo4j /data \
    && chown -R neo4j:noe4j /logs \
    && chown -R neo4j:neo4j /conf \
    && chmod -R 777 /data \
    && chmod -R 777 /logs \
    && chmod -R 777 /conf \
    && chown -R neo4j:neo4j /var/lib/neo4j \
    && chmod -R 777 /var/lib/neo4j \
    && ln -s /data /var/lib/neo4j/data \
    && ln -s /logs /var/lib/neo4j/logs \
    && ln -s /conf /var/lib/neo4j/conf\
    && apk del curl

ENV PATH /var/lib/neo4j/bin:$PATH

WORKDIR /var/lib/neo4j

VOLUME /data
VOLUME /logs
VOLUME /conf

COPY docker-entrypoint.sh /docker-entrypoint.sh

EXPOSE 7474 7473 7687

ENTRYPOINT ["/sbin/tini", "-g", "--", "/docker-entrypoint.sh"]
CMD ["neo4j"]
