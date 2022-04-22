# Base image
FROM nginx:stable-alpine

# Create new group and user (with UID = 1000)
ARG USERNAME=www-data
ARG UID=1000

# set -eux; will stop the script if any error occurs
RUN set eux; \
    adduser -S -D -u ${UID} -G ${USERNAME} ${USERNAME}; \
    chown -hR ${USERNAME}:${USERNAME} /usr/share/nginx; \
    chown -hR ${USERNAME}:${USERNAME} /var/cache/nginx; \
    touch /var/run/nginx.pid; \
    chown -hR ${USERNAME}:${USERNAME} /var/run/nginx.pid

# Set working directory to nginx resources directory and remove default resources
WORKDIR /usr/share/nginx/html

# Copy the builded app to the image
COPY ./dist .

USER www-data
