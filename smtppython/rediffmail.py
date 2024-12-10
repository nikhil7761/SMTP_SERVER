import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SMTP server details
SMTP_SERVER = "smtp.rediffmailpro.com"
SMTP_PORT = 587

# Credentials
rediff_email = "nikhilvargudedevops@gmail.com"
rediff_password = "a0970jlvvjswkw8c84kc"

# Email details
recipient_email = "nikhilvargudedevops@gmail.com"
subject = "Test Email"
body = "This is a test email."

def send_email():
    try:
        print("Connecting to SMTP server using SSL...")
        context = ssl.create_default_context()
        server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context)
        server.set_debuglevel(1)  # Enable SMTP debug output
        
        print("Logging in...")
        server.login(rediff_email, rediff_password)
        print("Login successful.")

        # Create the email
        msg = MIMEMultipart()
        msg["From"] = rediff_email
        msg["To"] = recipient_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Send the email
        server.sendmail(rediff_email, recipient_email, msg.as_string())
        print(f"Email sent successfully to {recipient_email}")

        server.quit()

    except smtplib.SMTPAuthenticationError as e:
        print(f"SMTP Authentication Error: {e}")
    except smtplib.SMTPException as e:
        print(f"SMTP Error: {e}")
    except Exception as e:
        print(f"General Error: {e}")

if __name__ == "__main__":
    send_email()
