#!/usr/bin/python
import cgi, os
import fsplit
import MySQLdb
import cgitb; cgitb.enable()
#import main
form = cgi.FieldStorage()
# Get filename here.
user=form.getvalue("upload_value")
db=MySQLdb.connect("localhost",'root','mani',"mycloud")
cursor=db.cursor()
sql_login="select * from login where user_id='%s'"%(user)
cursor.execute(sql_login)
login_pswd=cursor.fetchone()
fileitem = form['filename']
# Test if the file was uploaded
if fileitem.filename:
	# strip leading path from file name to avoid
	# directory traversal attacks
	fn = os.path.basename(fileitem.filename.replace("\\", "/" ))
	fc=fileitem.value
	#fw=open(loc, 'wb')#.write(fileitem.file.read())
	#fw.close()
	#test1.f_write(fn,fc)
	fw=open('/var/www/cgi-bin/files/' + fn, 'wb')
        fw.write(fc)
        fw.close()
	
	message = 'Uploaded'
else:
	message = 'Not uploaded'
fsplit.f_split(user,fn);
print '''\
Content-Type: text/html\n
<html><title>myCloud</title><head>
<link rel="stylesheet" type="text/css" href="style2.css"></head>
<body>
<br><br>
<center>
<h2><a href="main.py?username=%s&password=%s">Main page</a></h2>'''%(user,login_pswd[1])
print"""<br><h2>Filename: %s</h2>
<h2>Status: %s</h2></center>
</body>
</html>
""" % (fileitem.filename,message)


