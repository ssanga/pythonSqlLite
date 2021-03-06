#https://www.datacamp.com/community/tutorials/sqlite-in-python?utm_source=adwords_ppc&utm_campaignid=898687156&utm_adgroupid=48947256715&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=229765585186&utm_targetid=aud-299261629574:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=9061040&gclid=Cj0KCQjwy8f6BRC7ARIsAPIXOjh5N3lHWqM3vGAJ5lpTaCQ2CQnJgjsHCuLdXVE-jLyYJIAMOhbtT5saAkFFEALw_wcB

import sqlite3
import pythonSqlLite_SQLAlchemy

def trying_countries():

    conn = sqlite3.connect('pythonSqlLite.db')
    cur = conn.cursor()
    
    cur.execute('SELECT * from countries')
    print(cur.fetchone())
    
    
    for row in cur.execute('SELECT * FROM countries'):
        print(row)
        
        
    code = ('AFG',)
    cur.execute('SELECT * FROM countries WHERE "alpha-3" = ?', code)
    print(cur.fetchone())
    conn.close()

    
def trying_consumers():

    conn = sqlite3.connect('pythonSqlLite.db')
    cur = conn.cursor()
    
    cur.execute("INSERT INTO consumers VALUES (2,'John Doe','john.doe@xyz.com','A')")
    for row in cur.execute('SELECT * FROM consumers'):
        print(row)
        
    # Prepare a list of records to be inserted
    purchases = [(3,'John Paul','john.paul@xyz.com','B'),
             (4,'Chris Paul','john.paul@xyz.com','A'),]

    # Use executemany() to insert multiple records at a time
    cur.executemany('INSERT INTO consumers VALUES (?,?,?,?)', purchases)
    for row in cur.execute('SELECT * FROM consumers'):
        print(row)

    conn.commit()
    conn.close()
    
if __name__ == "__main__":
    # trying_countries()
    # trying_consumers()
    
    dbms = pythonSqlLite_SQLAlchemy.MyDatabase(dbname='pythonSqlLite.db')
    
    # dbms.insert_single_data()
    dbms.print_all_data(pythonSqlLite_SQLAlchemy.COUNTRIES)
    dbms.print_all_data(pythonSqlLite_SQLAlchemy.CONSUMERS)
    # dbms.sample_query() # simple query
    # dbms.sample_delete() # delete data
    # dbms.sample_insert() # insert data
    # dbms.sample_update() # update data