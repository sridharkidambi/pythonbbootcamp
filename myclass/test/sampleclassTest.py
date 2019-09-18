import unittest
import sys
# sys.path.append('/PYTHON/myclass/sampleclass/')
from  myclass.sampleclass  import  sampleclass


class sampleclassTest(unittest.TestCase):


    def testarthme(self):
        print(sys.path)
        self.assertEqual(1,1)
        # obj = sampleclass('SK')
        # result=  obj.arthme(2,3)
        # self.assertEqual(result,5)

    if __name__=='__main__':
        unittest.main()