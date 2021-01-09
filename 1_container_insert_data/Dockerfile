FROM python:3.8-alpine
WORKDIR /app
RUN apk update
RUN apk add curl sudo build-base unixodbc-dev unixodbc freetds-dev && pip install pyodbc
RUN apk add --no-cache tzdata
ENV TZ America/Phoenix
RUN rm -rf /var/cache/apk/*
RUN curl -O https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/msodbcsql17_17.5.2.2-1_amd64.apk
RUN sudo sudo apk add --allow-untrusted msodbcsql17_17.5.2.2-1_amd64.apk

COPY  bfi_data_suplier.py .
#COPY  modelPickle .
#expose 5000
# nginx es como apache server y la expocision la hariamos con kubernetes ingress
#CMD ["gunicorn", "-b", "0.0.0.0:5000", "app"]
CMD ["python", "bfi_data_suplier.py"]
