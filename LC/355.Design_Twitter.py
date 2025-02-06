import heapq
from collections import defaultdict, deque

class Twitter(object):

    def __init__(self):
        # Create a hashmap (dictionary) to store user tweets
        self.user_tweets = defaultdict(deque)
        # Create a hashmap (dictionary) to store follow relationships
        self.following = defaultdict(set)
        # Initialize a timestamp for sorting tweets chronologically
        self.timestamp = 0

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        # Increase the timestamp each time a tweet is posted
        self.timestamp += 1

        # Populate the hashmap with the tweet, associated with the user
        if len(self.user_tweets[userId]) >= 10:
            self.user_tweets[userId].pop()
        self.user_tweets[userId].appendleft((self.timestamp, tweetId))

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        # Use a min-heap to get the 10 most recent tweets
        min_heap = []

        # Populate the heap with the user's own tweets
        for tweet in self.user_tweets[userId]:
            heapq.heappush(min_heap, tweet)
            if len(min_heap) > 10:
                heapq.heappop(min_heap)

        # Populate the heap with the tweets from the users this user follows
        for followeeId in self.following[userId]:
            for tweet in self.user_tweets[followeeId]:
                heapq.heappush(min_heap, tweet)
                if len(min_heap) > 10:
                    heapq.heappop(min_heap)

        # Retrieve tweets from the heap and sort them by timestamp
        min_heap.sort(reverse=True, key=lambda x: x[0])
        return [tweetId for _, tweetId in min_heap]

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        # Use the hashmap to store the follow relationship
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        # Remove the follow relationship if it exists
        self.following[followerId].discard(followeeId)
