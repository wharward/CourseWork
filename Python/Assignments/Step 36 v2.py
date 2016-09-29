#MODULES
import time 

#TUPLE:required variables list
var_tup = ("name", "current_age", "retirement_age", "death_age", "m_exp", "before_rate","after_rate")

#TEST DICTIONARY:variable name: [question, (default) value, test]
dictionary = {
    "name":
        ["What is your name? ",
         str("Bob"),
         "undefined"],
    "current_age":["How old are you? ",int(0)],
    "retirement_age":["What age do you want to retire? ",int(0)],
    "death_age":["What age are you planning to live to? ",int(0)],
    "m_exp":["How much are your monthly expenses? ",float(0)],
    "before_rate":["What is the estimated average APR(%) BEFORE retirement? ( Choose 0 to 30)",float(0)/100],
    "after_rate":["What is the estimated average APR(%) AFTER retirement? ( Choose 0 to 30)",float(0)/100],
    }

#FUNCTIONS
# 'r_amt' function: calculates retirement amount
# 'cont_amt' function: calculates monthly contribution to get that retirement.
def r_amt(m_exp, after_rate, retirement_age, death_age): 
    calc = (m_exp/(after_rate/12))*(1-(1/((1+(after_rate/12))**((death_age-retirement_age)*12))))
    return float('{0:.2f}'.format(calc))
def cont_amt(ret_amt, before_rate,retirement_age,current_age):
    calc = (ret_amt*(before_rate/12))/(((1+(before_rate/12))**(12*(retirement_age-current_age)))-1)
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

#Integer Tests
for q in range(1, 4):
    while True:
            try:
                dictionary[var_tup[q]][1]=int(raw_input(dictionary[var_tup[q]][0]))
                q =+ 1
                #more opportunties for conditional functions to insert here                
                break
            except ValueError:
                print "Sorry, I only understand numbers. Try again..." + "\n"

print "Ok. Just a few more questions:"

#Float Tests
for q in range(4, 7):
    while True:
            try:
                dictionary[var_tup[q]][1]=float(raw_input(dictionary[var_tup[q]][0]))
                q =+ 1
                #more opportunties for conditional functions to insert here                
                break
            except ValueError:
                print "Sorry, I only understand numbers. Try again..." + "\n"

print "Thank you! That's all I needed! "+ "\n" + "Calculating..."

r_amt(dictionary["m_exp"][1], dictionary["after_rate"][1]/100, dictionary["retirement_age"][1], dictionary["death_age"][1])
ret_amt = r_amt(dictionary["m_exp"][1], dictionary["after_rate"][1]/100, dictionary["retirement_age"][1], dictionary["death_age"][1])

#END RESULTS
time.sleep(2.5)
print "Ok, are you ready?"
time.sleep(2.5)
print "\n"+ name + ", assuming your monthly expenses stay exactly the same,"
time.sleep(1.5)
print "and not including taxes,"
time.sleep(1.5)
print "you need "+ "{:,}".format(ret_amt) +" for retirement."
time.sleep(1.5)
print "\n"+"Keep in mind, any inflation needs to be added to your savings interest rate." + "\n"
#pause added for effect
time.sleep(3)

ret_pmt = cont_amt(ret_amt, dictionary["before_rate"][1]/100,dictionary["retirement_age"][1],dictionary["current_age"][1])
print "Now, if you have zero savings,"
time.sleep(1.5)
print "to acheive that goal,"
time.sleep(1.5)
print "you need to contribute "+ "{:,}".format(ret_pmt) +" monthly"
time.sleep(1.5)
print " to your retirement fund."
#print "You need to contribute " + save_amt + " a month to reach this goal!"

print "\n" + "I hope that was helpful! Good luck!"  
