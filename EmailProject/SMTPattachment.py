import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

me = "ljbryant8888@gmail.com"
you = "bryantlj@rose-hulman.edu"

msg = MIMEMultipart('related')
msg['Subject'] = 'CSSE432 Homework 2 Logan Bryant'
msg['From'] = me
msg['To'] = you
msg.preamble = 'This is a super cool multipart message using html and python c:'

msgAlt = MIMEMultipart('alternative')
msg.attach(msgAlt)


textToSend = """
poggers
"""
msgTxt = MIMEText(textToSend)
msgAlt.attach(msgTxt)

thehtmlcode = """
<html>
<head>Test Header</head>
<body>
<p>This isn't plain text!<br>
If you're seeing this everything should be working as planned :D<br>
Here's the gif <a href="http://tinypic.com?ref=2wpnfnt" target="_blank"><img src="http://i43.tinypic.com/2wpnfnt.gif" border="0" alt="Image and video hosting by TinyPic"></a>
</p>
</body>
</html>
"""
msgTxt = MIMEText(thehtmlcode, msgAlt.attach(msgTxt))

fp = open('../../KingsmanGif.gif', 'rb')
msgImg = MIMEImage(fp.read())
fp.close()

fp = open('../../KingsmanImage.jpg', 'rb')
msgImg2 = MIMEImage(fp.read())
fp.close()


msgImg.add_header('EMEGRENCY thing', '<Itsapicture>')
msg.attach(msgImg)
msg.attach(msgImg2)

# s = smtplib.SMTP('rosehulman-edu01b.mail.protection.outlook.com', 25)
# s.send_message(msg)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('ljbryant8888@gmail.com', "bflcwxjyffucwdwf")
server.send_message(msg)
server.quit()