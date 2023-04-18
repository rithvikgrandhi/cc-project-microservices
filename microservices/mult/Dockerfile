# Follow Task-0 subtask-1
FROM python:3.8-alpine

COPY ./app/ app/

WORKDIR /app

RUN apk add --update \
	&& pip install --upgrade pip  \
	&& pip install -r requirements.txt \
	&& rm -rf /var/cache/apk/*

CMD ["python", "mult.py"]
