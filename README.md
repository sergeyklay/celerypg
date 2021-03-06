# Celery Playgroud

[![Code Linting][actions-badge]][actions link]

My primary playground for doing Celery trials. Hence, the name.


## Contents


- **Workflow Primitives**
  - [`chord`][workflow]: Performing a task after all tasks have been completed
  - [`chain`][chain]: Performing chord with group of chains and a callback at the end

## Prerequisites

To play with this project at your local environment you'll need the following
requirements:

- Python >= 3.7
- Redis or Docker

The project should work the same on the all major systems macOs, Linux,
Windows or WSL.

## Installing

To install all dependencies such as Celery use the pip:

```
$ python -m pip install -r requirements.txt
```

## Run tests

1. Start Redis:
   ```
   $ docker run -d -p 6379:6379 redis
   ```

2. Run the consumer (worker) instance:
   ```
   $ celery -A <module> worker --loglevel=INFO
   ```

3. Run the producer:
   ```
   $ python -m <module>.producer
   ```

## License

This is free and unencumbered software released into the public domain.
For more see [LICENSE][license] file.

[actions link]: https://github.com/sergeyklay/celerypg/actions/workflows/cs.yml
[actions-badge]: https://github.com/sergeyklay/celerypg/actions/workflows/cs.yml/badge.svg
[workflow]: https://github.com/sergeyklay/celerypg/tree/master/workflow
[chain]: https://github.com/sergeyklay/celerypg/tree/master/chain
[license]: https://github.com/sergeyklay/celerypg/blob/master/LICENSE
