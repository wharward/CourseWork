#Create the list of epic programmers
epic_programmer_list = ["Tim Berners-Lee",
                        "Guido van Rossum",
                        "Linus Torvalds",
                        "Larry Page",
                        "Sergey Brin",]

#Add myself to the end of the list
epic_programmer_list.append("Me")

#Looping through each item in epic_programmer_list
for programmer in epic_programmer_list:
    #Print the programmers' name to the console
    print "An epic prgorammer:" + programmer

#Create a list of numbers
    number_list = [1,2,3,4,5]
    empty_list = []
#Loop each number in number_list
    for x in number_list:
        #Append each number to the power of 2
        empty_list.append(x**2)

print empty_list
