#!/usr/bin/python
print "Content-type:text/html\r\n\r\n"
print """<html>
  <head>
    <title>mycloud</title>
    <link rel="stylesheet" type="text/css" href="style1.css"></head>
   </head>"""
print '''
  <body>
  <div id="header">
  <form action="/main.py" method="post">
   <div id="header1">
  <table><tr>'''
print '''
 &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;<td> <input type="text" name="username" placeholder=" Username " required/></td>
  &nbsp;&nbsp;&nbsp;<td><input type="password" name="password" placeholder=" Password " required/></td>
  &nbsp;&nbsp;
  <td><input type="submit" value="Client_login"/></td>
  <td><input type="submit" formmethod="post" formaction="admin.py" value="Admin_login">  </tr>
  </table></div>
  </form></div>'''
print '''
  <img id="logo" src="../images/bg.jpg" alt="mycloud" >
             <div id="reg"><ul> <form action="/main.py" method="post">
		    <br><br><br><br> <li><h1>register</h1></li></br><li><input  type="text" name="reg_username" size="35" placeholder=" Username " required/></li></br>
		     <li><input  type="password" name="reg_password" size="35" placeholder=" Password " required/></li></br>
		     <li><input  type="password" name="confirm_password" size="35" placeholder=" Confirm password " required/></li></br>
		     <li><input  type="text" size="35" placeholder=" Country "/></li></br>
		     <li><input  type="submit" value="register"/></li></form>	
		     </ul></div>'''
  
print'''</body> </html>'''
