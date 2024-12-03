import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SMTP Server Configuration
SMTP_SERVER = "smtp.gmail.com"  # Change to smtp.gmail.com or smtp.office365.com as needed
SMTP_PORT = 587               # Use 587 for STARTTLS
EMAIL = "nikhilvargudedevops@gmail.com" # Replace with your email
PASSWORD = "fzvteglpegkeqqwr"    # Replace with your password or app-specific password

# Create the Email
def send_email():
    subject = "Subject of the Email"
    body = "this mail is testing purposes please do not reply to it"
    recipient = "nikhilvargudedevops@zohomail.in"

    # Create a MIME multipart message
    message = MIMEMultipart()
    message["From"] = EMAIL
    message["To"] = recipient
    message["Subject"] = subject

    # Attach the plain text body
    message.attach(MIMEText(body, "plain"))

    try:
        # Connect to the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade connection to secure
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, recipient, message.as_string())
            print(f"Email sent successfully to {recipient}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    send_email()
