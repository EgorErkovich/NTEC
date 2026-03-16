FROM python:3.6

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY entrypoint.sh /entrypoint.sh
COPY entrypoint_celery.sh /entrypoint_celery.sh
RUN chmod +x /entrypoint.sh /entrypoint_celery.sh

ENTRYPOINT ["/entrypoint.sh"]
