"""Lab 03.02 – Singly Linked List (Traversal and Insert Last)"""
class DataNode:
    def __init__(self, data=None) :
        self.data = data
        self.next = None

class SinglyLinkedList :
    def __init__(self) :
        self.count = 0
        self.head = None
    
    def insert_last(self, data) :
        """insert_data"""
        new_node = DataNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.count += 1

    def traverse(self) :
        """traverse"""
        if self.head is None:
            print("This is an empty list.")
        else :
            current = self.head
            while current:
                print(current.data, end=" -> " if current.next else "\n")
                current = current.next

def main() :
    """main"""
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        mylist.insert_last(input())
    mylist.traverse()
main()
