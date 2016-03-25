import ftplib as FTP
import sys


def getBinary(filename, outfile=None):
    # get the binary file
    if outfile is None:
        outfile = sys.stdout

    ftp.retrbinary("RETR " + "target.png", outfile.write)

try:
    ftp = FTP("ftp://ndrives.calu.edu/")
    ftp.login(user = "hah5158", passwd = "Pbhmount18")
except FTP.all_errors as e:
    print "An error occured with the FTP connection\nError " + e

# command line argument is filename on server
getBinary(sys.argv[2])
