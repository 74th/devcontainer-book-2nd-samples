FROM mcr.microsoft.com/devcontainers/python:3.13

RUN apt-get update && apt-get install -y --no-install-recommends \
  iptables \
  ipset \
  iproute2 \
  dnsutils \
  aggregate \
  && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY ./init.sh ./allow_domains.txt /root

USER root

# sudoを削除
RUN rm /etc/sudoers.d/vscode

ENTRYPOINT /bin/bash /root/init.sh && sleep infinity