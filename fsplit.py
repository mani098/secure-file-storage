#!/usr/bin/python
import MySQLdb
import math
import os
#from main import user_id
import random
#import save_file
from Crypto.Cipher import AES
db=MySQLdb.connect("localhost","root","mani","mycloud")
cursor=db.cursor()
#src="/files/"+save_file.file_name()
#sfile=open("src",'r');
key_x=random.randint(23445523457809122341,3343445657333453445354)
key_a=str(hex(key_x))
key_n=len(key_a)
key = key_a[2:18]
mode = AES.MODE_ECB
#sdata = sfile.read()
def f_split(fuser,fname):
	src="/var/www/cgi-bin/files/"+fname
	sfile=open(src,'a+');
	sdata = sfile.read()
        ln=float(len(sdata))/16
        if (ln != 0):
                x=(math.ceil(ln) - ln)*16
                ix=int(x)
                for i in range(ix):
                     sfile.write(" ")
        sfile.close()
	fileobj=open(src,'r')
	sdata1=fileobj.read()
	enc=AES.new(key,mode)
        cipher=enc.encrypt(sdata1)
        fcontent_1,sentinel,fcontent_2=cipher.partition(cipher.split()[len(cipher.split())/2])
        dir1_x=random.randint(4345566767809122341,67673445657333453445354)
	dir1_a=str(hex(dir1_x))
	dir1_n=len(dir1_a)#insert into login values
	#dir1_new = "/files/cloudA"+dir1_a[2:dir1_n]+'/'+"encr1"+fname
	dir1_path="/var/www/cgi-bin/files/cloudA/"+dir1_a[2:dir1_n]+"/"
	
	if not os.path.exists(dir1_path):
		os.mkdir(os.path.dirname(dir1_path))
	#dir1_path="/files/cloudA/"+dir1_new
	dir1_new=dir1_path+"/encr1"+fname
	tfile_1=open(dir1_new,'w')
        tfile_1.write(fcontent_1+sentinel)
        tfile_1.close()
	dir1_update=dir1_a[2:dir1_n]+"/encr1"+fname
	
	dir2_x=random.randint(4345566767809122341,67673445657333453445354)
        dir2_a=str(hex(dir2_x))
        dir2_n=len(dir2_a)
        #dir2_new = dir2_a[2:dir2_n]+'/'+"encr2"+fname
	dir2_path="/var/www/cgi-bin/files/cloudB/"+dir2_a[2:dir2_n]+"/"
	if not os.path.exists(dir2_path):
                os.mkdir(os.path.dirname(dir2_path))
        #dir2_path="/files/cloudB/"+dir2_new
        dir2_new=dir2_path+"/encr2"+fname
	tfile_2=open(dir2_new,'w')
        tfile_2.write(fcontent_2)
        tfile_2.close()
	dir2_update=dir2_a[2:dir2_n]+"/encr2"+fname
	fileobj_x=random.randint(455609122341,657333453445354)
        fileobj_a=str(hex(fileobj_x))
        fileobj_n=len(fileobj_a)
        fileobj_new = fileobj_a[2:fileobj_n]
	sql_updatefile="insert into usrdata values('%s','%s','%s','%s','%s','%s')" %(fuser,fname,fileobj_new,dir1_update,dir2_update,key)
	cursor.execute(sql_updatefile)
	db.commit()
	

