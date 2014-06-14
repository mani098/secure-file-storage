#!/usr/bin/python
import cgi, cgitb; cgitb.enable()
import MySQLdb
import time

print "Content-type:text/html\r\n\r\n"
form = cgi.FieldStorage()
uname=form.getvalue('usrname')
filename = form.getvalue('fview')
print '<html>'
db=MySQLdb.connect("localhost",'root','mani',"mycloud")
cursor=db.cursor()
sql_fview="select * from usrdata where filename='%s' and user_id='%s'"%(filename,uname)
cursor.execute(sql_fview)
fview_data=cursor.fetchone()
f_path="/var/www/cgi-bin/files/"
f1=open(f_path+"cloudA/"+fview_data[3],'r')
f2=open(f_path+"cloudB/"+fview_data[4],'r')
print "<head><title>%s-view</title></head>"%filename
print '<link rel="stylesheet" type="text/css" href="style2.css"></head>'
print '''<body><div id="header"></br><h2><span id="span1">%s  &nbsp;&nbsp;&nbsp; 
<a href="../index.py">logout</h2></a></span></br></div>'''%(uname)
print '''<center><h2 id="f_name">Filename: %s</h2></br>'''%fview_data[1]

print"<h2>F_slice_1: %s</h2>"%fview_data[3]
print'''<textarea name="textcontent" cols="90" rows="10">
%s
</textarea><br>'''%f1.read()
print"<br><br><h2>F_slice_2: %s</h2>"%fview_data[4]
print'''<textarea name="textcontent1" cols="90" rows="10">
%s
</textarea><br>'''%f2.read()
print'''<form action="download.py" method="post">
<input type="text" name="fdownload" value=%s hidden>
<br><input type="submit" value="Download">
</form></center>'''%filename
print "</body></html>"
