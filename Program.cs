using System;
using MimeKit;
using MailKit.Net.Smtp;

class Program
{
    static void Main(string[] args)
    {
        try
        {
            // Create the email message
            var message = new MimeMessage();
            message.From.Add(new MailboxAddress("Your Name", "your-email@domain.com"));
            message.To.Add(new MailboxAddress("Recipient Name", "recipient-email@domain.com"));
            message.Subject = "Test Email from .NET using Postfix";

            message.Body = new TextPart("plain")
            {
                Text = "Hello, this is a test email sent using .NET and Postfix SMTP server."
            };

            // Send the email using the Postfix server at 172.30.1.24 on port 587
            using (var client = new SmtpClient())
            {
                // Connect to the Postfix server at 172.30.1.24, port 587 (StartTLS)
                client.Connect("172.30.2.90", 587, MailKit.Security.SecureSocketOptions.StartTls);

                // No authentication required, so no need to call Authenticate

                // Send the email
                client.Send(message);
                client.Disconnect(true);
            }

            Console.WriteLine("Email sent successfully!");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Failed to send email. Error: {ex.Message}");
        }
    }
}
