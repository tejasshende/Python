#!/ms/dist/python/PROJ/core/2.7.3/bin/python

'''
Documentation of Script

# Date - 19-July-2016
# Owenr - Tejas Shende
# Python Version - 2.6.6
# Purpose -  This script is launcher script for SMARTS-Automation
'''

## Importing the packages / classes from W:/SMARTSAutomation dir
from SMARTSAutomationFunctionsLib import SMARTSAutomation
from outputTableComparision import outputTableCompare
#from filterDataFromInput import filterInputData

import ms.version
ms.version.addpkg('numpy', '1.7.1-mkl')
ms.version.addpkg('pandas', '0.13.0')
ms.version.addpkg('dateutil', '1.5')
ms.version.addpkg('xlrd', '0.9.2')
ms.version.addpkg('openpyxl', '1.8.5')

import openpyxl.reader.excel
import pandas as pd
import openpyxl
import os
import time
import datetime

class launchSMARTSAutomation(object):
	
	dir = os.getcwd()
	
	## Reading the input file
	filename = openpyxl.reader.excel.load_workbook(dir + '//SMARTSAutomation_Inputs.xlsx')
	sheet = filename.get_sheet_by_name('compareQAvsPROD')
	
	## Setting up the input values in variable
	sourceQAPath = sheet['B2'].value
	sourceProdPath = sheet['B3'].value
	region = sheet['B4'].value
	busDt = sheet['B5'].value
	
	#sheet.close()
	
	## Reading the Input Excel values into Dictionary
	shtCompareDict, shtInpFileDict, shtDervFileDict = {}, {}, {}
		
	shtCompareDict = pd.read_excel(dir + r'/SMARTSAutomation_Inputs.xlsx',
								 sheetname = 'compareQAvsPROD',
								 header = 0,
								 index_col = 0,
								 parse_cols = 'A, B').to_dict()
	
	# shtInpFileDict = pd.read_excel(dir + r'/SMARTSAutomation_Inputs.xlsx',
								 # sheetname = 'inputFileFilters',
								 # header = 0,
								 # index_col = 0,
								 # parse_cols = 'A, B').to_dict()
								 
	# shtDervFileDict = pd.read_excel(dir + r'/SMARTSAutomation_Inputs.xlsx',
								 # sheetname = 'derivedFileFilters',
								 # header = 0,
								 # index_col = 0,
								 # parse_cols = 'A, B').to_dict()
								 
	# print (shtCompareDict)
	# print (shtInpFileDict)
	# print (shtDervFileDict)
	
	## setting target paths
	targetQAPath = dir + '/' + 'QA' + '/' + region + '/' + busDt
	targetPRODPath = dir + '/' + 'PROD' + '/' + region + '/' + busDt
	
	## Creating object of SMARTSAutomationFunctionsLib.SMARTSAutomation
	smauto = SMARTSAutomation()
	optbl = outputTableCompare()
	#fltrdt = filterInputData()
	
	print('Script Execution started on... ', str(datetime.datetime.now()))
	time.sleep(2)
	
	print('''
		  ------------------------------------------------------------------
			This script will...
				* Create QA and PROD folder structure.
				* Copy QA and PROD output files.
				* Format .CSV output files to convert into .TXT
				* Create database tables for copied output files.
				* Load Data into Database tables.
				* Execute compare queries.
				* Display result of mismatch samples.
				* Save the result in proper excel sheet.
		  ------------------------------------------------------------------
		  ''')
	
	## Calling function checkDirectories for QA & PROD
	smauto.checkDirectories('QA', region, busDt)
	smauto.checkDirectories('PROD', region, busDt)

	# ## Calling copySourceFile function for QA & PROD
	smauto.copySourceFiles('QA', sourceQAPath, targetQAPath)
	smauto.copySourceFiles('PROD', sourceProdPath, targetPRODPath)
	
	# ## Calling formatFiles function for QA & PROD
	smauto.formatFiles ('QA', targetQAPath) 
	smauto.formatFiles ('PROD', targetPRODPath) 
	
	# ## Calling createTables function for QA & PROD
	smauto.createTables('QA', region, busDt, targetQAPath)
	smauto.createTables('PROD', region, busDt, targetPRODPath)
	
	# ## Calling loadTables function for QA & PROD
	smauto.loadTables('QA', region, busDt, targetQAPath)
	smauto.loadTables('PROD', region, busDt, targetPRODPath)
	
	# ## Calling verifyEnterTable function for QA & PROD
	optbl.verifyEnterTable(region, busDt)
	optbl.verifyAmendTable(region, busDt)
	optbl.verifyDeletTable(region, busDt)
	optbl.verifyTradeTable(region, busDt)
	
	# ## Calling generateReport function for QA & PROD
	optbl.generateReport(region, busDt)
	
	## Calling The sum Up function
	optbl.sumUpValues(region, busDt)
	
	## Calling the getMismatchSamples function
	optbl.getMismatchSamples(region, busDt)
	
	## For database verification
	# -- QA
	# /*
	# DROP TABLE LC.SMARTS_ENTER_QA_SPAIN_0714;
	# DROP TABLE LC.SMARTS_TRADE_QA_SPAIN_0714;
	# DROP TABLE LC.SMARTS_DELET_QA_SPAIN_0714;
	# DROP TABLE LC.SMARTS_CANTR_QA_SPAIN_0714;
	# */

	# -- PROD
	# /*
	# DROP TABLE LC.SMARTS_OFFTR_QA_SPAIN_0714;
	# DROP TABLE LC.SMARTS_ENTER_PROD_SPAIN_0714;
	# DROP TABLE LC.SMARTS_TRADE_PROD_SPAIN_0714;
	# DROP TABLE LC.SMARTS_DELET_PROD_SPAIN_0714;
	# DROP TABLE LC.SMARTS_CANTR_PROD_SPAIN_0714;
	# DROP TABLE LC.SMARTS_OFFTR_PROD_SPAIN_0714;
	# */
	
	print('Script Execution completed on -------', str(datetime.datetime.now()))
	