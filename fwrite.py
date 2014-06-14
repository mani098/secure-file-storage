import save_file_test

def filewrite():
	print "filename : "+fn
	print"file content : "+fc
	file_w=open('/tmp/' + fn, 'wb')
	fw.write(fc)
	fw.close()

