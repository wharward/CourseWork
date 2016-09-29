from tkinter import *
from tkinter import ttk
import datetime
import os
import shutil
import sqlite3
import time
import datetime



##Open Time Logging Database
conn = sqlite3.connect('trackerlog.db')
c = conn.cursor()

###SQLite Functions
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

### Window Functions
def browser():
    root = Tk()
    root.withdraw()
    dirname = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
    import_button.state(['!disabled'])

    v.set(dirname)
    s=v.get

def browser1():
    root = Tk()
    root.withdraw()
    dirname = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
    import_button.state(['!disabled'])

    v1.set(dirname)
    s1=v1.get

def fileScreener():
    now = datetime.datetime.now()
    source = str(v.get())
    contents = os.listdir(source)
    destination =str(v1.get())

    for files in contents:
        if files.endswith(".txt"):
            modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(source + "\\" + files))
            duration = now - modified_date
            if duration.days < 1:
                shutil.copy(source + "\\" + files,destination)
                print(source + "/" + files + " moved to " +  destination + "/" + files)

    root.destroy()

def quit():
    root.destroy()

##Read last entry


## Create Window
root = Tk("Choose a folder")
root.wm_title("New File Retrieve Tool")

### Last Ran Widget
Time_Rec = StringVar()
Time_Rec.set(last_record())
ttk.Label(root, text = "hello").grid(row = 0, column = 1)


###Source Folder Widgets
ttk.Label(root, text = 'From Location:').grid(row = 1, column = 1)

v = StringVar()
entry = ttk.Entry(root, width = 40, textvariable = v).grid(row = 1, column = 2)
v.set("Browse for the Source Folder >>>")
s = v.get()

browse_button = ttk.Button(root, text = 'Browse', command = browser).grid(row = 1, column = 3) #launches browser function

###Destination Folder Widgets
ttk.Label(root, text = 'To Location:').grid(row = 2, column = 1, stick='e')

v1 = StringVar()
entry1 = ttk.Entry(root, width = 40, textvariable = v1).grid(row = 2, column = 2)
v1.set("Browse for the Destination Folder >>>")
s1 = v1.get()

browse_button1 = ttk.Button(root, text = 'Browse', command = browser1).grid(row = 2, column = 3) #launches browser function

###Import and Cancel Buttons
import_button = ttk.Button(root, text = 'Import', command = fileScreener, state = 'disabled')
import_button.grid(row = 3, column = 2, stick = 'e') # launches the FileScreener function
cancel_button1 = ttk.Button(root, text = 'Cancel',command = quit).grid(row = 3, column = 3) #closes the window


root.mainloop()
