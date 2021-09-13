from celery.result import AsyncResult
from celery.canvas import Signature

from .tasks import power


def test_simple():
    assert power(3, 4) == 81

    result = power.delay(3, 4)
    assert isinstance(result, AsyncResult)
    print(result.__repr__())

    result = power.s(3, 4)
    assert isinstance(result, Signature)
    print(result.__repr__())


if __name__ == '__main__':
    print('Start testing workflow...')
    test_simple()
