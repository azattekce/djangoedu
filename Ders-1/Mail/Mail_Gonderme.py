import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart()

mesaj["From"] = "azattekce@gmail.com"

mesaj["To"] = "azat.tekce@opet.com.tr"

mesaj["Subject"] = "Smtp Mail Gönderme"


yazi = """

Smtp ile mail gönderiyorum.

Mustafa Murat Coşkun


"""


mesaj_govdesi = MIMEText(yazi,"plain")

mesaj.attach(mesaj_govdesi)

try:
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("azattekce@gmail.com","Az.123456+1")
    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())

    print("Mail Başarıyla Gönderildi....")

    mail.close()

except Exception as hata:
    sys.stderr.write("Bir sorun oluştu! : {}".format(hata))
    sys.stderr.flush()







