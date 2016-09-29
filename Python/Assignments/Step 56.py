import datetime

HQ_current_hour = datetime.datetime.now().hour
London_current_hour = HQ_current_hour+8
NYC_current_hour = HQ_current_hour+3


def OfficeOpen():
    if NYC_current_hour <= 9 or NYC_current_hour >= 21:
        NY_Status = "NYC Office: Closed"
    else:
        NY_Status = "NYC Office: Open"

    if London_current_hour <=9 or London_current_hour >= 21:
        UK_Status = "London Office: Closed"
    else:
        UK_Status = "London Office: Open"

    print str(NY_Status + "\n" + UK_Status)        
