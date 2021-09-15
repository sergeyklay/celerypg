from celery import Celery

app = Celery(
    'workflow',
    broker='redis://localhost',
    backend='redis://localhost',
    include=['workflow.tasks'])

if __name__ == '__main__':
    app.start()
