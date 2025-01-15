using System;
using System.Net;
using System.Net.Mail;

class Program
{
    static void Main(string[] args)
    {
        // Rediffmail SMTP Configuration
        string smtpServer = "smtp.rediffmail.com";
        int smtpPort = 465; // Use 465 for SSL or 587 for TLS
        string emailAddress = "nikhilvargude@rediffmail.com";
        string emailPassword = "a0970jlvvjswkw8c84kc"; // Use a secure password or token if applicable
        string recipientEmail = "nikhil.vargude@ifinixfintech.com";

        try
        {
            Console.WriteLine("Connecting to Rediffmail SMTP server...");

            // Create a new MailMessage
            MailMessage mail = new MailMessage
            {
                From = new MailAddress(emailAddress),
                Subject = "Test Email",
                Body = "This is a test email sent using Rediffmail SMTP and .NET.",
                IsBodyHtml = false
            };
            mail.To.Add(recipientEmail);

            // Configure the SMTP client
            SmtpClient smtp = new SmtpClient(smtpServer, smtpPort)
            {
                Credentials = new NetworkCredential(emailAddress, emailPassword),
                EnableSsl = true // Ensure SSL/TLS is enabled
            };

            // Send the email
            smtp.Send(mail);

            Console.WriteLine("Email sent successfully!");
        }
        catch (SmtpException ex)
        {
            Console.WriteLine($"SMTP Error: {ex.Message}");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"General Error: {ex.Message}");
        }
    }
}
