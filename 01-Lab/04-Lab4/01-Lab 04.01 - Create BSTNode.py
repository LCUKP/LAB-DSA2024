"""Lab 04.01 - Create BSTNode"""
class BSTNode :
    def __init__(self, data: int=None):
        self.data = data
        self.left = None
        self.right = None

def main() :
    """main"""
    BST = BSTNode(int(input()))
    print(BST.data)
    print(BST.left)
    print(BST.right)
main()
