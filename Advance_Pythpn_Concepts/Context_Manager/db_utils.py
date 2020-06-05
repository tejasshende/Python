
from contextlib import contextmanager
import psycopg2

''' This function is responsible to execute all DQL statements, e.g. SELECT '''
@contextmanager    
def execute_dql(host, database, user, password, port):
    try:
        print("Initilized database connection...")
        db_connection = psycopg2.connect(host=host,database=database, user=user, password=password, port=port)
        db_cursor=db_connection.cursor()
        yield db_cursor
    except Exception as e:
        db_connection.rollback()
        print(e)
    finally:
        print('cloing database connection and cursor object')
        db_connection.close()
        db_cursor.close()

''' This function is responsible to execute all DML statements, e.g. INSERT, UPDATE, DELETE, MERGE, LOCK TABLE '''
@contextmanager
def execute_dml(host, database, user, password, port):
    try:
        print("Initilized database connection...")
        db_connection = psycopg2.connect(host=host,database=database, user=user, password=password, port=port)
        db_cursor=db_connection.cursor()
        db_connection.autocommit=True
        yield db_cursor
        #db_connection.commit()
    except Exception as e:
        db_connection.rollback()
        print(e)
    finally:
        print('cloing database connection and cursor object')
        db_connection.close()
        db_cursor.close()