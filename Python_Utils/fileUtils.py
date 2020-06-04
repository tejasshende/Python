
'''
This file contains all the utilities that are required to deal with file(s)
'''

import os.path
import configparser

## This function will write the given content to file
def write_to_file(fileName, fileContents):
    
    try:
        # checking file exists or not, if file exists, it will append else it will create first and then appen
        if os.path.exists(fileName):        
            file=open(fileName,'a')
            file.write(fileContents)
        
        else:
            file=open(fileName,'a')
            file.write(fileContents)
        file.close()
    except Exception as e:
        file.close()
        print(e)
    
## This function will read the .properties file and will return the dictionary
def get_property_val_dict(fileName):
    
    propValDict={}
    
    try:
        # reading the config file
        config = configparser.RawConfigParser()
        config.read(fileName)
        
        #stroing the values in dictionary
        propValDict['DBName'] = config.get('DatabaseSection', 'DatabaseName')
        propValDict['DBUser'] = config.get('DatabaseSection', 'DatabaseUser') 
        propValDict['DBPassword'] = config.get('DatabaseSection', 'DatabasePassword') 
        
        # returning the dictionary
        return propValDict 
        
    except Exception as e:
        print(e)
    
## This function will return True if file exists else retuen false
def check_file_exists(fileName):

        return os.path.exists(fileName)
    
## This function set the value in config file
def update_config_file(fileName, sectionName, key, value):
    try:
        # reading the config file
        config = configparser.RawConfigParser()
        config.read(fileName)
        
        # setting the new value in config file
        config.set(sectionName, key, value)
        
    except Exception as e:
        print(e)