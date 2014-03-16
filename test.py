from time import gmtime,strftime

class Time:
    def currentTime(self):
        print " Current Time is "
        print strftime("%Y-%m-%d %H:%M:%S",gmtime())



if __name__=='__main__':
    TimeObj=Time()
    print " Calling time function "
    TimeObj.currentTime()
