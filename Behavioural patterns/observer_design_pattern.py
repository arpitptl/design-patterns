"""
Observer design pattern:

The Observer design pattern is used when you want to establish a one-to-many dependency between objects, where one object (subject) changes its state, and all its dependents (observers) are notified automatically. Here's an example of the Observer pattern in Python:.
"""

# Subject (Observable) class
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

# Observer (Observer) class
class Observer:
    def update(self, message):
        pass

# Concrete Subject class
class NewsAgency(Subject):
    def __init__(self):
        super().__init__()
        self._latest_news = None

    def set_news(self, news):
        self._latest_news = news
        self.notify(news)

# Concrete Observer class
class NewsChannel(Observer):
    def __init__(self, name):
        self._name = name

    def update(self, message):
        print(f"{self._name} received news: {message}")

# Example usage
if __name__ == "__main__":
    agency = NewsAgency()

    channel1 = NewsChannel("Channel 1")
    channel2 = NewsChannel("Channel 2")

    agency.attach(channel1)
    agency.attach(channel2)

    agency.set_news("Breaking News: Python ranked as the most popular language!")

    agency.detach(channel1)

    agency.set_news("New AI breakthrough announced!")





"""
In this example, we have the Subject class (NewsAgency) that maintains a list of observers (NewsChannel). The Subject provides methods to attach and detach observers and a notify() method to inform all attached observers when its state changes.

The Observer class is an abstract class with an update() method. Concrete observers (NewsChannel) inherit from the Observer class and implement the update() method to respond to updates from the subject.

When the NewsAgency updates its state by setting the latest news using the set_news() method, it calls the notify() method to inform all its attached observers. Each observer (NewsChannel) receives the news and processes it by printing it in this example.

By using the Observer pattern, the NewsAgency can notify multiple NewsChannel objects without being aware of their specific implementations. This design promotes loose coupling between the NewsAgency and the NewsChannel, making it easy to add or remove observers without affecting the subject's logic.
"""
