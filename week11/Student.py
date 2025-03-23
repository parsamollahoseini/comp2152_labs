from Person import Person

class Student(Person):
    def __init__(self, name, age, height, major):
        # Call parent constructor
        super().__init__(name, age, height)
        self.major = major
        print("This time it's a Student object")

# Creating an instance of Student
if __name__ == "__main__":
    student = Student("Maria", 22, 6, "Computer Science")
    print(f"Major: {student.major}")
    print(f"Public property from Person: {student.public_prop}")