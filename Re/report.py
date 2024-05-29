import yagmail

def send_email(subject, body, to_email, attachment_paths=None):
    # Initialize yagmail SMTP connection
    yag = yagmail.SMTP('zpan01080124@gmail.com', 'jonmhkxxddvnlquj')

    # Send email
    yag.send(to=to_email, subject=subject, contents=body, attachments=attachment_paths)

if __name__ == '__main__':
    subject = "Daily Report"
    body = "Please find the daily report attached."
    to_email = "gracepan922@gmail.com"  # Replace with recipient email address

    attachment_paths = ["games.pdf"]  # Replace with correct attachment path

    send_email(subject, body, to_email, attachment_paths)


