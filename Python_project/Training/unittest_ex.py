import unittest

class StringMethods(unittest.TestCase):
    def test_upper(self):
        #obj - Person()
        #self.asserTrue(obj.IsEmployed()))
        self.asserEqual('foo'.upper(),'FOO')
        
    def test_isupper(self):
        self.assertTrue('FOO'.islower())
        self.asserFalse('Foo'.isuppper())
        
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(['hello','world']))   
        
    def test(self):
        print("Hello")
    
    def run(self,*args, **kwargs):
        print("Inside run")
     
if __name__ ==  "__main__":
    unittest.main()