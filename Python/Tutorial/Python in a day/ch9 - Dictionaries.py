#Create the list of epic programmers
epic_programmer_list = ["Tim Berners-Lee",
                        "Guido van Rossum",
                        "Linus Torvalds",
                        "Larry Page",
                        "Sergey Brin",]

#Add myself to the end of the list
epic_programmer_list.append("Me")

epic_programmer_dict = {'Tim Berners-Lee':'tbl@gmail.com',
                        'Guido van Rossum':'gvr@gmail.com',
                        'Linus Torvolds':'lt@gmail.com',
                        }
#Adds a different email address
epic_programmer_dict['Tim Berners-Lee']='tim@gmail.com'
print 'New email for Tim: ' + epic_programmer_dict['Tim Berners-Lee']

#Add Larry Page and his email to the dictionary
epic_programmer_dict['Larry Page']='lp@gmail.com'
#Add You & Sergey also
epic_programmer_dict['Sergey Brin']='sb@gmail.com'
epic_programmer_dict['Me']='me@gmail.com'
#Delete Sergey Brin from the dictionary
del epic_programmer_dict['Sergey Brin']

print epic_programmer_dict
