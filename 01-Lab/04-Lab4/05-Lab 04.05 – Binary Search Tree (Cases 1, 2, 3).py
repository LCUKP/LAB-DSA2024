"""Lab 04.05 – Binary Search Tree (Cases 1, 2, 3)"""
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

    def find_min(self) :
        """find_min"""
        if self.is_empty() :
            return None
        node = self.root
        while node.left :
            node = node.left
        return node.data

    def find_max(self) :
        """find_max"""
        if self.is_empty() :
            return None
        node = self.root
        while node.right :
            node = node.right
        return node.data
    
    def delete(self, data: int):
        """delete"""
        self.root = self._delete_recursive(self.root, data)

    def _delete_recursive(self, node: BSTNode, data: int):
        """_delete_recursive"""
        if node is None:
            print("Delete Error, "+str(data)+" is not found in Binary Search Tree.")
            return None

        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else:

            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
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
