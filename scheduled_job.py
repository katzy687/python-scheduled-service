"""
https://github.com/dbader/schedule
"""
import schedule
import time

import datetime
from log_handler import get_logger

logger = get_logger()


def my_job():
    now = datetime.datetime.now()
    job_msg = f'job ran: {now.strftime("%H:%M:%S")}'
    logger.info(job_msg)


class SchedulerHandler:
    def __init__(self, frequency_seconds: int = 5):
        self.frequency_seconds = frequency_seconds
        self.active = False
        self.logger = get_logger()

    def run_scheduler(self):
        logger.info("Starting scheduled job")
        schedule.every(self.frequency_seconds).seconds.do(my_job)
        self.active = True
        while self.active:
            schedule.run_pending()
            time.sleep(1)

    def stop_scheduler(self):
        logger.info("stopping scheduled job")
        self.active = False
        schedule.clear()


if __name__ == "__main__":
    handler = SchedulerHandler()
    handler.run_scheduler()
