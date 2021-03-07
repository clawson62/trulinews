import cgi
import cgitb #found this but isn't used?

form = cgi.FieldStorage()

name = form.getvalue('Name')
email = form.getvalue('Email')




print (name)
print(email)