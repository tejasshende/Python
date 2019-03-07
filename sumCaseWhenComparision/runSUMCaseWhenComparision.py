#!/ms/dist/python/PROJ/core/2.7.3/bin/python

'''
Documentation of Script

# Date - 10-Feb-2017
# Owner - Tejas Shende
# Python Version - 2.7.3
# Purpose - This script will run the sumCaseWhenComparision file
'''
import datetime
import time

from sumCaseWhenComparision import sumCaseWhenComparision

class runsumCaseWhenComparision(object):

	try:
		print('Script Execution started on... ' + str(datetime.datetime.now()))
		time.sleep(2)
		
		print('''
		  ------------------------------------------------------------------
			This script will...
				* Prepare dynamic SUM CASE WHEN SQL queries like...
						~ QA IS NULL & PROD IS NOT NULL
						~ QA IS NOT NULL & PROD IS NULL
						~ QA = PROD
						~ QA IS NULL & PROD IS NULL
				* Execute the SUM CASE WHEN queries.
				* Get the count of mismatch records.
				* Generate the report with mismatch samples is excel sheet.
		  ------------------------------------------------------------------
		  ''')
		
		##Creating the object of sumCaseWhenComparision Class
		sumCase = sumCaseWhenComparision()
		
		##Calling the Function QA IS NULL & PROD IS NOT NULL
		sumCase.qaIsNullProdIsNotNull()
		
		##Calling the function QA IS NOT NULL & PROD IS NULL
		sumCase.qaIsNotNullProdIsNull()
		
		##Calling the function QA = PROD
		sumCase.qaEqualToProd()
		
		##Calling the function QA IS NULL & PROD IS NULL
		sumCase.qaIsNullProdIsNull()
		
		##Calling the getMatchingCount function
		sumCase.getMatchingRowCount()
		
		##Calling function Sum Up Values
		sumCase.sumUpValues()
		
		##Calling the function getMismatchSamples
		sumCase.getMismatchSamples()
		
		##This function will generate the final report
		sumCase.generateReport()
		
		##Calling the function Remove Temp file
		sumCase.removeTempFile()
		
		##Calling the DB Connection Close function
		sumCase.closeDBCon
		
		print('Script Execution completed on -------' + str(datetime.datetime.now()))
		
	except Exception as e:
		print(e)
		sumCase.closeDBCon
