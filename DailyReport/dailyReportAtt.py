# step1: use .env to store sender email and password
# step2: from dotenv import load_dotenv
# step3: load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))
# step4: from_email = os.getenv('EMAIL_USER')
# step5: password = os.getenv('EMAIL_PASSWORD')
# step6: Add paths to attachments here
# step7: user gmail should be able to generate app password for security reasons
# step8: gmail settings should enable SMTP access
# step9: check emails whether it works of not
# step10: remove generated password for security


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import datetime
import os
from dotenv import load_dotenv

# Determine the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Load environment variables from .env file located in the same directory as the script
load_dotenv(dotenv_path=os.path.join(script_dir, '.env'))

def send_email(subject, body, to_emails, attachment_paths=None):
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

    # Attach files if specified
    if attachment_paths:
        for attachment_path in attachment_paths:
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

    # Add paths to attachments here
    attachment_paths = [
        os.path.join(script_dir, 'python_makinggames.pdf')

    ]
    
    send_email(subject, body, to_emails, attachment_paths)
