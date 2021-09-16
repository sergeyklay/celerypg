# Celery Playgroud

My primary playground for doing Celery trials. Hence, the name.


## Contents

- **Workflow Primitives**
  - [`chord`][workflow]: Running a task after all tasks have been completed

## Run tests

1. Start redis:
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
For more see [LICENSE](./LICENSE) file.

[workflow]: https://github.com/sergeyklay/celerypg/tree/master/workflow
