import smtplib
from email.message import EmailMessage

# Set up the email content and details
email = EmailMessage()
email['From'] = 'johndoe@gmail.com'
email['To'] = 'doejohn@gmail.com'
email['Subject'] = 'Automated Python Email'
email.set_content('This is an automated email sent using the favourite programming language, Python.')

# Connect to the SMTP server and send the email
# Using Gmail as the SMTP for example
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()  # Enable encryption
    smtp.login('johndoer@gmail.com', 'password')  # Replace with your email and password
    smtp.send_message(email)
