class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list) #userId = [time, tweetId]
        self.follower = defaultdict(set) #userId = [followeeId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = list(self.follower[userId])
        users.append(userId)

        minHeap = []
        for u in users:
            for t in self.tweets[u][-10:]:
                heapq.heappush(minHeap, t)
                while len(minHeap) > 10:
                    heapq.heappop(minHeap)
        
        res = []
        while minHeap:
            time, tweetId = heapq.heappop(minHeap)
            res.append(tweetId)

        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follower[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].discard(followeeId)
