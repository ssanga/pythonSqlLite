import unittest
import pythonSqlLite_SQLAlchemy

# https://docs.python.org/3/library/unittest.html

class Test_pythonSqlLite_SQLAlchemy(unittest.TestCase):

    def setUp(self):
        self.dbms = pythonSqlLite_SQLAlchemy.MyDatabase(dbname='pythonSqlLite.db')
    
    def test_execute_insert_into_with_no_query_returns_False(self):
        result = self.dbms.execute_query('')
        self.assertFalse(result)
        
    def test_execute_insert_into_returns_True(self):
        sql = "INSERT INTO consumers VALUES (NULL, 'Integration Test','integration.test@xyz.com','A')"
        result = self.dbms.execute_query(sql)
        self.assertTrue(result)
    
    def test_print_constumers_table_data_True(self):
        self.dbms.print_all_data(pythonSqlLite_SQLAlchemy.CONSUMERS)
      
    @unittest.skip("demonstrating skipping")
    def test_skip_example(self):
        self.assertTrue(True)
        
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")

if __name__ == '__main__':
    unittest.main()
    
    
