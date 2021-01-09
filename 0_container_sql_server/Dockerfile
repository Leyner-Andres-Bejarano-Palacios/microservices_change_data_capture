FROM mcr.microsoft.com/mssql/server:2019-latest

RUN apt-get install curl -y
RUN apt-get update && apt-get install -y gnupg2
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN apt-get install software-properties-common -y
RUN apt-add-repository https://packages.microsoft.com/ubuntu/18.04/prod -y
RUN apt-get install mssql-cli -y
RUN apt-get install -f

