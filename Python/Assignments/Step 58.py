import datetime
import os
import shutil

now = datetime.datetime.now()
source = str("C:\Users\WAaro\Desktop\All Files")
contents = os.listdir(source)
destination = "C:\Users\WAaro\Desktop\New Files"

for files in contents:
        if files.endswith(".txt"):
            modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(source + "\\" + files))
            duration = now - modified_date
            if duration.days < 1:
                shutil.copy(source + "\\" + files,destination)
                print source + "\\" + files + " moved to " +  destination + "\\" + files
                
            
#for files in source


 




##Working code to get and test file age
##============
##now = datetime.datetime.now()
##modified_date = datetime.datetime.fromtimestamp(os.path.getmtime("C:\Users\WAaro\Desktop\Folder A\Text File 1.txt"))
##duration = now - modified_date
##print duration.seconds > (24*60*60)


##Working shutil code in step 57!
