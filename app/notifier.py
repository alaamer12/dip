from abc import ABC, abstractmethod
from app.message import Message

class Notifier(ABC):
    @abstractmethod
    def send_message(self, message: Message):
        pass

class EmailNotifier(Notifier):
    def send_message(self, message: Message):
        print(f"Sending email: {message.content}")

class SMSNotifier(Notifier):
    def send_message(self, message: Message):
        print(f"Sending SMS: {message.content}")
