#!/usr/bin/python
# HTTP Header
import cgi
import cgitb
cgitb.enable()
form = cgi.FieldStorage()
fname=form.getvalue('fdownload')
print "Content-Type:application/octet-stream;" #name=\"sample.txt\"\r\n";
print "Content-Disposition: attachment; filename=%s"%(fname)
print 
# Actual File Content will go hear.
fo = open("/var/www/cgi-bin/files/"+fname, "rb")
str = fo.read()
print str

# Close opened file
fo.close()

