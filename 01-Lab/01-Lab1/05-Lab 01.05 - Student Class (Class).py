"""Lab 01.05 - Student Class (Class)"""
def main() :
    class Studens :
        def __init__(self, name, sex, age, code, gpa):
            self.name = name
            self.sex = sex
            self.age = age
            self.code = code
            self.gpa = gpa
    stds = [Studens(input(), input(), input(), input(), float(input())) for _ in range(3)]
    id = input()
    for std in stds :
        if std.code == id :
            print("Mr" if std.sex == "Male" else "Miss", end=" ")
            print(f"{std.name} ({std.age}) ID: {std.code} GPA {std.gpa:.2f}")
            return
    print("Student not found")
main()