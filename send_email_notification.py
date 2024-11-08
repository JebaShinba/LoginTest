import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email(subject, body):
    sender_email = "jebashinba2001@gmail.com"
    sender_password = "rjos mxvq elqt yugu"  # Use the App Password instead of your Gmail password
    recipient_email = "jeba@nidrive.in"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)  # Log in using the app password
            server.sendmail(sender_email, recipient_email, msg.as_string())  # Send the email
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    send_email("Test Subject", "selenium scripts failed.")
