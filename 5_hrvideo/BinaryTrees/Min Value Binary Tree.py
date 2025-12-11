def max_min_value_binary_tree(root):
    if root is None:
        return None, None

    def traverse(node):
        if node is None:
            return float('inf'), float('-inf')

        left_min, left_max = traverse(node.left)
        right_min, right_max = traverse(node.right)

        current_min = min(node.value, left_min, right_min)
        current_max = max(node.value, left_max, right_max)

        return current_min, current_max

    return traverse(root)