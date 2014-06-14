import time
#import main
import MySQLdb
import random
import shutil
import os
db=MySQLdb.connect("localhost",'root','mani',"mycloud")
cursor=db.cursor()
#sql_data="select * from usrdata"
#cursor.execute(sql_data)
#usr_file=cursor.fetchall()
i,var=0,1
#sfile="sample.txt"
#src="/home/m@ni/myproject/tmp/"+sfile
while var==1:
        i+=1
        #x=random.randint(2376845907651287634,45684565128456789067)
        #a=str(hex(x))
        #n=len(a)
        sql_data="select * from usrdata"
	cursor.execute(sql_data)
	usr_file=cursor.fetchall()

	for row in usr_file:
                filename=row[1]
                fsplit1=row[3]
                fsplit2=row[4]

                dir1_x=random.randint(4345566767809122341,67673445657333453445354)
                dir1_a=str(hex(dir1_x))
                dir1_n=len(dir1_a)
                dir1_new = "encr1"+filename
                storage1="/var/www/cgi-bin/files/cloudA/"
               	src1=storage1+fsplit1
		#if not os.path.exists(storage1):
                #       os.mkdir(os.path.dirname(storage1))
                dir1_update=dir1_a[2:dir1_n]+"/"+dir1_new
		dest_dir1=storage1+dir1_a[2:dir1_n]+"/"+dir1_new
                print dest_dir1
		#dest="/home/m@ni/datastorage/"+a[2:n]+"/"+sfile        
                if not os.path.exists(dest_dir1):
                      os.mkdir(os.path.dirname(dest_dir1))
                shutil.move(src1,dest_dir1)

                dir2_x=random.randint(4345566767809122341,67673445657333453445354)
                dir2_a=str(hex(dir2_x))
                dir2_n=len(dir2_a)
                dir2_new = "encr2"+filename
                storage2="/var/www/cgi-bin/files/cloudB/"
                src2=storage2+fsplit2

                #if not os.path.exists(storage2):
                 #       os.mkdir(os.path.dirname(storage2))

                src2=storage2+fsplit2
		dir2_update=dir2_a[2:dir2_n]+"/"+dir2_new
                dest_dir2=storage2+dir2_update
		print dest_dir2
                #dest="/home/m@ni/datastorage/"+a[2:n]+"/"+sfile        
                if not os.path.exists(dest_dir2):
                       os.mkdir(os.path.dirname(dest_dir2))
                shutil.move(src2,dest_dir2)
       	        sql_update="update usrdata set fsplit_1= '%s' , fsplit_2='%s' where filename='%s'" %(dir1_update,dir2_update,filename)
                cursor.execute(sql_update)
        	db.commit()
	time.sleep(10)

