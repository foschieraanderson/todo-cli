import sqlite3
from contextlib import contextmanager
 
@contextmanager
def connection():
    try:
        
        # Connect to DB and generate a cursor
        conn = sqlite3.connect('database.db')
        conn.row_factory = sqlite3.Row # fetchall returns dicts
        yield conn.cursor()
      
    # Handle errors
    except sqlite3.Error as error:
        conn.rollback()
        raise Exception(f'Error occured - {error}')
      
    # Close DB Connection irrespective of success
    # or failure
    finally:
        conn.commit()
        conn.close()
        
