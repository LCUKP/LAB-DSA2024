"""Lab 04.02 - Binary Search Tree (Preorder, Insert)"""
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
            
    def preorder(self):
        """preorder"""
        self._preorder_recursive(self.root)
    
    def _preorder_recursive(self, node: BSTNode):
        if node is not None:
            print(" -> "+str(node.data), end="")
            self._preorder_recursive(node.left)
            self._preorder_recursive(node.right)

def main():
    """main"""
    my_bst = BST()
    for i in range(int(input())):
        my_bst.insert(int(input()))
        
    print("Preorder:", end="")
    my_bst.preorder()

main()
