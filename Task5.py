import os
from typing import Optional, Union

class IteratorTask5:
    '''iterator class for task 5'''
    def __init__(self, dataset: str, classname: str, path: str) -> Union[str, None]:
        '''class constructor'''
        self.pathdir = ""
        self.classname = ""
        self.names = []
        self.limit = 0
        self.counter = 0
        self.dataset = ""
        self.init(dataset, classname, path)

    def __next__(self) -> Union[str, None]:
        '''!!!looped!!!move on to the next element on the task after the iteration'''
        if self.counter < self.limit:
            self.counter += 1
            return self.names[self.counter - 1]
        elif self.counter == self.limit:
            self.counter = 0
            self.counter += 1
            return self.names[self.counter - 1]

    def __iter__(self) -> Union[str, None]:
        '''iterator defining'''
        return self

    def init(self, dataset: str, classname: str, pathdir: str) -> Union[str, None]:
        '''we check the objects (items) with which we will have to work in the future'''
        if not "dataset" in pathdir:
            raise ("error")
        self.pathdir = pathdir
        self.classname = classname
        self.names = os.listdir(os.path.join(dataset, self.pathdir, self.classname))

        for i in self.names:
            if not ".jpg" in i:
                self.names.remove(i)
        self.limit = len(self.names)
        self.counter = 0

    def clear(self) -> Union[str, None]:
        '''cleansing'''
        self.counter = 0

    def setclassName(self, classname: str) -> Union[str, None]:
        '''setting the class name'''
        self.init(self.dataset, classname, self.pathdir)

    def getclassName(self) -> Union[str, None]:
        '''getting the class name'''
        print(self.classname)

    def setPath(self, pathdir: str) -> Union[str, None]:
        '''setting the path'''
        self.init(self.dataset, self.classname, pathdir)
