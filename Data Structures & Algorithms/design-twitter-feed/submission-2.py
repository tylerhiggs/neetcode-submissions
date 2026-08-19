class Twitter:

    def __init__(self):
        # self.users = {'following': {}, 'tweets': []}
        # heapq.heapify(self.users['tweets'])
        self.users = {}
        self.t = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.ensure_user(userId)
        self.users[userId]['tweets'].append([self.t, tweetId])
        self.t += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.ensure_user(userId)
        top = []
        for user in self.users[userId]['following']:
            for tweet in self.users[user]['tweets'][-10:]:
                heapq.heappush(top, tweet)
                if len(top) == 11:
                    heapq.heappop(top), top
        return [tweet[1] for tweet in sorted(top, key=lambda x:x[0])[::-1]]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.ensure_user(followerId)
        self.ensure_user(followeeId)
        self.users[followerId]['following'].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.ensure_user(followerId)
        self.ensure_user(followeeId)
        if not followeeId in self.users[followerId]['following']:
            return
        self.users[followerId]['following'].remove(followeeId)

    def ensure_user(self, user_id):
        if user_id in self.users:
            return
        self.users[user_id] = {'following': {user_id}, 'tweets': []}
        
