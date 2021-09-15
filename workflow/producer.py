from celery import chord

from .tasks import amass, power


def main():
    # Create 10 tasks signatures.
    tasks = (power.s(i, 2) for i in range(10))

    # Create a callback.
    callback = amass.s()

    # A ``chord`` is just like a ``group`` but with a callback.
    #
    # A ``chord`` consists of a header group and a body,
    # where the body is a task that should execute after all of the
    # tasks in the header are complete.
    #
    # Actually, the code bellow is equivalent the following
    # >>> group = chord(tasks)
    # >>> group(callback)
    return chord(tasks)(callback)


if __name__ == '__main__':
    print('Start testing workflow...')
    main()
