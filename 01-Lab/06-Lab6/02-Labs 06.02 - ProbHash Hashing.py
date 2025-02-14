"""Labs 06.02 - ProbHash Hashing"""
class Student :
    def __init__(self, std_id, name, gpa):
        self.__std_id = std_id
        self.__name = name
        self.__gpa = gpa

    def Student(self, std_id, name, gpa):
        self.__std_id = std_id
        self.__name = name
        self.__gpa = gpa

    def get_std_id(self) :
        return self.__std_id
    
    def get_name(self) :
        return self.__name
    
    def get_gpa(self) :
        return self.__gpa
    
    def print_details(self) :
        print(f"ID: {self.get_std_id()}\nName: {self.get_name()}\nGPA: {self.get_gpa():.2f}")

class ProbHash :
    def __init__(self, size : int):
        self.__size = size
        self.__hash_table = [None for _ in range(self.__size)]

    def hash(self, key) :
        h = key % self.__size
        return h
    
    def rehash(self, key) :
        if key < self.__size :
            key += 1
            if key >= self.__size :
                key = 0
        elif key >= self.__size :
            key = 0
        return key
        
    def insert_data(self, std : Student) :
        if None not in self.__hash_table :
            print(f"The list is full. {std.get_std_id()} could not be inserted.")
            return
        index = self.hash(int(std.get_std_id()))
        while self.__hash_table[index] is not None :
            index = self.rehash(index)
        self.__hash_table[index] = std
        print(f"Insert {std.get_std_id()} at index {index}")
    
    def search_data(self, std_id : int) :
        for i,v in enumerate(self.__hash_table) :
            if v is not None and v.get_std_id() == std_id:
                print(f"Found {v.get_std_id()} at index {i}")
                return v
        print(f"{std_id} does not exist.")

def main():
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_details()
            print("------")
        else:
            print("Invalid Condition!")
main()
