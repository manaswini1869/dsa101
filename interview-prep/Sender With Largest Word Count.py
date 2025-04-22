from collections import defaultdict
class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        freq_map = defaultdict(int)
        max_heap = []
        for i in range(len(senders)):
            sen = messages[i].split()
            freq_map[senders[i]] = freq_map.get(senders[i], 0) + len(sen)

        max_count = -1
        best_sender = ""

        for sender, count in freq_map.items():
            if count > max_count or (count == max_count and sender > best_sender):
                max_count = count
                best_sender = sender

        return best_sender
