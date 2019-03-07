#!/ms/dist/python/PROJ/core/2.7.3/bin/python

'''
Documentation of Script

# Date - 26-Sep-2016
# Owenr - Tejas Shende
# Python Version - 2.6.6
# Purpose -  This script will filter data from given input file
'''

import ms.version

ms.version.addpkg("ibm_db","2.0.4-9.5.5") 
ms.version.addpkg("ms.db2","1.0.3")        # specify which ms.db2 module want to use 
ms.version.addpkg("ms.modulecmd", "1.0.4") # we will use ms.modulecmd to module load ibmdb2/client/9.5.5 
import ms.modulecmd
ms.modulecmd.load("ibmdb2/client/9.5.5") # load the module

ms.version.addpkg('numpy', '1.7.1-mkl')
ms.version.addpkg('pandas', '0.13.0')
ms.version.addpkg('dateutil', '1.5')
ms.version.addpkg('xlrd', '0.9.2')
ms.version.addpkg('openpyxl', '1.8.5')

import ibm_db
import ms.db2 #import the ms.db2 module
import os, sys, shutil, openpyxl
import pandas as pd

global folders
global basePath
global srcPath
global fileList

class filterInputData(object):
	
	dir = os.getcwd()
	
	try:
	
		#fileList = ['amend.csv','cantr.csv','delet.csv','enter.csv','offtr.csv','trade.csv']
		
		shtCompareDict, shtInpFileDict, shtDervFileDict = {}, {}, {}
		
		shtCompareDict = pd.read_excel(dir + r'/SMARTSAutomation_Inputs.xlsx',
									 sheetname = 'compareQAvsPROD',
									 header = 0,
									 index_col = 0,
									 parse_cols = 'A, B').to_dict()
		
		shtInpFileDict = pd.read_excel(dir + r'/SMARTSAutomation_Inputs.xlsx',
									 sheetname = 'inputFileFilters',
									 header = 0,
									 index_col = 0,
									 parse_cols = 'A, B').to_dict()
									 
		shtDervFileDict = pd.read_excel(dir + r'/SMARTSAutomation_Inputs.xlsx',
									 sheetname = 'derivedFileFilters',
									 header = 0,
									 index_col = 0,
									 parse_cols = 'A, B').to_dict()
									 
		# print (shtCompareDict)
		# print (shtInpFileDict)
		# print (shtDervFileDict)
		
		dbcon = ms.db2.connect(shtInpFileDict['values']['databaseName']) 
		dbcur = dbcon.cursor()
		
		basePath = os.getcwd()
		#srcPath = shtInpFileDict['values']['inputFilePath']
		folders = os.listdir(dir)
		databaseName = shtInpFileDict['values']['databaseName']
		
		def __init__(self):
			pass
		
		def main(self):
			sys.exit(0)
			print("The main function says - This module can't be run as standalone")
		
		def checkSourceFiles(self, srcPath, region, busDt):
			print ('Checking source files...')
			os.chdir(srcPath)
			
		#Checking ORDERS_<region>_<busDt>.ZIP / ORDERS_<region>_<busDt>.TXT files are available
			srcDir = os.getcwd()
			files = os.listdir(srcDir)
			#print files
			i = 1
			while(i < 13):
				if 'ORDERS_EU_EXTRACT' + str(i) + '_' + busDt + '.TXT' in files:
					print ('ORDERS_EU_EXTRACT' + str(i) + '_' + busDt + '.TXT')
				else:
					print('The ORDERS source files are not availalble')
				i+=1
				
		#Checking ORDERS_<region>_GTC_<busDt>.ZIP / ORDER_<region>_GTC_<busDt>.TXT files are available
			srcDir = os.getcwd()
			files = os.listdir(srcDir)
			
			i = 1
			while(i < 13):
				if 'ORDERS_EU_GTC_EXTRACT' + str(i) + '_' + busDt + '.TXT' in files:
					print ('ORDERS_EU_GTC_EXTRACT' + str(i) + '_' + busDt + '.TXT')
				else:
					print('The ORDERS GTC source files are not availalble')
				i+=1
		
		#Checking TARDE_<region>_<busDt>.ZIP / TRADES_<region>_<busDt>.TXT files are available
			srcDir = os.getcwd()
			files = os.listdir(srcDir)
			
			i = 1
			while(i < 13):
				if 'TRADES_EU_EXTRACT' + str(i) + '_' + busDt + '.TXT' in files:
					print ('TRADES_EU_EXTRACT' + str(i) + '_' + busDt + '.TXT')
				else:
					print('The TRADES source files are not availalble')
				i+=1
					
		#Checking TRADES_<region>_GTC_<busDt>.ZIP / TRADES_<region>_GTC_<busDt>.TXT files are available
			srcDir = os.getcwd()
			files = os.listdir(srcDir)

			i = 1
			while(i < 13):
				if 'TRADES_EU_GTC_EXTRACT' + str(i) + '_' + busDt + '.TXT' in files:
					print ('TRADES_EU_GTC_EXTRACT' + str(i) + '_' + busDt + '.TXT')
				else:
					print('The TRADES GTC source files are not availalble')
				i+=1

		def copyInputFiles(self, srcPath, destPath = None):
			os.chdir(srcPath)
			dbColumns = os.system("head -1 TRADES_EU_GTC_EXTRACT10_20161003.TXT|sed  -e 's/,/ /g' -e 's/~|/ VARCHAR(200),/g'")
			dbColumns = str(dbColumns) + ' VARCHAR(200)'
			print(dbColumns)
			#dbColumns = str(dbColumns).replace('0 VARCHAR(200)', ' VARCHAR(200)')
			print ('''
						  CREATE TABLE LC.SMARTS_XETRA_Automation
						  (
						  '''
						  +
						  str(dbColumns).replace('0 VARCHAR(200)', ' VARCHAR(200)')
						  +
						  '''
						  )
							IN TS_APPDAT_FACT_16K
							INDEX IN TS_APPIX_FACT_16K
							DISTRIBUTE BY HASH (ORDER_ID) COMPRESS YES
					''')
			
			#Creating tables
			
			# filterInputData.dbcur.execute
						# (
						  # '''
						  # CREATE TABLE LC.SMARTS_XETRA_Automation
						  # (
						  # '''
						  # +
						  # dbColumns
						  # +
						  # '''
						  # )
							# IN TS_APPDAT_FACT_16K
							# INDEX IN TS_APPIX_FACT_16K
							# DISTRIBUTE BY HASH (ORDER_ID) COMPRESS YES
					# ''')
			# filterInputData.dbcon.commit()
		
		
		if(__name__ == '__main__'):
			__call__ = main()
		else:
			pass
	
	
	
	except Exception as e:
		print (e)