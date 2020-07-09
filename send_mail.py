import smtplib
from email.message import EmailMessage

# CREDENTIALS
creds = open("creds/mdc_gmail.txt").readlines()
my_email = creds[0][:-1]
my_password = creds[1]
# RECIPIENT DETAILS
company_name = "Mars De' Coder"
recipient_name = "Shovon"
recipient_email = "shovon@marsdecoder.com"
# MESSAGE DETAILS
msg = EmailMessage()
msg['From'] = "Mars De' Coder"
msg['To'] = recipient_email
msg['Subject'] = f"Private, online data science training exclusively for {company_name}"
# PLAIN TEXT MSG SETUP
msg_addressing_plain = f'Hi {recipient_name},'
msg_body_plain = open("plain_text_msg.txt").read()
msg.set_content(f'{msg_addressing_plain}{msg_body_plain}')
# HTML MSG SETUP
msg_addressing_html = f'<p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Hi {recipient_name},</span></p>'
msg_body_html = open("html_msg.txt").read()
msg.add_alternative(f'{msg_addressing_html}{msg_body_html}', subtype='html')
# SEND MESSAGE
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(my_email, my_password)
    smtp.send_message(msg)
