"""Lab 04.03 – Binary Search Tree (Traversals)"""
class BSTNode :
    def __init__(self, data: int=None):
        self.data = data
        self.left = None
        self.right = None

class BST :
    def __init__(self):
        self.root = None

    def insert(self, data) :
        """insert"""
        new_node = BSTNode(data)
        if self.root is None :
            self.root = new_node
        else :
            current = self.root
            while True :
                if data < current.data :
                    if current.left is None :
                        current.left = new_node
                        break
                    else :
                        current = current.left
                else :
                    if current.right is None :
                        current.right = new_node
                        break
                    else :
                        current = current.right
    
    def is_empty(self):
        """is_empty"""
        return self.root is None

    def preorder(self):
        """preorder"""
        print("Preorder:",end="")
        self._preorder_recursive(self.root)
        print()
    
    def _preorder_recursive(self, node: BSTNode):
        """_preorder_recursive"""
        if node is not None:
            print(" -> "+str(node.data), end="")
            self._preorder_recursive(node.left)
            self._preorder_recursive(node.right)
    
    def inorder(self):
        """inorder"""
        print("Inorder:",end="")
        self._inorder_recursive(self.root)
        print()

    def _inorder_recursive(self, node: BSTNode):
        """_inorder_recursive"""
        if node is not None:
            self._inorder_recursive(node.left)
            print(" -> "+str(node.data), end="")
            self._inorder_recursive(node.right)

    def postorder(self):
        """postorder"""
        print("Postorder:",end="")
        self._postorder_recursive(self.root)
        print()

    def _postorder_recursive(self, node: BSTNode):
        """_postorder_recursive"""
        if node is not None:
            self._postorder_recursive(node.left)
            self._postorder_recursive(node.right)
            print(" -> "+str(node.data), end="")

    def traverse(self):
        """traverse"""
        if self.is_empty():
            print("This is an empty binary search tree.")
        else:
            self.preorder()
            self.inorder()
            self.postorder()

def main():
    """main"""
    my_bst = BST()
    for i in range(int(input())):
        my_bst.insert(int(input()))
    my_bst.traverse()

main()
