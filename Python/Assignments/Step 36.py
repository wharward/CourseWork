#MODULES

import time

#VARIABLES

#current_age=int()
#retirement_age=int()
#death_age=int()

#LISTS

#List of questions
ret_questions  = [
    "How old are you? ",
    "What age do you want to retire? ",
    "What age are you planning to live to? ",
    ]

#List of inputs
ret_inputs = [int(current_age),int(retirement_age),int(death_age)]

#FUNCTIONS
# 'r_amt' function: calculates retirement amount

def r_amt(m_exp, after_rate, retirement_age, death_age): 
    calc = (m_exp/(after_rate/12))*(1-(1/((1+(after_rate/12))**((death_age-retirement_age)*12))))
    return float('{0:.2f}'.format(calc))

#BEGIN PROGRAM
#Get the users name
name = str.title(raw_input ("What is your name? "))

print "\n" + "Welcome, "+ name + "!"
print "This program is designed to help you discover how much you need for retirement."+"\n"

#Get permission to ask questions
#This part of the program loops until the boolean:'starter' gets changed or kills the app
starter = True
while starter == True:
    play_inquiry = raw_input(name + ", can I ask you a few questions? ")
    if play_inquiry == 'y':
        print "\n" + "Great. Then let's begin..." + "\n"
        #Changes 'starter' to end the loop
        starter = False
    elif play_inquiry == 'n':
        print "Ok. Maybe later, then. Bye!"
        exit()
    else:
        #if not results other than 'y' or 'n' then the loop restarts
         print "Sorry, please type either 'y' for yes, or 'n' for no."

#'q' means question, 'i' means input calling the age data 
for q in range(0, 3):
    i=0
    while True:
            try:
                ret_inputs[i] = int(raw_input(ret_questions[q]))
                q =+ 1
                i =+ 1
                #more opportunties for conditional functions to insert here
                break
            except ValueError:
                print "Sorry, I only understand numbers. Try again..." + "\n"

# just a humourous blurb to give a more human feel.
if death_age > 90:
    print "\n" + "hmmm..."
    time.sleep(2.5)
    print "That's pretty old, "+name+"..."
    time.sleep(1)
    print "..."
    time.sleep(1)
    print "\n" + "Ha ha! Just kidding!" + "\n"
    time.sleep(.5)
    print "Anyway..."
    
#other inputs needed
print "Ok. Just a few more questions:"
m_exp = float(raw_input("How much are your monthly expenses? "))
before_rate = float(raw_input("What is the average interest rate do you expect to earn BEFORE you retire? (0 to 30)"))/100
after_rate = float(raw_input("What is the average interest rate do you expect to earn AFTER you retire? (0 to 30)"))/100
print "Thank you! That's all I needed!"

r_amt(m_exp, after_rate, retirement_age, death_age)
return_value = r_amt(m_exp, after_rate, retirement_age, death_age)
time.sleep(2.5)
print "Ok, are you ready?"
time.sleep(2.5)
print name + ", you need "+ return_value +" for retirement."

# insert 'contribution needed' calc here


# End Result

#print "You need to contribute " + save_amt + " a month to reach this goal!"

    
