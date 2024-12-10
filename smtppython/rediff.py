import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
smtplib.SMTP.debuglevel = 1  # Enable debug output


# Rediffmail credentials
sender_email = "nikhilvargude@rediffmail.com"
password = "9n4mz6jyjaoso04g8k"  # Your Rediffmail account password
receiver_email = "nikhil.vargude@ifinixfintech.com"

# Email content
subject = "Test Email from Python (Rediffmail)"
body = "This is a test email sent using Python and Rediffmail."

# Create the email message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

try:
    # Connect to Rediffmail's SMTP server using SSL
    with smtplib.SMTP_SSL("smtp.rediffmail.com", 465) as server:
        server.login(sender_email, password)  # Login with Rediffmail account
        server.send_message(message)  # Send the email
        print("Email sent successfully via Rediffmail!")
except Exception as e:
    print(f"An error occurred: {e}")
