#https://www.datacamp.com/community/tutorials/sqlite-in-python?utm_source=adwords_ppc&utm_campaignid=898687156&utm_adgroupid=48947256715&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=229765585186&utm_targetid=aud-299261629574:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=9061040&gclid=Cj0KCQjwy8f6BRC7ARIsAPIXOjh5N3lHWqM3vGAJ5lpTaCQ2CQnJgjsHCuLdXVE-jLyYJIAMOhbtT5saAkFFEALw_wcB

import sqlite3

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

    
def trying_consumers():

    conn = sqlite3.connect('pythonSqlLite.db')
    cur = conn.cursor()
    
    cur.execute("INSERT INTO consumers VALUES (1,'John Doe','john.doe@xyz.com','A')")
    for row in cur.execute('SELECT * FROM consumers'):
        print(row)

if __name__ == "__main__":
    trying_countries()