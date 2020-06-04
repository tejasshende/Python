
'''
This file contains all the utilities that are required to deal with date
'''

import datetime
   
## This function will format the date as per input format.
def format_date(self, currentDate, newDateFormat, seperator):
    newDate = datetime.datetime(currentDate)
    
    # checking the newDateFormat
    if newDateFormat == 'ddmmyyyy':
        return newDate.strftime()
