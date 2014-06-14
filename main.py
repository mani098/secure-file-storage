#!/usr/bin/python
import cgi, cgitb; cgitb.enable()
import MySQLdb
import time
#import save_file
print "Content-type:text/html\r\n\r\n"


form = cgi.FieldStorage()
username = form.getvalue('username')
password  = form.getvalue('password')
reg_username=form.getvalue('reg_username')
reg_password=form.getvalue('reg_password')
confirm_password=form.getvalue('confirm_password')


print '<html>'
db=MySQLdb.connect("localhost",'root','mani',"mycloud")
cursor=db.cursor()
sql_login="select * from login"
cursor.execute(sql_login)
login_data=cursor.fetchall()
for row in login_data:
	if username==row[0] and password==row[1]:
		userid=row[0]
		sql_usrdata="select * from usrdata where user_id= '%s'"%(userid)
		cursor.execute(sql_usrdata)
		userdatas=cursor.fetchall()
		break
	elif reg_username:
		userid=reg_username
		sql_reg=" insert into login values('%s','%s')" %(reg_username,reg_password)
		cursor.execute(sql_reg)
		sql_usrdata="select * from usrdata where user_id= '%s'"%(reg_username)
                cursor.execute(sql_usrdata)
                userdatas=cursor.fetchall()
		break
	else:
		userid="ERROR"
			
print '<title>myCloud</title><head>'
#print'''<script>
#function userName()
#{
#  documnet.getElementById("u_id").innerHTML=%s

#}
#</script>'''%(userid)
def user_id():
	return userid
print '<link rel="stylesheet" type="text/css" href="style2.css"></head>'
print '''<body onload="userName()" ><div id="header"></br><h2><span id="span1">%s  &nbsp;&nbsp;&nbsp; 
<a href="../index.py">logout</h2></a></span></br></div>'''%(userid)
if userid !='ERROR':
	print'''<center> <h2> File Upload </h2> </br>
	<form enctype="multipart/form-data"  action="save_file.py"  method="post"> 
	<label for="public">Public</label>
	<input type="radio" name="upload_value" id="public" value="%s" required> &nbsp; &nbsp;
	<label for="private">Private</label>
  	<input type="radio" name="upload_value" id="private" value="%s" required></br></br>
	<input type="file" name="filename" /></br><br>
	<input type="submit"  value="Upload_File"> </form></center> '''%(userid,userid)

	print '''<br><br> <table border="1">
	<tr>
	<th>Filename</th> <th>Fsplit_1</th> <th>Fsplit_2</th> <th>Current Time</th> <th> View file </th>
	</tr><tr>'''
	for data in userdatas:
		print'<td>%s</td>'%data[1]
		print'<td>%s</td>'%data[3]
		print'<td>%s</td>'%data[4]
		print'<td>%s</td>'%time.ctime()
		print'''<td><form action="view.py" method="post">
		<input type="text" value=%s name="usrname" hidden>
		<input type="text" value=%s name="fview" hidden>
		<center><input type="submit" value="View"></form></center></td></tr>'''%(userid,data[1])

	print '</table> '
else:
	print'<h1>Incorrect Username or Password</h1>'
print '</body>'
print '</html>'
db.commit()
db.close()

