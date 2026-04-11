class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        
        cols = len(encodedText) // rows
        result = []
        for j in range(cols):
            rp = 0
            cp = j
            while rp < rows and cp < cols:
                idx = rp * cols+cp
                result.append(encodedText[idx])
                rp += 1
                cp += 1
        return ''.join(result).rstrip()

