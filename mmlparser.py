#!/usr/bin/python
# -*- encoding: UTF-8 -*-

import sys

print("Python 3")
        
class MMLParser:
    """docstring for MMLParser"""
    
    verbose = False
    
    def __init__(self, fname):
        super(MMLParser, self).__init__()
        self.fname = fname
        print("MMLParser intialized")
        
    def printError(self):
        print("*"*72)
        print("\tError")
        print("*"*72)

    def buildRulesTable(self):
        ''' 
            The rules table is a lookup table, for each line, 
            which regex applies and calls a particular function
            to apply to that given rule.
        '''

    def readmML(self):
        try:
            # read the model into memory, even 10k line model
            # ia a huge hiearchy and should be ok without paging
            print("Parsing " + self.fname)
            with open(self.fname) as f:
                content = f.readlines()
            f.close()
    
            print("Processing each line")        
            for line in content:
                if MMLParser.verbose:
                    print(line)
                buildRulesTable();
        except:
            self.printError()
            #print("Error processing: %s" % self.fname, file=sys.stderr)
            raise



if __name__ == '__main__':
    mmlParser = MMLParser("input.mml")
    mmlParser.readmML()      