import time
import random

from celery import Celery

# Wait for rabbitmq to be started
time.sleep(15)

app = Celery(
    'postman',
    broker='redis://redis:6379',
    backend='rpc://',
)


@app.task(name='addTask')  # Named task
def add(x, y):
    print('Task Add started')
    time.sleep(10 * random.random())  # Simulate a long task
    print('Task Add done')
    return x + y
