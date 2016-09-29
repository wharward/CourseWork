import shutil
import os

def TextFileTransfer():  
    source = str("C:\Users\WAaro\Desktop\Folder A")
    contents = os.listdir(source)
    destination = "C:\Users\WAaro\Desktop\Folder B"
    for files in contents:
        if files.endswith(".txt"):
            shutil.move(source + "\\" + files,destination)
            print source + "\\" + files + " moved to " +  destination + "\\" + files
            
