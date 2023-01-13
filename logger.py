import sqlite3
from datetime import datetime, date

# On require, boot up sqlite for storing times & stuff
con = sqlite3.connect("cur.db")
cur = con.cursor()

def init():
    x = cur.execute("SELECT name FROM sqlite_master WHERE name='washer'")
    if x.fetchone() is None:
        print("creating tables...")
        cur.execute("CREATE TABLE washer(date, time_start, time_end)")
        cur.execute("CREATE TABLE dryer(date, time_start, time_end)")

def addWashingMachineEntry(start, end):
    rn = datetime.now().second
    cur.execute(f"""
        INSERT INTO washer VALUES
            ('{rn}','{start}','{end}')
    """)

    con.commit()

def addDryingMachineEntry(start, end):
    rn = datetime.isoformat(date.today())
    cur.execute(f"""
        INSERT INTO washer VALUES
            ('{rn}','{start}','{end}')
    """)

    con.commit()