class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []

        path_arr = path.split("/")
        print(path_arr)

        for pa in path_arr:
            if pa == "" or pa == ".":
                continue
            elif pa == "..":
                if res:
                    res.pop()
            else:
                res.append(pa)

        return "/" + "/".join(res)