from celery import Celery
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')

@app.task
def send_mail(send_from, send_to, subject, text, text_name, file=None):
	msg = MIMEMultipart()
	msg['From'] = send_from
	msg['To'] = send_to
	msg['Subject'] = subject

	msg.attach(MIMEText(text))

	ff = open(file, "rb")
	part = MIMEApplication(
	    ff.read(),
	    Name=basename(file)
	)
	# After the file is closed
	part['Content-Disposition'] = 'attachment; filename="%s"' % text_name+'.png'
	msg.attach(part)
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(send_from, password)
	server.sendmail(send_from, send_to, msg.as_string())
	server.close()
	return 'email_sent'
