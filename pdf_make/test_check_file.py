'''
Created on 2017/09/30

@author: nozaki
'''
import unittest
import file_setup

class TestCheckFile(unittest.TestCase):


    def testGetFileSuccess(self):
        path = 'G:\\text\summary.txt'
        result = file_setup.fileSetup.getFile(path)
        self.assertEqual(result, 0)

    def testGetFileFailure(self):
        path = 'hogehoge'
        result = file_setup.fileSetup.getFile(path)
        self.assertEqual(result, 1)

    def testGetFileNullPath(self):
        path = ''
        result = file_setup.fileSetup.getFile(path)
        self.assertEqual(result, 999)

if __name__ == "__main__":

    unittest.main()