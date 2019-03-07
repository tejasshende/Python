#!/ms/dist/python/PROJ/core/2.7.3/bin/python

'''
Documentation of Script

# Date - 19-July-2016
# Owenr - Tejas Shende
# Python Version - 2.6.6
# Purpose -  This script is a function library for SMARTS Automation
'''

import ms.version

ms.version.addpkg("ibm_db","2.0.4-9.5.5") 
ms.version.addpkg("ms.db2","1.0.3")        # specify which ms.db2 module want to use 
ms.version.addpkg("ms.modulecmd", "1.0.4") # we will use ms.modulecmd to module load ibmdb2/client/9.5.5 
import ms.modulecmd
ms.modulecmd.load("ibmdb2/client/9.5.5") # load the module 

import ibm_db
import ms.db2 #import the ms.db2 module
import os
import shutil

global folders
global basePath
global fileList

class SMARTSAutomation(object):

	try:
		
		## Creating a list of files present for comparision
		fileList = ['amend.csv','cantr.csv','delet.csv','enter.csv','offtr.csv','trade.csv']
		databaseName = 'NYTD_LCDMart'

		basePath = os.getcwd()

		dir = os.getcwd()
		folders = os.listdir(dir)
		
		## This function will check the QA & PROD directory structure exists or not, it will create if its not exists
		def checkDirectories(self, environment, region, busDt):
			
			print ('Checking ' + environment + ' folder Structure...')
			os.chdir(SMARTSAutomation.basePath)
			SMARTSAutomation.folders = os.listdir(SMARTSAutomation.basePath)
			
			if environment in SMARTSAutomation.folders:
				print('        Folder %s exists' %environment)
				os.chdir(environment)
			else:
				print('        Creating folder %s' %environment)
				os.mkdir(environment)
				os.chdir(environment)
				
			if (environment == 'QA'):
				qaDir = os.getcwd()
			else:
				prodDir = os.getcwd()

				##### Checking the region folder exists or not #####
				
			if (environment == 'QA'):
				SMARTSAutomation.folders = os.listdir(qaDir)
			else:
				SMARTSAutomation.folders = os.listdir(prodDir)

			if region in SMARTSAutomation.folders:
				print('        Folder %s exists' %region)
				os.chdir(region)
			else:
				print('        Creating folder %s' %region)
				os.mkdir(region)
				os.chdir(region)
				
			if (environment == 'QA'):
				qaRegionDir = os.getcwd()
			else:
				prodRegionDir = os.getcwd()
				
				#### Checking date folder exists or not ####
				
			if (environment == 'QA'):
				SMARTSAutomation.folders = os.listdir(qaRegionDir)
			else:
				SMARTSAutomation.folders = os.listdir(prodRegionDir)

			if busDt in SMARTSAutomation.folders:
				print('        Folder %s exists' %busDt)
				os.chdir(busDt)
			else:
				print('        Creating folder %s' %busDt)
				os.mkdir(busDt)
				os.chdir(busDt)
				
			if (environment == 'QA'):
				targetQAPath = os.getcwd()
			else:
				targetProdPath = os.getcwd()
		
			os.chdir(SMARTSAutomation.basePath)
			
			##### Copying the files in QA folder #####
		
		## This function will copy the Source file to target
		def copySourceFiles(self, environment, sourcePath, targetPath):
			os.chdir(sourcePath)
			SMARTSAutomation.folders = os.listdir(sourcePath)
			
			print ('Copying ' + environment + ' source files...')

			if 'amend.csv' in SMARTSAutomation.folders:
				shutil.copy2(sourcePath + '//amend.csv', targetPath)

			if 'delet.csv' in SMARTSAutomation.folders:
				shutil.copy2(sourcePath + '//delet.csv', targetPath)
				
			if 'offtr.csv' in SMARTSAutomation.folders:
				shutil.copy2(sourcePath + '//offtr.csv', targetPath)
				
			if 'trade.csv' in SMARTSAutomation.folders:
				shutil.copy2(sourcePath + '//trade.csv', targetPath)
				
			if 'enter.csv' in SMARTSAutomation.folders:
				shutil.copy2(sourcePath + '//enter.csv', targetPath)
				
			if 'cantr.csv' in SMARTSAutomation.folders:
				shutil.copy2(sourcePath + '//cantr.csv', targetPath)
			
			os.chdir(targetPath)
			SMARTSAutomation.folders = os.listdir(targetPath)
			
			## Checking & displaying which files are copied
			for i in SMARTSAutomation.folders:
				if i in SMARTSAutomation.fileList:
					print('''	%s file copied successfully''' %i)
			
		## This function will remove "comma, space, ~" & replace it with comma & save file with .TXT extension
		def formatFiles(self, environment, targetPath):
		
			print ('File formating started...')
			os.chdir(targetPath)
			SMARTSAutomation.folders = os.listdir(targetPath)
			
			## amend.csv --> amend.txt
			if 'amend.csv' in SMARTSAutomation.folders:
				os.system("sed  -e 's/,/ /g' -e 's/|/,/g' -e 's/\~/ /g' amend.csv > amend_conv.TXT")
			
			## delet.csv --> delet.txt
			if 'delet.csv' in SMARTSAutomation.folders:
				os.system("sed  -e 's/,/ /g' -e 's/|/,/g' -e 's/\~/ /g' delet.csv > delet_conv.TXT")

			## enter.csv --> enter.txt
			if 'enter.csv' in SMARTSAutomation.folders:
				os.system("sed  -e 's/,/ /g' -e 's/|/,/g' -e 's/\~/ /g' enter.csv > enter_conv.TXT")

			## trade.csv --> trade.txt
			if 'trade.csv' in SMARTSAutomation.folders:
				os.system("sed  -e 's/,/ /g' -e 's/|/,/g' -e 's/\~/ /g' trade.csv > trade_conv.TXT")

			## offtr.csv --> offtr.txt
			if 'offtr.csv' in SMARTSAutomation.folders:
				os.system("sed  -e 's/,/ /g' -e 's/|/,/g' -e 's/\~/ /g' offtr.csv > offtr_conv.TXT")

			## cantr.csv --> cantr.txt
			if 'cantr.csv' in SMARTSAutomation.folders:
				os.system("sed  -e 's/,/ /g' -e 's/|/,/g' -e 's/\~/ /g' cantr.csv > cantr_conv.TXT")
			
			
			print ('	All ' + environment + ' CSV files successfully converted to TXT')

		## This function will create blank Database Tables
		def createTables(self, environment, region, busDt, targetPath):
			
			print ('Hand-shaking with Database to create table schema...')
			os.chdir(targetPath)
			SMARTSAutomation.folders = os.listdir(targetPath)
			
			## Checking ENTER.TXT file is available or not, if it is available then it will create table
			if 'enter_conv.TXT' in SMARTSAutomation.folders:
				dbcon = ms.db2.connect(SMARTSAutomation.databaseName) 
				dbcur = dbcon.cursor()
				dbcur.execute(
						  '''
						  CREATE TABLE LC.SMARTS_ENTER_''' + environment + '_' + region + '_' + busDt +
						  '''
						  (
							EXCHANGE_ID VARCHAR(100),
							MESSAGE_TYPE VARCHAR(100),
							DATE1 VARCHAR(100),
							TIME1 VARCHAR(100),
							ORDER_ID VARCHAR(100),
							MARKET_SIDE VARCHAR(100),
							SECURITY VARCHAR(100),
							PRICE VARCHAR(100),
							QUANTITY VARCHAR(100),
							UNDISCLOSED_VOL VARCHAR(100),
							VALUE1 VARCHAR(100),
							ORDER_FLAGS VARCHAR(100),
							ACCOUNT VARCHAR(100),
							ACCOUNTTYPE VARCHAR(100),
							BROKER VARCHAR(100),
							TRADER VARCHAR(100),
							ORDER_TYPE  VARCHAR(100),
							PARENT_ORDER_ID VARCHAR(100),
							EXECUTION_INSTRCUTIONS VARCHAR(100),
							ORDER_RECEIVE_DATE VARCHAR(100),
							ORDER_RECEIVE_TIME VARCHAR(100),
							OTHER VARCHAR(100),
							ISIN VARCHAR(100)
							)'''
							
							'''
							IN TS_APPDAT_FACT_16K
							INDEX IN TS_APPIX_FACT_16K
							DISTRIBUTE BY HASH (ORDER_ID) COMPRESS YES
					''')
				dbcon.commit()		
				print('        ' + environment + ' - ENTER table created Successfully')
			else:
				print('        ' + environment + " - File ENTER.TXT doesn't exists")
			
			## Checking AMEND.TXT file is available or not, if it is available then it will create table
			if 'amend_conv.TXT' in SMARTSAutomation.folders:
				dbcon = ms.db2.connect(SMARTSAutomation.databaseName) 
				dbcur = dbcon.cursor()
				dbcur.execute('''
								CREATE TABLE LC.SMARTS_AMEND_''' + environment + '_' + region + '_' + busDt +
							  '''(	
									EXCHANGE_ID VARCHAR(100),
									MESSAGE_TYPE VARCHAR(100),
									DATE1 VARCHAR(100),
									TIME1 TIME,
									ORDER_ID VARCHAR(100),
									NEW_ORDER_ID VARCHAR(100),
									MARKET_SIDE VARCHAR(100),
									SECURITY VARCHAR(100),
									PRICE VARCHAR(100),
									QUANTITY VARCHAR(100),
									UNDISCLOSED_VOL VARCHAR(100),
									VALUE1 VARCHAR(100),
									ORDER_FLAGS VARCHAR(100),
									ORDER_TYPE  VARCHAR(100),
									PARENT_ORDER_ID VARCHAR(100),
									EXECUTION_INSTRCUTIONS VARCHAR(100),
									AMEND_RECEIVE_DATE VARCHAR(100),
									AMEND_RECEIVE_TIME TIME,
									OTHER VARCHAR(100)
								) '''
								
							  '''
								IN TS_APPDAT_FACT_16K
								INDEX IN TS_APPIX_FACT_16K
								DISTRIBUTE BY HASH (NEW_ORDER_ID) COMPRESS YES 
					''')
				dbcon.commit()
				print('        ' + environment + ' - AMEND table created Successfully')
			else:
				print('        ' + environment + " - File AMEND.TXT doesn't exists")
			
			## Checking DELET.TXT file is available or not, if it is available then it will create table
			if 'delet_conv.TXT' in SMARTSAutomation.folders:
				dbcon = ms.db2.connect(SMARTSAutomation.databaseName) 
				dbcur = dbcon.cursor()
				dbcur.execute('''
								CREATE TABLE LC.SMARTS_DELET_''' + environment + '_' + region + '_' + busDt +
							  '''(
									EXCHANGE_ID         VARCHAR(100),
									MESSAGE_TYPE        VARCHAR(100),
									DATE1               VARCHAR(100),
									TIME1               VARCHAR(100),
									ORDER_ID            VARCHAR(100),
									MARKET_SIDE         VARCHAR(100),
									SECURITY            VARCHAR(100),
									ORDER_TYPE          VARCHAR(100),
									PARENT_ORDER_ID     VARCHAR(100),
									DELETE_RECEIVE_DATE VARCHAR(100),
									DELETE_RECEIVE_TIME VARCHAR(100)
								) '''
							'''
							IN TS_APPDAT_FACT_16K
							INDEX IN TS_APPIX_FACT_16K
							DISTRIBUTE BY HASH (ORDER_ID)  COMPRESS YES
				''' )
				dbcon.commit()
				print('        ' + environment + ' - DELET table created Successfully')
			else:
				print('        ' + environment + " - File AMEND.TXT doesn't exists")
			
			## Checking TRADE.TXT file is available or not, if it is available then it will create table
			if 'trade_conv.TXT' in SMARTSAutomation.folders:
				dbcon = ms.db2.connect(SMARTSAutomation.databaseName) 
				dbcur = dbcon.cursor()
				dbcur.execute('''
								CREATE TABLE LC.SMARTS_TRADE_''' + environment + '_' + region + '_' + busDt +
							  '''(
									EXCHANGE_ID     VARCHAR(100),
									MESSAGE_TYPE    VARCHAR(100),
									DATE1           VARCHAR(100),
									TIME1           VARCHAR(100),
									TRADE_ID        VARCHAR(100),
									SECURITY        VARCHAR(100),
									PRICE           VARCHAR(100),
									QUANTITY        VARCHAR(100),
									TRADE_FLAGS     VARCHAR(100),
									VALUE1          VARCHAR(100),
									BID_ORDER_ID    VARCHAR(100),
									ASK_ORDER_ID    VARCHAR(100),
									TRADE_TYPE      VARCHAR(100),
									PARENT_TRADE_ID VARCHAR(100),
									OTHER           VARCHAR(100)
								) '''
							'''
							IN TS_APPDAT_FACT_16K
							INDEX IN TS_APPIX_FACT_16K
							DISTRIBUTE BY HASH (TRADE_ID)  COMPRESS YES
					''')
				dbcon.commit()
				print('        ' + environment + ' - TRADE table created Successfully')
			else:
				print('        ' + environment + " - File TRADE.TXT doesn't exists")
				
			## Checking OFFTR.TXT file is available or not, if it is available then it will create table
			if 'offtr_conv.TXT' in SMARTSAutomation.folders:
				dbcon = ms.db2.connect(SMARTSAutomation.databaseName) 
				dbcur = dbcon.cursor()
				dbcur.execute('''
								CREATE TABLE LC.SMARTS_OFFTR_''' + environment + '_' + region + '_' + busDt +
							  '''(		
									EXCHANGE_ID      VARCHAR(100),
									MESSAGE_TYPE     VARCHAR(100),
									DATE1            VARCHAR(100),
									TIME1            VARCHAR(100),
									TRADE_ID         VARCHAR(100),
									SECURITY         VARCHAR(100),
									PRICE            VARCHAR(100),
									QUANTITY         VARCHAR(100),
									TRADE_FLAGS      VARCHAR(100),
									VALUE1           VARCHAR(100),
									BID_ORDER_ID     VARCHAR(100),
									ASK_ORDER_ID     VARCHAR(100),
									BID_BROKER       VARCHAR(100),
									BID_TRADER       VARCHAR(100),
									ASK_BROKER       VARCHAR(100),
									ASK_TRADER       VARCHAR(100),
									EXECUTE_TIME     VARCHAR(100),
									BID_ACCOUNT      VARCHAR(100),
									BID_ACCOUNT_TYPE VARCHAR(100),
									ASK_ACCOUNT      VARCHAR(100),
									ASK_ACCOUNT_TYPE VARCHAR(100),
									TRADE_TYPE       VARCHAR(100),
									PARENT_TRADE_ID  VARCHAR(100),
									OTHER            VARCHAR(100)
								) '''
							'''
							IN TS_APPDAT_FACT_16K
							INDEX IN TS_APPIX_FACT_16K
							DISTRIBUTE BY HASH (TRADE_ID)  COMPRESS YES
					''')
				dbcon.commit()
				print('        ' + environment + ' - OFFTR table created Successfully')
			else:
				print('        ' + environment + " - File OFFTR.TXT doesn't exists")			
			

		## This function will load the data into respective tables
		def loadTables(self, environment, region, busDt, targetPath):
			
			print ('Data loading process started...')
			
			os.chdir(targetPath)
			SMARTSAutomation.folders = os.listdir(targetPath)
			
			os.system("db3 connect to nytd_lcdmart")
			
			## Checking ENTER.TXT file is available or not, if it is available then it will load the data
			if 'enter_conv.TXT' in SMARTSAutomation.folders:
				sqlStr1 = ' db2 "load client from \''
				sqlStr2 = targetPath +'/enter_conv.TXT\' of del messages\''
				sqlStr3 = targetPath + '/LoadMsg\'' 
				sqlStr4 = ' insert into LC.SMARTS_ENTER_' + environment + '_' + region + '_' + busDt + ' copy yes to /dev/null"'
				
				os.system (sqlStr1 + sqlStr2 + sqlStr3 + sqlStr4)
				print('        ' + environment + ' - ENTER table data loaded successfully')
			else:
				print('        ' + environment + " - Enter file doesn't exists")
			
			## Checking AMEND.TXT file is available or not, if it is available then it will load the data
			if 'amend_conv.TXT' in SMARTSAutomation.folders:
				sqlStr1 = ' db2 "load client from \''
				sqlStr2 = targetPath +'/amend_conv.TXT\' of del messages\''
				sqlStr3 = targetPath + '/LoadMsg\'' 
				sqlStr4 = ' insert into LC.SMARTS_AMEND_' + environment + '_' + region + '_' + busDt + ' copy yes to /dev/null"'
				
				os.system (sqlStr1 + sqlStr2 + sqlStr3 + sqlStr4)
				print('        ' + environment + ' - AMEND table data loaded successfully')
			else:
				print('        ' + environment + " - AMEND file doesn't exists")
			
			## Checking DELET.TXT file is available or not, if it is available then it will load the data
			if 'delet_conv.TXT' in SMARTSAutomation.folders:
				sqlStr1 = ' db2 "load client from \''
				sqlStr2 = targetPath +'/delet_conv.TXT\' of del messages\''
				sqlStr3 = targetPath + '/LoadMsg\'' 
				sqlStr4 = ' insert into LC.SMARTS_DELET_' + environment + '_' + region + '_' + busDt + ' copy yes to /dev/null"'
				
				os.system (sqlStr1 + sqlStr2 + sqlStr3 + sqlStr4)
				print('        ' + environment + ' - DELET table data loaded successfully')
			else:
				print('        ' + environment + " - DELET file doesn't exists")
			
			## Checking TRADE.TXT file is available or not, if it is available then it will load the data
			if 'trade_conv.TXT' in SMARTSAutomation.folders:
				sqlStr1 = ' db2 "load client from \''
				sqlStr2 = targetPath +'/trade_conv.TXT\' of del messages\''
				sqlStr3 = targetPath + '/LoadMsg\'' 
				sqlStr4 = ' insert into LC.SMARTS_TRADE_' + environment + '_' + region + '_' + busDt + ' copy yes to /dev/null"'
				
				os.system (sqlStr1 + sqlStr2 + sqlStr3 + sqlStr4)
				print('        ' + environment + ' - TRADE table data loaded successfully')
			else:
				print('        ' + environment + " - TRADE file doesn't exists")
			
			## Checking OFFTR.TXT file is available or not, if it is available then it will load the data
			if 'offtr_conv.TXT' in SMARTSAutomation.folders:
				sqlStr1 = ' db2 "load client from \''
				sqlStr2 = targetPath +'/offtr_conv.TXT\' of del messages\''
				sqlStr3 = targetPath + '/LoadMsg\'' 
				sqlStr4 = ' insert into LC.SMARTS_OFFTR_' + environment + '_' + region + '_' + busDt + ' copy yes to /dev/null"'
				
				os.system (sqlStr1 + sqlStr2 + sqlStr3 + sqlStr4)
				print('        ' + environment + ' - OFFTR table data loaded successfully')
			else:
				print('        ' + environment + " - OFFTR file doesn't exists")
			
			## Removing all LoadMsg files
			dir = os.getcwd()
			files = os.listdir(dir)
			for i in files:
				if (str(i).startswith('LoadMsg')):
					os.remove(i)
			print ('All LoadMsg files have been removed successfully')
			
			os.chdir(SMARTSAutomation.basePath)
			 
	except Exception as e:
		print(e)