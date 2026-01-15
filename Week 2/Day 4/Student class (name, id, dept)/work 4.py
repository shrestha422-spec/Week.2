class Student:
    def __init__(self, name, student_id, depf):
        self.name = name
        self.student_id = student_id
        self.depf = depf
    def display_info(self):
        print("Student Name;", self.name)
        print("Student ID:", self.student_id)
        print("department:", self.depf)
        
        
s1 = Student("Alex Biswas", 50, "English")

s1.display_info()