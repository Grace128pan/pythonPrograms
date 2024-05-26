'''
1. We should use gmail account to generate the password for the smtp_password.
2. the generated password should be stored in .env file
3. $env:SMTP_PASSWORD = "sapg gdrd gnds gudl"
Write-Output $env:SMTP_PASSWORD
in the terminal or powershell, we should do the above command to set the password.
4. the sender email should enable IMAP(settings-Forwarding and Pop/IMAP-IMAP access-Enable IMAP)
5. The .env file should be in the same directory as the python file.
ps:This code might not run as I removed the generated password from the .env file.
'''


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(subject, body, to_email, from_email, smtp_server, smtp_port, smtp_user, smtp_password, attachment_path=None):
    try:
        # Create the message
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))

        # Attach any files if provided
        if attachment_path:
            filename = os.path.basename(attachment_path)
            try:
                with open(attachment_path, "rb") as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f"attachment; filename= {filename}")
                msg.attach(part)
            except Exception as e:
                print(f"Failed to attach file: {e}")
                return

        # Create server
        print(f"Connecting to server {smtp_server} on port {smtp_port}...")
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Login Credentials for sending the mail
        if smtp_password is None:
            raise ValueError("SMTP password is not set. Please set the SMTP_PASSWORD environment variable.")

        print("Logging in...")
        server.login(smtp_user, smtp_password)

        # Send the mail
        print("Sending email...")
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()

        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    # Set email parameters
    subject = "Daily Report"
    body = "Please find the daily report attached."
    to_email = "gracepan922@gmail.com"
    from_email = "zpan01080124@gmail.com"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = "zpan01080124@gmail.com"
    
    # Use environment variables to store sensitive information
    smtp_password = os.getenv('SMTP_PASSWORD')
    print("SMTP_PASSWORD is set to:", smtp_password)

    if smtp_password is None:
        print("Error: SMTP_PASSWORD environment variable is not set.")
    else:
        attachment_path = "python_makinggames.pdf"  # Ensure the file exists at this path

        send_email(subject, body, to_email, from_email, smtp_server, smtp_port, smtp_user, smtp_password, attachment_path)
