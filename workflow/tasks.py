from time import sleep

import random

from .celery import app

@app.task
def power(value, expo):
    sleep(random.randint(10, 1000) / 100.0)
    return value ** expo


@app.task
def amass(values):
    print(str(values))
