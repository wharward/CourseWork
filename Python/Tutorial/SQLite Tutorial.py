import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def tableCreate():
    c.execute("CREATE TABLE stuffToPlot (ID INT, unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

##def dataEntry():
##    c.execute("INSERT INTO stuffToPlot VALUES(1, 1365652181.288, '2013-04-14 10:09:41', 'Python Sentiment',5)")
##    c.execute("INSERT INTO stuffToPlot VALUES(2, 1365952257.905, '2013-04-14 10:10:37', 'Python Sentiment',6)")
##    c.execute("INSERT INTO stuffToPlot VALUES(3, 1365652264.123, '2013-04-14 10:11:04', 'Python Sentiment',4)")
##    conn.commit()


def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)
    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES(?,?,?,?)",
              (unix, date, keyword, value))
    conn.commit()

def read_from_db():
    c.execute("SELECT * FROM stuffToPlot")
    data = c.fetchall()
    print(data)
    for row in c.fetchall():
        print(row[0])

def graph_data():
    c.execute('SELECT unix, value FROM stuffToPlot')
    dates = []
    values = []
    for row in c.fetchall():
        #print (row[0])
        #print(datetime.datetime.fromtimestamp(row[0]))
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])

    plt.plot_date(dates, values, '-')
    plt.show()

def del_and_update():
    c.execute('SELECT * FROM stuffToPlot')
    (print(row) for row in c.fetchall())
    
    
##
tableCreate()
###data_entry()
##for i in range(10):
##    dynamic_data_entry()
##    time.sleep(1)
##graph_data()
##del_and_update()
c.close()
conn.close()

