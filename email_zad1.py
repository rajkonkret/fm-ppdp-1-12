import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = ''
smtp_port = 587
email_address = ''
password = ''
to = ""

wiadomosc = MIMEMultipart()
wiadomosc['From'] = email_address
wiadomosc["To"] = to
wiadomosc['Subject'] = "Wiadomośc z systemu"

tresc = "Zosatłeś zainfekowany pythonem"
wiadomosc.attach(MIMEText(tresc, "plain"))

try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(email_address, password)
        server.sendmail(email_address, to, wiadomosc.as_string())
        print("E-mail został wysłany")
except Exception as e:
    print("Bład", e)
