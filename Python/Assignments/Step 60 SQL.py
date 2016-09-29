import sqlite3
import time
import datetime

conn = sqlite3.connect('trackerlog.db')
c = conn.cursor()

def tableCreate():
    c.execute("CREATE TABLE IF NOT EXISTS lastRan (ID INT, unix REAL, datestamp TEXT)")

def update_log():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    c.execute("INSERT INTO lastRan (unix, datestamp) VALUES(?,?)",
              (unix, date))
    conn.commit()
    
def last_record():
    c.execute('SELECT max(datestamp) FROM lastRan')
    data = c.fetchone()
    print("Last Ran: " + data[0])


tableCreate()
last_record()
c.close()
conn.close()


##AFTER IMPORT
##INSERT NEW RECORD DATESTAMP

