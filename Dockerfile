FROM python:3.10-slim

WORKDIR /app

COPY pyproject.toml poetry.lock* entrypoint.sh ./

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

COPY . .

CMD ["python", "app.py"]