FROM mcr.microsoft.com/mssql/server:2019-latest

USER root
RUN apt update 
RUN apt install -y curl gnupg2               
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN apt install -y software-properties-common 
RUN apt-add-repository -y https://packages.microsoft.com/ubuntu/18.04/prod 
RUN apt install -y mssql-cli netcat-openbsd

RUN mkdir /scripts
COPY ./conf /scripts

ENV ACCEPT_EULA: ${ACCEPT_EULA}
ENV SA_PASSWORD: ${MSSQL_PASSWORD}
ENV MSSQL_PASSWORD: ${SA_PASSWORD}
ENV MSSQL_AGENT_ENABLED: ${MSSQL_AGENT_ENABLED}
ENV MSSQL_PID: ${MSSQL_PID}

RUN ["chmod", "+x", "/scripts/init_db.sh"]