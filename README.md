# celery-redis

### Celery Monitor
redis-cli monitor

### Celery example - standalone (git tag 1.0.0)
celery -A tasks worker --loglevel=info


### Flask application with Celery (git tag 1.0.0)
```
Celery worker
celery -A celery_example.celery worker --loglevel=info

Flask application
python celery_example.py
```

### Run a curl request
curl -X GET http://localhost:5000/process/hello
{
  "status": "http://localhost:5000/status/582db787-cb10-46ba-97ad-eccf6accd5b1",
  "uuid": "582db787-cb10-46ba-97ad-eccf6accd5b1"
}

curl -X GET http://localhost:5000/status/582db787-cb10-46ba-97ad-eccf6accd5b1
{
  "state": "PENDING"
}

curl -X GET http://localhost:5000/status/582db787-cb10-46ba-97ad-eccf6accd5b1
{
  "state": "SUCCESS",
  "status": "olleh"
}

### Interesting reading: Celery client for Node.js
https://github.com/mher/node-celery