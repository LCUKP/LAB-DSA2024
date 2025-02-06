"""Lab 04.06 – Binary Search Tree (Delete All Cases)"""
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

    def find_min(self, node: BSTNode) :
        """find_min"""
        current = node
        while current.left:
            current = current.left
        return current
    
    def find_max(self, node: BSTNode):
        """find_max"""
        current = node
        while current.right:
            current = current.right
        return current
    
    def delete(self, data: int):
        """delete"""
        self.root = self._delete_recursive(self.root, data)

    def _delete_recursive(self, node: BSTNode, data: int):
        """_delete_recursive"""
        if node is None:
            print("Delete Error, " + data + " is not found in Binary Search Tree...")
            return None

        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            max_in_left = self.find_max(node.left)
            node.data = max_in_left.data
            node.left = self._delete_recursive(node.left,node.data)
        return node

def main():
    my_bst = BST()
    while 1:
        text = input()
        if text == "Done":
            break
        condition, data = text.split(": ")
        if condition == "I":
            my_bst.insert(int(data))
        elif condition == "D":
            my_bst.delete(int(data))
        else:
            print("Invalid Condition")
    my_bst.traverse()

main()