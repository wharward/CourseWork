#MODULES
from time import sleep

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

#QUESTIONS
while True:
    try:
        current_age = int(input("How old are you? "))
        break
    except ValueError:
        print("Sorry, I only understand numbers. Try again...")+ "\n"
while True:
    try:
        retirement_age = int(raw_input("What age do you want to retire? "))
        #check if retirement age is younger than current age
        if current_age > retirement_age:
            print "You can't plan retirement for the past, "+name+" !!!" + "\n" + "Please choose a retirement age, older than your current age."
            ValueError
        break
    except ValueError:
        print("Sorry, I only understand numbers. Try again...")+ "\n"
while True:
    try:
        death_age = int(raw_input("What age are you planning to live to? "))
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
        if death_age < current_age OR death_age < retirement_age
            print "If you're dead before you decide to retire, then you don't need any savings. Try again!"
        break
    except ValueError:
        print "Sorry, I only understand numbers. Try again..." + "\n"
                                

    
#other inputs needed
print "Ok. Just a few more questions:"
m_exp = float(raw_input("How much are your monthly expenses? "))
before_rate = float(raw_input("What is the average interest rate do you expect to earn BEFORE you retire? (0 to 30)"))/100
after_rate = float(raw_input("What is the average interest rate do you expect to earn AFTER you retire? (0 to 30)"))/100
print "Thank you! That's all I needed!"

r_amt(m_exp, after_rate, retirement_age, death_age)
ret_amt = r_amt(m_exp, after_rate, retirement_age, death_age)
print "Got it! Calcualating..."

#END RESULTS
time.sleep(2.5)
print "Ok, are you ready?"
time.sleep(2.5)
print name + ", assuming your monthly expenses stay exactly the same,"+"\n"+"and not including taxes,"+"\n"+"you need "+ "{:,}".format(ret_amt) +" for retirement."
print "Keep in mind, any inflation needs to be added to your savings interest rate." + "\n"
#pause added for effect
time.sleep(3)
ret_pmt = cont_amt(ret_amt, before_rate,retirement_age,current_age)
print "Now, if you have zero savings,"+"\n"+"to acheive that goal,"+"\n"+"you need to contribute "+ "{:,}".format(ret_pmt) +" monthly"+"\n"+" to your retirement fund."
#print "You need to contribute " + save_amt + " a month to reach this goal!"

print "\n" + "I hope that was helpful! Good luck!"  
    
