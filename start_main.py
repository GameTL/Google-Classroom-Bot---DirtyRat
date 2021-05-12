from apscheduler.schedulers.blocking import BlockingScheduler
import main
sched = BlockingScheduler()
import os

""" @sched.scheduled_job('interval', seconds=10)
def timed_job():
    print('This job is run every 10 seconds.') """


@sched.scheduled_job('cron', day_of_week='mon-fri', hour=00)
def scheduled_job():
    print('This job is run every weekday at 23.')


os.system('main.py')


sched.start()


