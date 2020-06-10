'''
This program will demonstarate how we can trigger multiple task simulteniously as a process in python
We'll be fetching some windows command from database and will run them as a process
'''

import MultiProcessing.database_connection as db
from multiprocessing import Lock, Process
import os

class run_process(object):
    
    
    ''' This function will create dictionary with key as command_sequence and value an list of commands.It will look as follows...
        taskSequence_Dict
        {
            1:['shutil2 C:\\test\\test.txt', G:\\test\\', 'shutil2 C:\\test\\test1.txt', G:\\test\\']
            2:['shutil2 C:\\temp\\temp.txt', G:\\test\\']
            3:['shutil2 C:\\test\\test2.txt', G:\\test\\', 'shutil2 C:\\test\\test3.txt', G:\\test\\', 'shutil2 C:\\test\\test4.txt', G:\\test\\']
        }
    
    '''
    def get_command_sequence_dict(self):
        
        taskSequence_Dict = {}
        taskSequence_List=[]
        
        try:
               
            ## Getting distinct TASK_SEQUENCE from database
            with db.execute_dql('localhost','test','postgres','admin',1234) as executor:
                executor.execute("SELECT DISTINCT(TASK_SEQUENCE) FROM T_CTRLM_JOBS")
                
                if executor is not None:
                    for data in executor.fetchall():
                        taskSequence_List.append(data)
                
                    ## Iterating over the distinct sequence list and getting all the task_commands for that particular task_sequence        
                    for i, val in enumerate(taskSequence_List):
                        with db.execute_dql('localhost','test','postgres','admin',1234) as executor:
                            executor.execute("SELECT JOB_COMMAND FROM T_CTRLM_JOBS WHERE TASK_SEQUENCE=" + val)
                            taskSequence_Set=()
                            
                            if executor is not None:
                                for data in executor.fetchall():
                                    taskSequence_Set.update(data)
                                
                                ## assigning the values to the dictionary
                                taskSequence_Dict[va]=taskSequence_Set
    
            ## returning the dictionary
            return taskSequence_Dict
                                
        except Exception as e:
            print(e)
    
    ## This function will actually run the command. Depending upon return code it will update the status in database
    def run_command(self, lock, command):
        
        result = os.system(command)
        
        print('[INFO] command execution completed. The return code is ' + str(result))
        
        if result == 0:
            with db.execute_dml('localhost','test','postgres','admin',1234) as executor:
                executor.execute("UPDATE T_CTRLM_JOBS SET STATUS='COMPLETED' WHERE COMMAND=" + command)
        elif result != 0:
            with db.execute_dml('localhost','test','postgres','admin',1234) as executor:
                executor.execute("UPDATE T_CTRLM_JOBS SET STATUS='FAILED' WHERE COMMAND=" + command)
    
    
    ## This function will prepare the command and will call the run_command function.
    def prepare_command(self):
        lock = Lock()
        processList = list()
        command_dict = {}
        taskDictKeys={}
        
        try:
            
            ## Getting distinct TASK_SEQUENCE from database
            with db.execute_dml('localhost','test','postgres','admin',1234) as executor:
                executor.execute("UPDATE T_CTRLM_JOBS SET STATUS='In-Progress'")
            
            command_dict = self.get_command_sequence_dict()
            
            ## Getting the key of dictionary
            for k in command_dict.keys():
                taskDictKeys.appen(int(k))
                
            ## sorting the dictionary
            taskDictKeys.sort()
            
            for sequence in taskDictKeys:
                for i, val in enumerate(command_dict[str(sequence)]):
                    
                    ## calling the run_command function
                    processList.append(Process(name=val,target=self.run_command, args=lock, val))
                         
                ## creating process and waiting for process to complete   
                _=[p.start() for p in processList]
                _=[p.join() for p in processList]
            
        except Exception as e:
            print(e)
        
## main method
def main():
    run = run_process()
    run.prepare_command()
        
    
if __name__ == "__main__":
    main()
    
