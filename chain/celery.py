from celery import Celery

app = Celery(
    'chain',
    broker='redis://localhost',
    backend='redis://localhost',
    include=['chain.tasks'])

if __name__ == '__main__':
    app.start()
