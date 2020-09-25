

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def numberOfBSTs(root):

    if not root:
        return (-float('inf'), float('inf'), 0, False)
    if root and not root.left and not root.right:
        return (root.val, root.val, 1, True)

    left_min, left_max, left_count, left_is_bst = numberOfBSTs(root.left)
    right_min, right_max, right_count, right_is_bst = numberOfBSTs(root.right)

    new_min = max(root.val, left_min, right_min)
    new_max = min(root.val, left_max, right_max)

    if left_is_bst and right_is_bst and left_max < root.val < right_min:
        return (new_min, new_max, left_count + right_count + 1, True)
    else:
        return (new_min, new_max, left_count + right_count, False)



if __name__ == '__main__':

    node = Node(15, Node(10, Node(8), Node(12)), Node(10, Node(17), Node(25)))
    ans = numberOfBSTs(node)
    print(ans)