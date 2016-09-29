date = "11/12/2013"

#Go through string and split
#where there is a '/'
date_manip = date.split('/')

#Show the outcome
print date_manip

print date_manip[0]
print date_manip[1]
print date_manip[2]

print 'Month: ' + date_manip[0]
print 'Day: ' + date_manip[1]
print 'Year: ' + date_manip[2]

print('Month: ' + date_manip[0] +
      '. Day: ' + date_manip[1] +
      '. Year: ' + date_manip[2])
