class TrieNode:
    def __init__(self):
        self.children = {}
        self.serial = ''
        self.is_deleted = False

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = TrieNode()

        for path in paths:
            node = root
            for folder in path:
                if folder not in node.children:
                    node.children[folder] = TrieNode()
                node = node.children[folder]
        serial_map = defaultdict(list)

        def serialise(node: TrieNode) -> str:
            if not node.children:
                return ""
            serial_parts = []

            for name in sorted(node.children):
                child = node.children[name]
                sub_serial = serialise(child)
                serial_parts.append(f"{name}({sub_serial})")
            node.serial = "".join(serial_parts)
            serial_map[node.serial].append(node)

            return node.serial

        serialise(root)

        for nodes in serial_map.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.is_deleted = True

        res = []

        def collect(node: TrieNode, path: List[str]):
            for name, child in node.children.items():
                if not child.is_deleted:
                    new_path = path + [name]
                    res.append(new_path)

                    collect(child, new_path)
        collect(root, [])
        return res