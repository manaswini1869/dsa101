class AuctionSystem:

    def __init__(self):
        self.auctions = defaultdict(dict)
        self.q = defaultdict(list)


    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        self.auctions[itemId][userId] = bidAmount
        heapq.heappush(self.q[itemId], (-bidAmount, -userId))


    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        self.auctions[itemId][userId] = newAmount
        heapq.heappush(self.q[itemId], (-newAmount, -userId))

    def removeBid(self, userId: int, itemId: int) -> None:
        del self.auctions[itemId][userId]


    def getHighestBidder(self, itemId: int) -> int:
        auctions = self.auctions[itemId]
        if not auctions:
            return -1
        q = self.q[itemId]
        while q:
            neg_amount, neg_user = q[0]
            amount = -neg_amount
            user = -neg_user
            if auctions.get(user) == amount:
                return user
            heapq.heappop(q)
        return -1


        # max_amount = 0
        # user_id = 0
        # for id, amount in auctions.items():
        #     if amount > max_amount:
        #         max_amount = amount
        #         user_id = id
        #     elif amount == max_amount:
        #         user_id = max(user_id, id)
        # return user_id



# Your AuctionSystem object will be instantiated and called as such:
# obj = AuctionSystem()
# obj.addBid(userId,itemId,bidAmount)
# obj.updateBid(userId,itemId,newAmount)
# obj.removeBid(userId,itemId)
# param_4 = obj.getHighestBidder(itemId)