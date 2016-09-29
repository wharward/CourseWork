from tkinter import *
from tkinter import ttk
import datetime
import os
import shutil

def browser():
    root = Tk()
    root.withdraw()
    dirname = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
    import_button.state(['!disabled'])

    v.set(dirname)
    s=v.get


def fileScreener():
    now = datetime.datetime.now()
    source = str(v.get())
    contents = os.listdir(source)
    destination =('C:\\Users\\WAaro\\Desktop\\New Files')

    for files in contents:
        if files.endswith(".txt"):
            modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(source + "\\" + files))
            duration = now - modified_date
            if duration.days < 1:
                shutil.copy(source + "\\" + files,destination)
                print (source + "\\" + files + " moved to " +  destination + "\\" + files)

    root.destroy()
    exit(code=None)

def quit():
    root.destroy()
    
root = Tk("Choose a folder")
ttk.Label(root, text = 'Folder Location:').grid(row = 1, column = 1)

v = StringVar()
entry = ttk.Entry(root, width = 30, textvariable = v).grid(row = 1, column = 2)
v.set("Browse to Select a Folder >>>")
s = v.get()

browse_button = ttk.Button(root, text = 'Browse', command = browser).grid(row = 1, column = 3) #launches browser function
import_button = ttk.Button(root, text = 'Import', command = fileScreener, state = 'disabled')
import_button.grid(row = 2, column = 2, stick = 'e') # launches the FileScreener function
cancel_button1 = ttk.Button(root, text = 'Cancel',command = quit).grid(row = 2, column = 3) #closes the window


root.mainloop()
