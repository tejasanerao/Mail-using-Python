import smtplib
import getpass
from email.message import EmailMessage

mailItHeader = '''
 __________________________________________________________
| _______________________________________________________  |
| |        __  __       _ _     _______  _________       | |
| |       |  \/  |     (_) |   |__   __||___   ___|      | |
| |       | \  / | __ _ _| | ___  | |       | |          | |
| |       | |\/| |/ _` | | ||___| | |       | |          | |
| |       | |  | | (_| | | |    __| |__     | |          | |
| |       |_|  |_|\__,_|_|_|   |_______|    |_|          | |
| |______________________________________________________| |
|__________________________________________________________|

'''
print('\033[96m {}\033[00m'.format(mailItHeader))
note = '''
NOTES:
1.This script only works with gmail accounts.
2.If your 2-step verification is not ON then turn ON the Less Secure Apps option of your google account
3.If your 2-step verification is ON then you need to create a app password for your device which will allow you to send mails through that device
  and use the same password for login in this script
'''
print('\033[31m {}\033[00m'.format(note))
input("Press Enter to Start...")

sender_mail = input('\033[33m{}\033[00m'.format("Your mail: "))
passw = getpass.getpass('\033[92m{}\033[00m'.format("Password(Hidden): "))
no_of_recipients = int(input('\nHow many recipients? '))
recipients = []
for i in range(no_of_recipients):
    r = input('\033[35m{}\033[00m'.format('Recipient '+str(i+1)+': '))
    recipients.append(r)

print("\n~~~~~~~~~~~~EMAIL CONTENT~~~~~~~~~~~~\n")
subject = input('Subject: ')
body = input('Body: ')
msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = sender_mail
msg['To'] = recipients
msg.set_content(body)

with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    try:
        smtp.login(sender_mail, passw)
        smtp.send_message(msg)
        print('EMAIL SENT SUCCESSFULLY')
    except:
        print('EMAIL NOT SENT')
