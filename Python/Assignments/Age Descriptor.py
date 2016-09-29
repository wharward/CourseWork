#Personalized input
print("Let's see how long you have lived in dats, minutes, and seconds.")
name = raw_input ("name: ")
print("now enter your age")
age = int(raw_input("age: "))

#Conversions
days = age * 365
minutes = age * 525948     
seconds = age * 31556926

#Result
print(name, "has been alive for", days,"days", minutes, "minutes and", seconds, "seconds!  Wow!")
