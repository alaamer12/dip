from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def send_message(self, message):
        pass


class EmailNotifier(Notifier):
    def send_message(self, message):
        print(f"Sending email: {message}")


class SMSNotifier(Notifier):
    def send_message(self, message):
        print(f"Sending SMS: {message}")


from injector import Binder, Module


class NotifierModule(Module):
    def configure(self, binder: Binder):
        binder.bind(Notifier, to=EmailNotifier)


from injector import Injector

injector = Injector([NotifierModule()])
notifier = injector.get(Notifier)

notifier.send_message("Hello, World!")
