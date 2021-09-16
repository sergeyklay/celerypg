from celery import chain, chord, group

from .tasks import amass, negate, power


def main():
    # Create 10 chain tasks signatures.
    chains = [chain(power.s(i, 2), negate.s()) for i in range(10)]

    # Create a callback.
    callback = amass.s()

    # A ``chord`` is just like a ``group`` but with a callback.
    #
    # A ``chord`` consists of a header group and a body,
    # where the body is a task that should execute after all of the
    # tasks in the header are complete.
    #
    # Actually, the code bellow is equivalent the following
    # >>> group = chord(group(chains))
    # >>> group(callback)
    return chord(group(chains))(callback)


if __name__ == '__main__':
    print('Start testing workflow...')
    main()
