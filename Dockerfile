# Base image
FROM jenkins/jenkins:lts-jdk21
LABEL authors="a.moinur"

# Switch to root user to install packages
USER root


ENTRYPOINT ["top", "-b"]