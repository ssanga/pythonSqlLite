# https://medium.com/@mahmudahsan/how-to-use-python-sqlite3-using-sqlalchemy-158f9c54eb32

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

# Table Names
CONSUMERS       = 'consumers'
COUNTRIES       = 'countries'

class MyDatabase:
    
    # Main DB Connection Ref Obj
    db_engine = None
    
    def __init__(self, dbname=''):
        engine_url = 'sqlite:///' + dbname
        self.db_engine = create_engine(engine_url)
        print(self.db_engine)
        
            
    def execute_query(self, query=''):
        if query == '' : return False
        print (query)
        with self.db_engine.connect() as connection:
            try:
                connection.execute(query)
                return True
            except Exception as e:
                print(e)
                return False
                
    def print_all_data(self, table='', query=''):
        query = query if query != '' else "SELECT * FROM '{}';".format(table)
        print(query)
        with self.db_engine.connect() as connection:
            try:
                result = connection.execute(query)
            except Exception as e:
                print(e)
            else:
                for row in result:
                    print(row) # print(row[0], row[1], row[2])
                result.close()
        print("\n")