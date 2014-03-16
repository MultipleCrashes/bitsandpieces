import time

class Time:
    def currentTime():
        print " Current Time is "
        print time.now()



if __name__=='__main__':
    TimeObj=Time()
    print " Calling time function "
    TimeObj.currentTime()
