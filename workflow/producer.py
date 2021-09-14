from celery.result import AsyncResult
from celery.canvas import Signature
from celery import chord, group

from .tasks import amass, power


def test_power():
    assert power(3, 4) == 81

    result = power.delay(3, 4)
    assert isinstance(result, AsyncResult)
    print(result.__repr__())

    result = power.s(3, 4)
    assert isinstance(result, Signature)
    print(result.__repr__())



def test_complex():
    # Create 10 tasks signatures.
    tasks = [power.s(i, 2) for i in range(10)]

    # The ``group`` primitive is a signature that takes
    # a list of tasks that should be applied in parallel.
    tasks = group(tasks)

    # Create a callback.
    callback = amass.s()

    # A ``chord`` is just like a ``group`` but with a callback.
    # A ``chord`` consists of a header ``group`` and a body,
    # where the body is a task that should execute after all of the
    # tasks in the header are complete.
    result = chord(tasks)(callback)
    assert isinstance(result, AsyncResult)
    print(result.__repr__())


if __name__ == '__main__':
    print('Start testing workflow...')
    # test_power()
    test_complex()
