import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

def send_email(subject, body, to_emails, attachment_path=None):
    from_email = os.getenv('EMAIL_USER')
    password = os.getenv('EMAIL_PASSWORD')

    if not from_email or not password:
        raise ValueError("EMAIL_USER and EMAIL_PASSWORD environment variables must be set")

    # Create the email container
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = ', '.join(to_emails)
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    # Attach a file if specified
    if attachment_path:
        with open(attachment_path, 'rb') as file:
            part = MIMEApplication(file.read(), Name=os.path.basename(attachment_path))
            part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
            msg.attach(part)

    # Send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_emails, msg.as_string())

def generate_report():
    # Replace with your report generation logic
    report_content = "Daily Report:\n\nAll systems operational."
    return report_content

if __name__ == '__main__':
    report = generate_report()
    subject = f"Daily Report - {datetime.now().strftime('%Y-%m-%d')}"
    body = report
    to_emails = ['gracepan922@gmail.com']
    
    send_email(subject, body, to_emails)

