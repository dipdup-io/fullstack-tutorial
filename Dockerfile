FROM python:3.10-slim-buster

RUN apt update && \
    apt install -y make git gcc && \
    rm -rf /var/lib/apt/lists/*

RUN pip install poetry

WORKDIR /demo
COPY poetry.lock pyproject.toml /demo/

RUN poetry config virtualenvs.create false && poetry install --no-dev

COPY . /demo

ENTRYPOINT ["poetry", "run", "dipdup"]
CMD ["-c", "dipdup.yml", "run"]