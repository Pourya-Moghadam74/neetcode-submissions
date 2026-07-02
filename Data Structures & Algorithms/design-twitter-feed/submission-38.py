class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list) #[userId] = [time, tweetId]
        self.following = defaultdict(set) #[userId] = (followeeId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []
        followeeIds = self.following[userId]
        followeeIds.add(userId)

        for followeeId in followeeIds:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId]) - 1
                time, tweetId = self.tweets[followeeId][index]
                heapq.heappush_max(maxHeap, (time, tweetId, followeeId, index - 1))

        while maxHeap and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop_max(maxHeap)
            res.append(tweetId)
            
            if index >= 0:
                time, tweetId = self.tweets[followeeId][index]
                heapq.heappush_max(maxHeap, (time, tweetId, followeeId, index - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
