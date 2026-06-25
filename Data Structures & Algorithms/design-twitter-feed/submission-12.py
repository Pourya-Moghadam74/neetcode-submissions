class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list) #userId = [(time, tweeitId)]
        self.following = defaultdict(set) #userId = {followeeId}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = list(self.following[userId])
        users.append(userId)
        maxHeap = []

        for user in users:
            for time, tweetId in self.tweets[user][-10:]:
                maxHeap.append((time, tweetId))
            
        heapq.heapify_max(maxHeap)

        res = []

        while maxHeap and len(res) < 10:
            time, tweetId = heapq.heappop_max(maxHeap)
            res.append(tweetId)

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
