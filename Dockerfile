FROM pypy:2

RUN pip install falcon gunicorn redis

COPY ./main.py /

ENTRYPOINT ["gunicorn", "-w", "4", "-b", ":8080", "main:api"]

