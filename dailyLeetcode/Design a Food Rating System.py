class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_map = defaultdict(list) # food : (rating, cuisine)
        self.food_cuisine = defaultdict(list) # cuisine : (rating, food) <- priority heap
        n = len(foods)
        for i in range(n):
            self.food_map[foods[i]] = (ratings[i], cuisines[i])
            heapq.heappush(self.food_cuisine[cuisines[i]], (-ratings[i], foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        old, cuisine = self.food_map[food]
        self.food_map[food] = (newRating, cuisine)
        heapq.heappush(self.food_cuisine[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        foods_heap = self.food_cuisine[cuisine]
        while foods_heap:
            rating_cuisine, food_name = foods_heap[0]
            rating, _ = self.food_map[food_name]
            if -rating_cuisine == rating:
                return food_name
            heapq.heappop(foods_heap)



# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)