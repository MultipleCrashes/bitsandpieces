
import os
import time
import urllib2

def downloadFiles(url="https://class.coursera.org/algs4partI-004/lecture/download.mp4?lecture_id=",location="D:\\coursera"):
    os.chdir(location)
    print "changed dir.. Downloading files to D:\\coursera "
    os.listdir(".")
   
    

    for i in range(3,63):
        print "downloading " +str(i)
        startTime=time.time()
        downloadCmd=url+str(i)
        print downloadCmd
        #os.system(downloadCmd)
        mp4file=urllib2.urlopen(downloadCmd)
        output=open(str(i)+'.mp4','wb')
        output.write(mp4file.read())
        output.close()
        endTime=time.time()
        timeElapsed=endTime-startTime
        print "Total time for downloading this file is = "+str(timeElapsed)


downloadFiles(url="https://class.coursera.org/algs4partI-004/lecture/download.mp4?lecture_id=",location="D:\\coursera")


    
    
    
