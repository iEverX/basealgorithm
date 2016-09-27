class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def makeTree(ns):

    def wrap(x):
        return TreeNode(x) if x else None

    nodes = [wrap(x) for x in ns]
    i, j, n = 0, 1, len(ns)
    while j < n:
        if nodes[i]:
            nodes[i].left = nodes[j]
            j += 1
            if j < n:
                nodes[i].right = nodes[j]
                j += 1
        i += 1
    return nodes[0]


def preorder(root):
    if not root:
        return None
    stack, current = [], root
    while True:
        if current:
            yield current.val
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop().right
        else:
            break


def r_preorder(root):
    if root:
        yield root.val
        yield from r_preorder(root.left)
        yield from r_preorder(root.right)


def inorder(root):
    stack, current = [], root
    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            yield current.val
            current = current.right
        else:
            break

def r_inorder(root):
    if root:
        yield from r_inorder(root.left)
        yield root.val
        yield from r_inorder(root.right)


def postorder(root):
    stack, visit, current, go_to_right = [], [], root, True
    while True:
        if current and go_to_right:
            stack.append(current)
            visit.append(True)
            current = current.left
        elif stack:
            go_to_right = visit[-1]
            if go_to_right:
                current = stack[-1].right
                visit[-1] = False
            else:
                current = stack.pop()
                visit.pop()
                yield current.val
        else:
            break


def r_postorder(root):
    if root:
        yield from r_postorder(root.left)
        yield from r_postorder(root.right)
        yield root.val


if __name__ == '__main__':

    def equal(g1, g2):
        v1 = list(g1)
        v2 = list(g2)
        print(v1)
        print(v2)
        assert v1 == v2

    def test(ns):
        t = makeTree(ns)
        equal(preorder(t), r_preorder(t))
        equal(inorder(t), r_inorder(t))
        equal(postorder(t), r_postorder(t))

    test([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    test([1, 2, None, 3, 4, None, 5, None, None, 6, 7, 8, None, 9, 10, None, 11, 12, None, None, None, 13])