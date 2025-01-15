import javax.mail.*;
import javax.mail.internet.*;
import java.util.Properties;

public class RediffSMTPExample {
    public static void main(String[] args) {
        String smtpHost = "smtp.rediffmail.com";
        int smtpPort = 25; // Port for free users
        final String username = "nikhilvargude@rediff.com";
        final String password = "28vb3u3j8c0044wo";

        String recipient = "nikhil.vargude@ifinixfintech.com";
        String subject = "Test Email";
        String body = "This is a test email using Rediffmail SMTP settings.";

        Properties props = new Properties();
        props.put("mail.smtp.host", smtpHost);
        props.put("mail.smtp.port", smtpPort);
        props.put("mail.smtp.auth", "true");
        props.put("mail.smtp.starttls.enable", "true");

        Session session = Session.getInstance(props, new Authenticator() {
            protected PasswordAuthentication getPasswordAuthentication() {
                return new PasswordAuthentication(username, password);
            }
        });

        try {
            Message message = new MimeMessage(session);
            message.setFrom(new InternetAddress(username));
            message.setRecipients(Message.RecipientType.TO, InternetAddress.parse(recipient));
            message.setSubject(subject);
            message.setText(body);

            Transport.send(message);
            System.out.println("Email sent successfully!");
        } catch (MessagingException e) {
            e.printStackTrace();
        }
    }
}
