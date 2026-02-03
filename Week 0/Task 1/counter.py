class counter:
    def __init__(self):
        self.__count = 0    # it starts from 0

    def addCount(self):
        self.__count += 1    # add 1 to count

    def getCount(self):
        return self.__count     # return current count

    def zeroCount(self):      # remove all counts and  set to zero
        self.__count = 0
