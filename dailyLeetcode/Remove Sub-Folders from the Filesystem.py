class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = []
        for fold in folder:
            if not res or not fold.startswith(res[-1] + '/'):
                res.append(fold)
        return res