FROM python:3.11-slim

WORKDIR /app

ENV pythondontwritebytecode=1\
    pythonunbuffered=1\
    pythonpath=/app

COPY requirements/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app/

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

CMD ["python", "serve.py"]