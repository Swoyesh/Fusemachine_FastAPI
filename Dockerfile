FROM python:3.11-slim

WORKDIR /app

ENV pythondontwritebytecode=1\
    pythonunbuffered=1\
    pythonpath=/app

COPY requirements/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["python", "src/serve.py"]