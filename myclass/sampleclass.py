class sampleclass:
    def __init__(self,name):
        self.name=name
        pass

    def printme(self,str):
        print(str)

    def __len__(self):
        return 1

    def __str__(self):
        return( f"my name is {self.name}")
    