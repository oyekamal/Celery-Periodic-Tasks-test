from celery import shared_task
from time import sleep

@shared_task(bind=True)
def go_to_sleep(self,durations):
    print('Request: {0!r}'.format(self.request))
    # sleep(durations)
    return 'DONE'


@shared_task
def add(x, y):
    return x + y 


from celery import Celery
from celery.schedules import crontab

app = Celery()

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test.s('Happy Mondays!'),
    )

@app.task
def test(num=12):
    # print(arg)
    print('----------------------------------')
    print(f"im working bro  {num}")
    
    
#for check 
#celery -A django_email_celery beat -l INFO
#celery -A django_email_celery worker -B -l INFO  
#celery -A django_email_celery worker -B -l INFO  --detach
#celery -A proj beat -l INFO --scheduler 
@app.task
def print1():
    print("----------------------------------")
    print("hello it working")
