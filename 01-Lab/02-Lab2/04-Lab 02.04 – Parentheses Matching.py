class ArrayStack :
    def __init__(self):
        self.size = 0
        self.data = list()

    def push(self, input_data):
        """push"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1

    def get_stack_top(self):
        """get_stack_top"""
        if self.get_size() != 0 :
            tmp_data = self.pop()
            self.data.append(tmp_data)
            return tmp_data
        else :
            print("Underflow: Cannot get stack top from an empty list")
            return None

    def pop(self):
        """pop"""
        if self.get_size() != 0 :
            pop_data = self.data.pop()
            self.size -= 1
            return pop_data
        else :
            print("Underflow: Cannot pop data from an empty list")
            return None
    
    def get_size(self):
        """get_size"""
        return self.size
    
    def is_empty(self):
        """is_empty"""
        return True if self.get_size() == 0 else False
    
    def print_stack(self):
        """print_stack"""
        print(self.data)

def main() :
    """main"""
    expression = input()
    result = is_parentheses_matching(expression)
    if result :
        print("Parentheses in", expression, "are matched")
        print(result)
    else :
        print("Parentheses in", expression, "are unmatched")
        print(result)

def is_parentheses_matching(expression) :
    """is_parentheses_matching()"""
    stack = ArrayStack()
    result = True
    for ex in expression :
        if ex == "(" :
            stack.push(ex)
        elif ex == ")" :
            tmp = stack.pop()
            if tmp == None :
                result = False
    return result and stack.is_empty()
main()
