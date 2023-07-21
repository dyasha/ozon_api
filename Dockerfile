FROM python:3.11-bookworm

RUN python -m pip install --upgrade pip

COPY . .

RUN pip install poetry==1.4.2
RUN poetry config virtualenvs.create false
RUN poetry install --without dev
CMD uvicorn ozon_api.app:app --host 0.0.0.0 --port 8000 --reload
