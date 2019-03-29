import datetime
import os

import pandas as pd
import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from dotenv import load_dotenv

load_dotenv()

TODAY = f"{datetime.datetime.now():%Y-%m-%d}"
TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
SHIFTS_FILE = "turnos_piazza.csv"
SHIFTS_DF = pd.read_csv(SHIFTS_FILE)
TODAYS_TA = SHIFTS_DF[SHIFTS_DF["Date"] == TODAY]["TA"].tolist()[0]

sched = BlockingScheduler()


@sched.scheduled_job('cron', day_of_week='mon-fri', hour=8, minute=30)
def scheduled_job():
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                             params={
                                 "chat_id": CHAT_ID,
                                 "text": f"El ayudante de hoy es: *{TODAYS_TA}*.",
                                 "parse_mode": "Markdown"
    })

sched.start()
