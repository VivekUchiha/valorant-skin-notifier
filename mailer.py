import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase 
from email import encoders 

def send_mail(text, receiver_address):
    # The sender gmail addresses and password
    # it is recommended to use app passwords https://support.google.com/accounts/answer/185833?hl=en 
    sender_address = 'test@test.com'
    sender_pass = ''

    session = smtplib.SMTP('smtp.gmail.com', 587) # use gmail with port
    session.starttls()
    session.login(sender_address, sender_pass) # login with mail_id and password

    message = MIMEMultipart()
    message['From'] = sender_address
    message['Subject'] = 'Valorant Daily Store'
    message['To'] = receiver_address
    mail_content = 'Skins in store today \n\n' + text
    message.attach(MIMEText(mail_content, 'plain'))
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    print(f'Mail Sent to {receiver_address}')
    session.quit()

if __name__ == "__main__":
    send_mail("Test", "test@test.com")