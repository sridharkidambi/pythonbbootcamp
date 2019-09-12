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

    def arthme(self,num1,num2):
        try:
            k= num1+num2
        except:
            return "not adding,i am an exception"
        else:
            return k
    