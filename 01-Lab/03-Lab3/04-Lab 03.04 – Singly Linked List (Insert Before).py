"""Lab 03.04 – Singly Linked List (Insert Before)"""
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

    def insert_front(self, data) :
        """insert_front"""
        new_node = DataNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.count += 1

    def insert_before(self, node, data) :
        """insert_before"""
        if self.head is None:
            print(f"Cannot insert, " + node + " does not exist.")
            return
        if self.head.data == node:
            self.insert_front(data)
            return
        current = self.head
        while current.next and current.next.data != node:
            current = current.next
        if current.next is None:
            print(f"Cannot insert, " + node + " does not exist.")
        else:
            new_node = DataNode(data)
            new_node.next = current.next
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

def main():
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        text = input()
        condition, data = text.split(": ")
        if condition == "F":
            mylist.insert_front(data)
        elif condition == "L":
            mylist.insert_last(data)
        elif condition == "B":
            mylist.insert_before(*data.split(", "))
            # elif condition == "D":
            #    mylist.delete(data)
        else:
            print("Invalid Condition!")
    mylist.traverse()
main()
