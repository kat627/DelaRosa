class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hi! I'm {self.name}, {self.age} years old, studying {self.course}.")

student1 = Student("David", 19, "Biology")
student2 = Student("Emma", 21, "History")
student3 = Student("Liam", 20, "Engineering")

student1.introduce()
student2.introduce()
student3.introduce()
