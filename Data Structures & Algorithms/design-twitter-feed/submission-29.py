class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list) #usetId = [(time, tweetId)]
        self.following = defaultdict(set) #userId = (followerId)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []
        users = self.following[userId]
        users.add(userId)

        for user in users:
            if user in self.tweets:
                index = len(self.tweets[user]) - 1
                time, tweetId = self.tweets[user][index]
                heapq.heappush_max(heap, [time, tweetId, user, index - 1])
        
        while heap and len(res) < 10:
            time, tweetId, user, index = heapq.heappop(heap)
            res.append(tweetId)
            if index >= 0:
                time, tweetId = self.tweets[user][index]
                heapq.heappush_max(heap, [time, tweetId, user, index - 1])
        
        return res



    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
