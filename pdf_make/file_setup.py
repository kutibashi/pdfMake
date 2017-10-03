'''
Created on 2017/09/30

@author: nozaki
'''

import os

class fileSetup():

    def getFile(self):
        if self == '':
            return 999
        else:
            if os.path.exists(self):
                return 0
            else:
                return 1

if __name__ == '__main__':
    fileSetup()