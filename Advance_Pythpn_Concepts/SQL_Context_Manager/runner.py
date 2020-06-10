import SQL_Context_Manager.db_utils as db


class runner(object):

    def select_data(self):
        try:
            with db.execute_dql('localhost','test','postgres','admin',1234) as executor:
                executor.execute("SELECT * FROM t_ctrlm_job_exec")

                if executor is not None:
                    for data in executor.fetchall():
                        print(data)

            with db.execute_dql('localhost','test','postgres','admin',1234) as executor:
                executor.execute("SELECT count(*) FROM t_ctrlm_job_exec")

                if executor is not None:
                    for data in executor.fetchall():
                        print("The count is " + str(data))
        except Exception as e:
            print(e)
            
    def modify_data(self):
        try:
            with db.execute_dml('localhost','test','postgres','admin',1234) as executor:
                executor.execute("TRUNCATE TABLE TEST")
                print('Truncated')
                executor.execute("INSERT INTO test VALUES(NOW())")
            print('Data inserted successfully..')
        except Exception as e:
            print(e)

def main():
    run = runner()
    run.select_data()
    run.modify_data()

if __name__ == "__main__":
    main()