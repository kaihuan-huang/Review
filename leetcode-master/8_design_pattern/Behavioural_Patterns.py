# Observer/PubSub
# How components communicate or respond to events or state changes?
# The Observer pattern is a popular solution. We have a Subject(aka Publisher) which will be the source of events.
# Multiples Observer(aka Subscriber) will recieve events from the SUbject realtime

#  Observer/PubSub widely used beyond just Object-oriented programming



class YoutubeChannel:
    def __init__(self, name):
        self.name = name
        self.subscribers = []
        
    def subscribe(self, event):
        self.subscribers.append(event)
        
    def notify(self, event):
        for sub in self.subscribers:
            sub.sendNotification(self.name, event)
            
from abc import ABC, abstractclassmethod

class YoutubeSubscriber(ABC):
    @abstractclassmethod
    def sendNotification(self, event):
        pass
    
class YoutubeUser(YoutubeSubscriber):
    def __init__(self, name):
        self.name = name
    
    def sendNotification(self, channel, event):
        print(f"User {self.name} received notification from {channel}:{event}")
        
channel = YoutubeChannel("ABC")

channel.subscribe(YoutubeUser("sub1"))
channel.subscribe(YoutubeUser("sub2"))
channel.subscribe(YoutubeUser("sub3"))

channel.notify("A new video released!")