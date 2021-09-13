from time import sleep

import random

from .celery import app

@app.task
def power(value, expo):
    sleep(random.randint(10, 1000) / 1000.0) # sleep for 10-1000ms
    return value ** expo
