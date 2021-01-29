FROM python:3.8-slim

ENV TZ ${TZ}

# install FreeTDS and dependencies
RUN apt-get update \
    && apt-get install unixodbc netcat-openbsd unixodbc-dev freetds-dev freetds-bin tdsodbc -y \
    && apt-get install --reinstall build-essential -y

# populate "ocbcinst.ini" as this is where ODBC driver config sits
RUN echo "[FreeTDS]\n\
Description = FreeTDS Driver\n\
Driver = /usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so\n\
Setup = /usr/lib/x86_64-linux-gnu/odbc/libtdsS.so" >> /etc/odbcinst.ini

RUN mkdir /src
COPY ./entrypoint.sh .
COPY . /src/

RUN pip install --no-cache-dir -r /src/requirements.txt
#COPY  modelPickle .
#expose 5000
# nginx es como apache server y la expocision la hariamos con kubernetes ingress
#CMD ["gunicorn", "-b", "0.0.0.0:5000", "app"]
#CMD ["python", "/app/data_context.py"]
RUN ["chmod", "+x", "/entrypoint.sh"]
ENTRYPOINT [ "sh", "/entrypoint.sh" ]