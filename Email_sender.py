#Hey everybody , this code it just for facilitate task of sending msg to many emails here its just for gmail . but you can change the host and port for other mails platformes .
#If you've any problems or need some support please contact me , on Github or any other platforme . Good luck


import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

f = open("Your emails list ","r")
myList = []
for line in f:
        myList.append(line)

print(myList)

sender = "your mail"
receivers = myList
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
msg = MIMEText('Your main text')
msg['Subject'] = "subject line"
msg['From'] = sender
msg['To'] = ", ".join(receivers)
server.login('your mail','your mail password')
server.sendmail(sender, recipients, msg.as_string())
server.quit()

#Notice : Do not show your code after editing, cause will contain sensitive informations .