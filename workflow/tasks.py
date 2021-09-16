import random
from time import sleep

from .celery import app


@app.task
def power(value, expo):
    # TODO: Simulate tasks error
    # if value == 7:
    #    raise ValueError

    sleep(random.randint(10, 1000) / 100.0)
    return value ** expo


@app.task
def amass(values):
    print(sum(values))
