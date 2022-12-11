import os


class IteratorTask5:
    def __init__(self, dataset: str, classname: str, path: str):
        self.pathdir = ""
        self.classname = ""
        self.names = []
        self.limit = 0
        self.counter = 0
        self.dataset = ""
        self.init(dataset, classname, path)

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.names[self.counter - 1]
        else:
            raise StopIteration

    def init(self, dataset: str, classname: str, pathdir: str):
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

    def clear(self):
        self.counter = 0

    def setclassName(self, classname: str):
        self.init(self.dataset, classname, self.pathdir)
    def getclassName(self):
       print(self.classname)


    def setPath(self, pathdir: str):
        self.init(self.dataset, self.classname, pathdir)