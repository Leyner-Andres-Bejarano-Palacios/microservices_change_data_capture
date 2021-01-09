FROM python:3

RUN pip install --upgrade pip


# Install Azure Event Hub PythonSDK Module
RUN pip install azure-eventhub && \
    pip install azure-eventhub-checkpointstoreblob-aio  && \
    pip install flask && \
    pip install flask-restful

# Remove Unneeded PIP Cache after Install
RUN rm -rf /.cache

COPY  . .
#COPY  modelPickle .
expose 5000
# nginx es como apache server y la expocision la hariamos con kubernetes ingress
#CMD ["gunicorn", "-b", "0.0.0.0:5000", "app"]
CMD ["python", "event_sender.py"]