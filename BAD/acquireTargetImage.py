import ftplib
import sys
    
def getBinary(filename="target.png", addr="ndrives.calu.edu", username="hah5158", psk="Pbhmount18", outfile=None):
    
    try:
        count = 0
        data = []
        
        #initialize and connect to network driver file server.
        ftp = ftplib.FTP(addr)
        ftp.login(user = username, passwd = psk)

        #write file to CWD (BAD/BAD)
        genfile = "autogendata.txt"
        ftp.retrbinary("RETR " + genfile, open(genfile, 'wb').write)
        
        f = open(genfile, 'r')
        imgname = f.readline().rstrip()
        cameratype = f.readline()

        print "'"+imgname+"'"
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
        ftp.retrbinary("RETR " + imgname, open('target.png', 'wb').write)
        ftp.quit()
        
    except ftplib.all_errors as e:
        print "An error occured with the FTP connection\nError " + str(e)
    return
    


# command line argument is filename on server
print "CL Input " + str(len(sys.argv)) + " " + sys.argv[1]
print "-----------------------------------"
getBinary(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
