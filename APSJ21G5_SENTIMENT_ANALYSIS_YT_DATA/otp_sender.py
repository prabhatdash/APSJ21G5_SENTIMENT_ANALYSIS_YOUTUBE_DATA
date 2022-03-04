import smtplib
import random
def otp_sender(email):
    otp=str(random.randint(100000,999999))
    SUBJECT = 'OTP FOR LOGIN'
    TEXT = 'YOUR OTP TO LOGIN IS:' + otp
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('group5@apsjorhat.org', 'apsj#12345678')
    message = 'Subject:{} \n\n{}'.format(SUBJECT, TEXT)
    s.sendmail('group5@apsjorhat.org', email, message)
    s.quit()
    return otp
