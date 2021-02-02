FROM python:3.8

WORKDIR /app 
RUN apt-get update
RUN apt-get install -y unixodbc-dev unixodbc freetds-dev
COPY ./requirements.txt /app/requirements.txt


# Install Azure Event Hub PythonSDK Module
RUN pip install -r /app/requirements.txt

# Remove Unneeded PIP Cache after Install
RUN rm -rf /.cache

COPY  . /app/
#COPY  modelPickle .
EXPOSE 5000
# nginx es como apache server y la expocision la hariamos con kubernetes ingress
#CMD ["gunicorn", "-b", "0.0.0.0:5000", "app"]
CMD ["python", "/app/EventSender.py", "-p","configs/sender.ini"]