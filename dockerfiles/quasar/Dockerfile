FROM node:carbon-stretch

# Generate locale C.UTF-8 for postgres and general locale data
ENV LANG C.UTF-8

# Install some deps, lessc and less-plugin-clean-css, and wkhtmltopdf
RUN set -x; \
        apt-get update \
        && apt-get install -y --no-install-recommends \
            ca-certificates \
            curl \
            nano \
            zip \
            unzip \
        && apt-get update \
        && npm install -g vue-cli quasar-cli
