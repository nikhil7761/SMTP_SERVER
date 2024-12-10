import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Gmail credentials
sender_email = "nikhilvargudedevops@gmail.com"
app_password = "fzvteglpegkeqqwr"  # Generated App Password
receiver_email = "shreyash.bongulwar@ifinixfintech.com"

# Email content
subject = "Test Email from Python"
body = "This is a test email sent using Python and Gmail with an app password."

# Create the email message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

try:
    # Connect to Gmail's SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Start TLS encryption
        server.login(sender_email, app_password)  # Login with app password
        server.send_message(message)  # Send the email
        print("Email sent successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
