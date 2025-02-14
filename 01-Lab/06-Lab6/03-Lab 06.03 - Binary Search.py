"""Lab 06.03 - Binary Search"""
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

def binary_search(data, target):
    begin, end = 0, len(data) - 1
    comparisons = 0

    while begin <= end:
        mid = (begin + end) // 2
        comparisons += 1
        if target > data[mid].get_name() :
            begin = mid + 1
        elif target < data[mid].get_name():
            end = mid - 1
        else :
            begin = end + 1

        if data[mid].get_name() == target:
            print(f"Found {target} at index {mid}")
            data[mid].print_details()
            print(f"Comparisons times: {comparisons}")
            return
    print(f"{target} does not exists.")
    print(f"Comparisons times: {comparisons}")


def main():
    import json
    std_in = json.loads(input())
    std = [Student(v["id"], v["name"], v["gpa"]) for v in std_in]
    binary_search(std, input())

main()
    

