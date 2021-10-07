import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = “alamat pengirim”
toaddr = “alamat penerima”
msg = MIMEMultipart()
msg[‘From’] = fromaddr
msg[‘To’] = toaddr


body = “isi pesan”
msg.attach(MIMEText(body, ‘plain’))
server = smtplib.SMTP(‘smtp.gmaicom’, 587)
server.login(fromaddr, “passwd pengirim”)
text = msg.as_string
server.sendmail(frmaddr, toaddr, text)
server.quit()
