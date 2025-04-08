class Twitter:

    def __init__(self):
        self.time = 0
        self.user_follow = defaultdict(set) # list of followee -> follower
        self.user_post = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_post[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.user_follow[userId].add(userId)
        for followerId in self.user_follow[userId]:
            if followerId in self.user_post:
                index = len(self.user_post[followerId]) - 1
                count, tweetId = self.user_post[followerId][index]
                heapq.heappush(minHeap, [count, tweetId, followerId, index-1])
        while minHeap and len(res) < 10:
            count, tweetId, followerId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.user_post[followerId][index]
                heapq.heappush(minHeap,[count, tweetId, followerId, index-1])
        return res
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.user_follow[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_follow[followerId].discard(followeeId)
