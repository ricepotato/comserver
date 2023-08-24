FROM python:3.10
RUN mkdir /app
WORKDIR /app
COPY ./docker-entrypoint.sh /app
COPY dist/*.whl /app
RUN pip install /app/*.whl
CMD ["./docker-entrypoint.sh"]
