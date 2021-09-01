FROM python:3.9-alpine
LABEL maintainer="Eric Karschner <erickarschner@gmail.com>"

RUN apk add tzdata && \
    cp /usr/share/zoneinfo/America/New_York /etc/localtime && \
    echo "America/New_York" > /etc/timezone && \
    apk del tzdata

WORKDIR /app/
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/

ENTRYPOINT ["gunicorn", "app:app"]
CMD ["--bind=0.0.0.0:8080"]
