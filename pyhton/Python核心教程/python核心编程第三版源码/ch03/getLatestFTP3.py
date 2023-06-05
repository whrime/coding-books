#!/usr/bin/env python

import ftplib
import os
import socket
import time

tt = time.strftime("%Y%m%d",time.localtime())
HOST = 'ftp.csindex.com.cn'
DIRN = 'idxdata/data/bonddata/general'
FILE = '%sbond_valuation.zip'%tt

def main():
    try:
        f = ftplib.FTP(HOST)
    except (socket.error, socket.gaierror) as e:
        print('ERROR: cannot reach "%s"' % HOST)
        return
    print('*** Connected to host "%s"' % HOST)

    try:
        f.login("csifzzq","74532442")
    except ftplib.error_perm:
        print('ERROR: cannot login anonymously')
        f.quit()
        return
    print('*** Logged successful!"')

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print('ERROR: cannot CD to "%s" folder' % DIRN)
        f.quit()
        return
    print('*** Changed to "%s" folder' % DIRN)

    try:
        f.retrbinary('RETR %s' % FILE,
            open(FILE, 'wb').write)
    except ftplib.error_perm:
        print('ERROR: cannot read file "%s"' % FILE)
        if os.path.exists(FILE):
            os.unlink(FILE)
    else:
        print('*** Downloaded "%s" to CWD' % FILE)
    f.quit()

if __name__ == '__main__':
    main()
