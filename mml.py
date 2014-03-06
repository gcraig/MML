#!/usr/bin/python
# -*- encoding: UTF-8 -*-

import sys

print("Python 3")

class ClassProperty:
    name = ""
    modifier = ""

class ClassParent:
    classParent = ""

class ClassName:
    className = ""
        
class ClassTable:

    table = dict()

    def populateTable(self):
        try:
            self.add_class("Event", "BaseObject", ["name", "description", "EventDetails"])
            self.add_class("EventDetails", "BaseObject", ["location", "start_time", "end_time"])
        except:
            raise

    def add_class(self, classname, parentname, classproperties):
        self.classname = classname
        self.parentname = parentname
        self.classproperties = classproperties
        self.table[classname] = (parentname, classproperties)

    def get_parent(self, classname):
        values = self.table[classname]
        return values[0] # change to dictionary from tuple

    def get_properties(self, classname):        
        values = self.table[classname]
        return values[1]

    def printTable(self):
        for classname in self.table.keys():
            print("Class: " + classname)
            print("Parent: " + str(self.get_parent(classname)))
            print("Properties: ")
            for prop in self.get_properties(classname):
                print(str(prop))

if __name__ == '__main__':
    ct = ClassTable()
    ct.populateTable()
    ct.printTable()

