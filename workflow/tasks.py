from time import sleep

import random

from .celery import app

@app.task
def power(value, expo):
    """
    >>> from workflow.tasks import power
    >>> power(3, 4)
    81
    >>> power.s(3, 4)
    workflow.tasks.power(3, 4)
    >>> power.delay(3, 4)
    <AsyncResult: 44270536-9a33-48cf-8b72-f1ab14052282>
    """
    sleep(random.randint(10, 1000) / 1000.0) # sleep for 10-1000ms
    return value ** expo
