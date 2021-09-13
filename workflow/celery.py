from celery import Celery

app = Celery(
    'workflow',
    backend='redis://localhost',
    broker='redis://localhost',
    include=['workflow.tasks'])

if __name__ == '__main__':
    app.start()
