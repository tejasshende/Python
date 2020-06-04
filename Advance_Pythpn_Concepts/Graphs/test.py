
class execute_jobs(object):
    
    def execute(self, command, jobName):
        
        #Update currently executing job in database
        cur=con.execute("Update execution_table set status='In-Process' where job=" + jobName)
        
        result=os.system(command)
        
        if(result==0):
            cur=con.execute("Update execution_table set status='SUCCESS' where job=" + jobName)
        else:
            cur=con.execute("Update execution_table set status='FAILURE' where job=" + jobName)
                
    def prepare_command(self):
        
        #getting command from database
        cur=con.execute("SELECT job from execution_table")
        pool = Pool(4)
        
        for rows in cur.fetchall():
            
            if("%%DATE" in rows):
                
                #replacing sh getData.sh %%DATE to sh getData.sh 20200531
                newRow=rows.replace("%%DATE", "20200531")
                
                result = pool.apply_sync(self.execute(newRow,rows))
                
                
        pool.close()
        pool.join()
                