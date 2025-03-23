class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        visits = sorted(zip(timestamp, username, website))
        user_web = defaultdict(list)
        for time, user, web in visits:
            user_web[user].append(web)
        count = defaultdict(int)
        for user, site in user_web.items():
            if len(site) < 3:
                continue
            seen_pattern = set()
            for i in range(len(site) - 2):
                for j in range(i+1, len(site) - 1):
                    for k in range(j+1, len(site)):
                        pat = (site[i], site[j], site[k])
                        if pat not in seen_pattern:
                            count[pat] += 1
                            seen_pattern.add(pat)
        return min(count.keys(), key=lambda k: (-count[k], k))

