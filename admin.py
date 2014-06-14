#!/usr/bin/python
import cgi, cgitb; cgitb.enable()
import MySQLdb

print "Content-type:text/html\r\n\r\n"

form = cgi.FieldStorage()
username = form.getvalue('username')
password  = form.getvalue('password')

print '<html>'
print '<head>'
print '<title>Admin-myCloud</title>'
print '<link rel="stylesheet" type="text/css" href="style2.css"></head>'
db=MySQLdb.connect("localhost",'root','mani',"mycloud")
cursor=db.cursor()
sql_login="select * from login"
cursor.execute(sql_login)
login_data=cursor.fetchall()
for row in login_data:
        if username=='admin' and password==row[1]:
                userid=row[0]
                break
else:
                userid="ERROR"
sql_usrname="select user_id from login"
cursor.execute(sql_usrname)
usrname_data=cursor.fetchall()
if userid =="admin":
	print '''<body><div id="header"></br><h2><span id="span1">%s  &nbsp;&nbsp;&nbsp; 
	<a href="../index.py">logout</h2></a></span></br></div>
	<br><br> <table id="clientdatas" border="1">
        <tr><th>User ID</th> <th>Files uploaded</th> ></tr><tr>'''%(userid)
	for row1 in usrname_data:
		if row1[0] !='admin':
			client_name=row1[0]
			sql_filecount="select filename from usrdata where user_id='%s'" %(client_name)
			cursor.execute(sql_filecount)
			fcount=cursor.rowcount
			print'''<td>%s</td><td>%s</td><tr>'''%(client_name,fcount)
print'</body></html>'
			
db.commit()
db.close()
