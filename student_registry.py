class Student():
    def __init__(self, name, age=13, grade="12th"):
        self.name = name
        self.age = age
        self.grade = grade
    
    @property
    def get_name(self):
        return self.name
    @property
    def get_age(self):
        return self.age
    @property
    def get_grade(self):
        return self.grade
    
    @get_name.setter
    def set_name(self, new_name):
        self.name = new_name
        # print(f'{self.name} == {new_name}')

    @get_age.setter
    def set_age(self,new_age):
        self.age = new_age

    @get_grade.setter
    def set_grade(self, new_grade):
         self.grade = new_grade

if __name__ == "__main__":
        student = Student("Alice")
        student = Student("Alex")
        print(student.get_name)
        print(student.get_age)
        print(student.get_grade)


alice = Student("alice", 13, "12th")
# francisco = Student("Francisco", 13, "12th")
# James = Student("James", 12, "11th" )

# francisco.student()
# James.student()