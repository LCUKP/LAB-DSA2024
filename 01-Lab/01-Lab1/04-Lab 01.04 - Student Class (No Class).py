"""Lab 01.04 - Student Class (No Class)"""
def std() :
    """Lab 01.04 - Student Class (No Class)"""
    stds = []
    for i in range(3) :
        my_list = [input(), input(), input(), input(), input()]
        stds.append(my_list)
    code = input()
    tmp = 1
    for i in stds :
        if i[3] == code :
            print("Mr" if i[1] == "Male" else "Miss", end=" ")
            print(f"{i[0]} ({i[2]}) ID: {i[3]} GPA {float(i[4]):.2f}")
            tmp = 0
    if tmp :
        print("Student not found")
std()
