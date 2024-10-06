from apscheduler.schedulers.background import BackgroundScheduler
from config.db import Session
from sqlalchemy.exc import OperationalError

class ScheduledTasks:
    def __init__(self):
        self.scheduler = BackgroundScheduler()

    def ping_database(self):
        try:
            db = Session()
            db.execute("SELECT 1")
        except OperationalError as e:
            print(f"Error pinging database: {e}")
        finally:
            db.close()

    def start(self):
        # Schedule the ping_database function to run every 60 minutes
        self.scheduler.add_job(self.ping_database, 'interval', minutes=60)
        self.scheduler.start()
        print("Scheduled tasks started")

    def stop(self):
        self.scheduler.shutdown()
