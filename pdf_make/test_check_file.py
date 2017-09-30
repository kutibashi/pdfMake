'''
Created on 2017/09/30

@author: nozaki
'''
import unittest
import file_setup

class TestCheckFile(unittest.TestCase):


    def testGetFileSuccess(self):
        path = 'G:\text\summary.txt'
        result = file_setup.fileSetup.getFile(path)
        self.assertTrue(result)

    def testGetFileFailure(self):
        path = ''
        result = file_setup.fileSetup.getFile(path)
        self.assertFalse(result)


if __name__ == "__main__":

    unittest.main()