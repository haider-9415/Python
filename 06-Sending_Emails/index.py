# install 'secure-smtplib' using pip
import smtplib as sm

# to start server and give port no.
ob = sm.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()

# to login 
# enter email address and password
ob.login("User's email address", "Password")

subject = 'testing'
body = 'i love python'
message = 'subject:{}\n\n{}'.format(subject, body)

listAddrss = ['Enter email addresses to which you want to send email as elements of this list']

# to send email
ob.sendmail("User's email address", listAddrss, message)
print('Email successfuly send')

# to stop the server
ob.quit()