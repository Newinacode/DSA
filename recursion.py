# understanding recursion

# finding element in a tree


class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None


root = Node(20)
root.right = Node(20)
root.right.right = Node(100)
root.right.left = Node(15)


def findElement(root,val):
    if not root:
        return None
    
    if root.val == val:
        return True
    
    return findElement(root.right,val) or findElement(root.left,val)


print(findElement(root,200))
        