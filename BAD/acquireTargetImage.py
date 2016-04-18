import ftplib
def getDataFile(outfile=None, ftp):
        try:
        count = 0
        data = []
        #write file to CWD (BAD/BAD)
        ftp.retrbinary("RETR " + filename, open("autogendata.txt", 'wb').write)
        ftp.quit()
        
def getParameters():
    filename = "autogendata.txt"
    f = open(filename, 'r')
    imgname = f.readline()
    cameratype = f.readline()
    temp = {"file":"", "camera":"")
    return temp
    
def getBinary(filename, outfile=None):
    
    try:
        count = 0
        data = []
        
        #initialize and connect to network driver file server.
        ftp = ftplib.FTP('ndrives.calu.edu')
        ftp.login(user = 'hah5158', passwd = 'Pbhmount18')
        getDataFile(ftp)
        data = getParamters()
        cameratype = data["camera"]
        #ftp.dir() will retrieve and print all available files/dirs
        #data will contain this info instead to minimize output
        ftp.dir(data.append)
        
        #Output only the valid files (.png)
        for item in data:
            if ".png" in item:
                print "- " + item
                count = count + 1
                
        #Notify user if there arent any valid files in directory
        if count <= 0:
            print "No appropriate images are on server"
            
        print "-----------------------------------"
        
        #write file to CWD (BAD/BAD)
        ftp.retrbinary("RETR " + filename, open("target.png", 'wb').write)
        ftp.quit()
        
    except ftplib.all_errors as e:
        print "An error occured with the FTP connection\nError " + str(e)



# command line argument is filename on server
print "CL Input " + str(len(sys.argv)) + " " + sys.argv[1]
print "-----------------------------------"
getBinary(sys.argv[1])
