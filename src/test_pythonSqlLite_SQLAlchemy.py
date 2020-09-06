import unittest
import pythonSqlLite_SQLAlchemy

class Test_pythonSqlLite_SQLAlchemy(unittest.TestCase):

    def test_execute_query_with_no_query_returns_False(self):
        
        dbms = pythonSqlLite_SQLAlchemy.MyDatabase(pythonSqlLite_SQLAlchemy.SQLITE, dbname='pythonSqlLite.db')
        result = dbms.execute_query('')
        self.assertFalse(result)
        
    def test_execute_query_returns_True(self):
        sql = "INSERT INTO consumers VALUES (NULL, 'Integration Test','integration.test@xyz.com','A')"
        dbms = pythonSqlLite_SQLAlchemy.MyDatabase(pythonSqlLite_SQLAlchemy.SQLITE, dbname='pythonSqlLite.db')
        result = dbms.execute_query(sql)
        self.assertTrue(result)
        
    def test_another_test(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
    
    
