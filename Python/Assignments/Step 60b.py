from tkinter import *
from tkinter import ttk
import datetime
import os
import shutil
import sqlite3
import time
import datetime

a = ['Files Moved:',"From: ","To: "]

class New_File_Getter(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.master = master
        self.master.title("New File Getter")
        #VARIABLES
        self.Time_Rec = StringVar() #For Label
        self.v = StringVar() #For Source Entry Box
        self.s = self.v.get() 
        self.v1 = StringVar() #For Destination Entry Box
        self.s1 = self.v1.get()

        self.v.set("Browse for the Source Folder >>>")
        self.v1.set("Browse for the Destination Folder >>>")

        self.Last_Ran_lbl = ttk.Label(self.master, text = self.Time_Rec)
        self.Last_Ran_lbl.grid(row = 0, column = 1, columnspan = 2, sticky='w')
##        self.Last_Ran_txt = ttk.Entry(self.master, text = self.Time_Rec)
##        self.Last_Ran_txt.grid(row = 0, column = 1)
        self.Source_lbl = ttk.Label(self.master, text = 'From Location:')
        self.Source_lbl.grid(row = 1, column = 1)
        self.Source_txt = ttk.Entry(self.master, width = 40, textvariable = self.v)
        self.Source_txt.grid(row = 1, column = 2)
        self.Source_btn = ttk.Button(self.master, text = 'Browse', command=lambda: browser(self))
        self.Source_btn.grid(row = 1, column = 3) #launches browser function
        self.Destination_lbl = ttk.Label(self.master, text = 'To Location:')
        self.Destination_lbl.grid(row = 2, column = 1, stick='e')
        self.Destination_txt = ttk.Entry(self.master, width = 40, textvariable = self.v1)
        self.Destination_txt.grid(row = 2, column = 2)
        self.Destination_btn = ttk.Button(self.master, text = 'Browse', state = 'disabled', command = lambda:browser1(self))
        self.Destination_btn.grid(row = 2, column = 3) #launches browser function
        self.import_btn = ttk.Button(self.master, text = 'Import', state = 'disabled', command = lambda:fileScreener(self))
        self.import_btn.grid(row = 3, column = 2, stick = 'e') # launches the FileScreener function        
        self.cancel_btn = ttk.Button(self.master, text = 'Cancel',command = lambda: _quit(self))
        self.cancel_btn.grid(row = 3, column = 3) #closes the window
        self.open_db()

        def _quit(self):
            self.master.destroy()

        ### Window Functions    
        def browser(self):
            dirname = filedialog.askdirectory(parent=self.master,initialdir="/",title='Please select a directory')

            self.v.set(dirname)
            self.s=self.v.get()
            if self.s:
                self.Destination_btn.config(state=NORMAL)

        def browser1(self):
            dirname = filedialog.askdirectory(parent=self.master,initialdir="/",title='Please select a directory')
            self.import_btn.config(state=NORMAL)

            self.v1.set(dirname)
            self.s1=self.v1.get()



        def fileScreener(self):
            now = datetime.datetime.now()
            source = str(self.v.get())
            contents = os.listdir(source)
            destination =str(self.v1.get())
            moved_count = 0
            a.insert(2, source)
            a.insert(4, destination)

            for files in contents:
                if files.endswith(".txt"):
                    modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(source + "\\" + files))
                    duration = now - modified_date
                    if duration.days < 1:
                        shutil.copy(source + "\\" + files,destination)
                        moved_count = moved_count + 1
                        a.append(files)
            if moved_count == 0:
                messagebox.showinfo("Result:", "No new files found")
            else:
                a.insert(1, str(moved_count))
                show_info(self)
                                    
            self.update_log()
            self.master.destroy()

        def show_info(self):
            messagebox.showinfo('Result:', "\n".join(a))
       

    ##Open Time Logging Database
    def open_db(self):
        conn = sqlite3.connect('trackerlog.db')
        with conn:
            cur = conn.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS lastRan (ID INT, unix REAL, datestamp TEXT)""")
            self.Time_Rec.set(self.last_record())
            conn.commit()
        conn.close()
        self.first_run()
        self.last_record()

    def first_run(self):
        conn = sqlite3.connect('trackerlog.db')
        with conn:
            cur = conn.cursor()
            cur.execute("""SELECT COUNT(*) FROM lastRan """)
            count = cur.fetchone()[0]
            if count < 1:
                check_date = time.time()
                cur.execute("""INSERT INTO lastRan (unix, datestamp) VALUES(?)""",(unix,))
                conn.commit()
        conn.close()
        return            
   
    def last_record(self):
        conn = sqlite3.connect('trackerlog.db')
        with conn:
            cur = conn.cursor()
            cur.execute("""SELECT max(datestamp) FROM lastRan""")
            data = cur.fetchone()[0]
            legible = data
        self.Last_Ran_lbl.config(text="Last Ran: " + legible)
##        self.Time_Rec.set(legible)
        conn.close()
                          
    def update_log(self):
        conn = sqlite3.connect('trackerlog.db')
        with conn:
            cur = conn.cursor()
            unix = time.time()
            date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
            cur.execute("""INSERT INTO lastRan (unix, datestamp) VALUES(?,?)""",
                      (unix, date))
            conn.commit()
        conn.close()


if __name__ == "__main__":
    root = Tk()
    App = New_File_Getter(root)
    root.mainloop()

