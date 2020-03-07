FROM python:3
RUN pip install --upgrade pip && pip install psutil
COPY collect_metrics.py /
ENTRYPOINT ["python3","./collect_metrics.py"]
CMD [ "cpu" ]
