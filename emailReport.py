import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(subject, body, to_email, from_email, smtp_server, smtp_port, smtp_user, smtp_password):
    try:
        # Create the message
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Create server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()

        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    subject = "Test Email"
    body = "This is a test email without attachment."
    to_email = "gracepan922@gmail.com"
    from_email = "zpan01080124@gmail.com"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = "zpan01080124@gmail.com"
    smtp_password = os.getenv('SMTP_PASSWORD')

    print("SMTP_PASSWORD is set to:", smtp_password)

    if smtp_password is None:
        print("Error: SMTP_PASSWORD environment variable is not set.")
    else:
        send_email(subject, body, to_email, from_email, smtp_server, smtp_port, smtp_user, smtp_password)







