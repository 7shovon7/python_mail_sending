import smtplib
from email.message import EmailMessage
from gsheet import authenticate


# USE THE AUTHENTICATION
client = authenticate("creds/creds.json")
# OPEN SHEET AND DO SOME MODIFICATIONS
sheet_url = "https://docs.google.com/spreadsheets/d/1DNKBYN3SQHPvjdy7eQ018t5HDaU-qDuzULcGqV5qJm8/edit#gid=408336874"
workbook = client.open_by_url(sheet_url)
selected_tab = workbook.worksheet("Sheet1")

# CREDENTIALS
creds = open("creds/aa_gmail.txt").readlines()
my_email = creds[0][:-1]
my_password = creds[1]
# RECIPIENT DETAILS
# recipient_emails = [
#     'mahmudur.rahman99@gmail.com',
#     'neelameherunnesa@gmail.com',
#     'marsdecoder@gmail.com'
# ]
starting_row = int(input("Enter the Starting Row Number: "))
finishing_row = int(input("Enter the Final Row Number: "))
collected_mails = selected_tab.get(f"H{starting_row}:H{finishing_row}")
recipient_emails = []
for mail in collected_mails:
    recipient_emails.append(mail[0])
# print(recipient_emails)
# MESSAGE DETAILS
def send_email_to(e_mail, smtp):
    msg = EmailMessage()
    msg['From'] = "Amber Abder"
    msg['To'] = e_mail
    msg['Subject'] = "HEAR WHAT PAST ATTENDEES HAD TO SAY ABOUT THEIR SIGNAL EXPERIENCE."
    msg_body = '''
    Hi,
    If you’ve never attended SIGNAL live before,
    then you may not know why thousands of your peers keep it on their can’t miss list each year.
    So we reached out to some past attendees to find out what they love about SIGNAL,
    and we’re excited to share what we learned.
    '''
    msg.set_content(msg_body)
    # SEND MESSAGE
    smtp.send_message(msg)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(my_email, my_password)
    for i in range(len(recipient_emails)):
        try:
            send_email_to(recipient_emails[i], smtp)
        except:
            row_no = starting_row + i
            print(f"{row_no} missed!")