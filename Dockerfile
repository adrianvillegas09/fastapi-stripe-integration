FROM python:3.8.1

ENV PYTHONUNBUFFERED 1

EXPOSE 8000
WORKDIR /src

COPY poetry.lock pyproject.toml ./
RUN pip install --upgrade pip
RUN apt-get -y install --no-install-recommends make=* && \
    pip install poetry==1.1.* && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

COPY . ./

CMD ["make", "run_server"]