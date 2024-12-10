import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SMTP Server Configuration
#SMTP_SERVER = "smtp.office365.com"
SMTP_SERVER= "smtp.rediffmail.com"
SMTP_PORT = 587
EMAIL= "nikhilvargudedevops@rediffmail.com"
#EMAIL = "nikhilvargudedevops@outlook.com"
#EMAIL = "nikhilvargudedevops@gmail.com"
#PASSWORD = "sgpxctyzdgrejryz"  # Replace with app-specific password
PASSWORD = "ft74pezmop44go444c"

# Create and send the email
def send_email():
    subject = "Testing SMTP"
    body = "This is a test email sent from Python."
    recipient = "nikhilvargudedevops@gmail.com"

    # Create the email structure
    message = MIMEMultipart()
    message["From"] = EMAIL
    message["To"] = recipient
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            #server.set_debuglevel(1)  # Enable debugging to see detailed logs
            server.starttls()  # Start secure connection
            server.login(EMAIL, PASSWORD)  # Use plain credentials
            server.sendmail(EMAIL, recipient, message.as_string())
            print(f"Email sent successfully to {recipient}")
    except smtplib.SMTPAuthenticationError as auth_error:
        print(f"SMTP Authentication Error: {auth_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    send_email()
