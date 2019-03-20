#Hey everybody , this code it just for facilitate task of sending msg to many emails here its just for gmail . but you can change the host and port for other mails platformes .
#If you've any problems or need some support please contact me , on Github or any other platforme . Good luck

import smtplib
from email.mime.text import MIMEText

f = open("your_email_list.txt","r")
myList = []
for line in f:
        myList.append(line)

print(myList)

sender = "Your email"
receivers = myList
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
msg = MIMEText('Your message')
msg['Subject'] = "subject line"
msg['From'] = sender
msg['To'] = ", ".join(receivers)
server.login('Your email ','Your password')
server.sendmail(sender, receivers, msg.as_string())
server.quit()
print("Your message was sent successfully")

#Notice : Do not show your code after editing, cause will contain sensitive informations .
#Notice_1 : if you need for exemple to send to outlook's emails you need to put server=smtplib.SMTP('smtp-mail.outlook.com', 587), and it will works so well .
