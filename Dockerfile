#-------Frontend build image-------
FROM node:22 AS frontend-builder

WORKDIR /app/frontend

COPY frontend/package*.json ./
RUN npm install

COPY frontend/ ./
RUN npm run build

#-------Python backend image-------
FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen

COPY ./src ./src
COPY ./api ./api

COPY --from=frontend-builder /app/frontend/dist ./frontend/dist

RUN mkdir -p output

ENV PYTHONPATH=/app/src

CMD uv run uvicorn api.app:app --host 0.0.0.0 --port ${PORT:-8000}