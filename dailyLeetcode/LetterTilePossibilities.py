class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def create_tiles(path, visited):
            nonlocal total
            if path:
                total += 1
            for i in range(len(tiles)):
                if visited[i] or (i>0 and tiles[i] == tiles[i-1] and not visited[i-1]):
                    continue
                visited[i] = True
                create_tiles(path + tiles[i], visited)
                visited[i] = False

        tiles = sorted(tiles)
        total = 0
        create_tiles("", [False]*len(tiles))
        return total