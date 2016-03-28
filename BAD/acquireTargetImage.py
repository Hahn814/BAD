import ftplib

def getBinary(filename, outfile=None):
    
    try:
        count = 0
        data = []
        ftp = ftplib.FTP('ndrives.calu.edu')
        ftp.login(user = 'hah5158', passwd = 'Pbhmount18')
        ftp.dir(data.append)
        
        for item in data:
            if ".png" in item:
                print "- " + item
                count = count + 1
                
        if count <= 0:
            print "No appropriate images are on server"
            
        print "-----------------------------------"
                
        ftp.retrbinary("RETR " + filename, open("target.png", 'wb').write)
        ftp.quit()
    except ftplib.all_errors as e:
        print "An error occured with the FTP connection\nError " + str(e)



# command line argument is filename on server
print "CL Input " + str(len(sys.argv)) + " " + sys.argv[1]
print "-----------------------------------"
getBinary(sys.argv[1])
