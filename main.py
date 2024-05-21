from app.message import Message
from app.notifier import EmailNotifier, SMSNotifier, Notifier

class MessagingApp:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def send_message(self, message_content):
        message = Message(message_content)
        self.notifier.send_message(message)

if __name__ == "__main__":
    # Dependency injection
    email_notifier = EmailNotifier()
    sms_notifier = SMSNotifier()

    # Client code
    email_app = MessagingApp(email_notifier)
    sms_app = MessagingApp(sms_notifier)

    email_app.send_message("Hello, this is an email message!")
    sms_app.send_message("Hello, this is an SMS message!")
