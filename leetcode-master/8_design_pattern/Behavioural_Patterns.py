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

# Itetator
# Many objects in python have built-in interators. Using the key word 'in' can conveniently iterate through an array
# Defines how the vlaues in an object can be iterated through in python
myList = [1, 2, 3, 4, 5]
for n in myList:
    print(n)
    
# For more complex objects: Linked Lists/ Binary Search Tree, we can define our own iterators

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None # ListNode with vale and next pointer
        
class LinkedList:
    def __init__(self, head):
        self.head = head
        self.cur = None # and LinkedList with a head pointer and a current pointer

    #First, define an iterator with iter function
    def __iter__(self):
        self.cur = self.head # set the current pointer to the head
        return self # return the references to the LinkedList
    
    #To get the next value in the sequence, we defined the next function:
    def __next__(self):
        if self.cur:
            val = self.cur.val
            self.cur = self.cur.next
            return val # if current function is non-null, return the value, and shift the current pointer
        else:
            raise StopIteration # when reach the end of the linked list, sent a signal that will stop iterating

# Initialize LinkedList
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
myList = LinkedList(head)


# Open-Close Principle: Strategy Patterns
# A Class is: Open for extension ; Closed for modifications 
# A class may have different behaviour, or invoke a different method based on something we define(i.e. a Strategy). 
# 1. we can filter an array by removing positive values; 2. filter it by removing all odd values 3....

from abc import ABC, abstractclassmethod
class FilterStrategy(ABC):
    @abstractclassmethod
    def removeValue(self, val):
        pass # Create a FilterStrategy(ABC) 
    
class RemoveNegativeStrategy(FilterStrategy):
    def removeValue(self, val):
        return val < 0 #implementation will remove all the negative vlaues
    
class RemoveOddStrategy(FilterStrategy):
    def removeValue(self, val):
        return abs(val) % 2 # this implementation will remove all odd values
    
class Values: #put strategy into Values Object
    def __init__(self, vals):
        self.vals = vals
        
    def filter(self, strategy):
        res = []
        for n in self.vals:
            if not strategy.removeValue(n):
                res.append(n)
        return res
    
values = Values([-2, -3, -4, 5, 6, 7, 8])
print(values.filter(RemoveNegativeStrategy()))
print(values.filter(RemoveOddStrategy()))
# this way can add additional strategy without modifying the Values class

# Structual Patterns (Facade): is a simple wrapper class that can be used to abstract lower-level details that we don't want to worry about

# Python array are dynamic by default, but this is an example of resizing
class Array:
    def __init__(self):
        self.capacity = 2
        self.length = 0
        self.arr = [0] * 2 
    
    #Insert n in the last position of the array
    def pushback(self, n):
        if self.length == self.capacity:
            self.resize()
        #insert at next empty position
        self.arr[self.length] = n
        self.length += 1
        
        
    def resize(self):
        #Create new array of double capacity
        self.capacity = 2 * self.capacity
        newArr = [0] * self.capacity
        #Copy elements to newArr
        for i in range(self.length):
            newArr[i] = self.arr[i]
        self.arr = newArr
        
    #Remove the last element in the array
    def popback(self):
        if self.length > O:
            self.length -= 1

        
        