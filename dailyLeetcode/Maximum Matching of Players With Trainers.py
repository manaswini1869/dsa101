class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        matches = 0

        i, j = 0, 0
        n = len(trainers)
        while j < n and i < len(players):
            if players[i] <= trainers[j]:
                matches += 1
                i += 1
                j += 1
            else:
                j += 1


        return matches
