class student:
    def __init__(self, name, Student_id, dept):
        self.name = name
        self.student_id = Student_id
        self.dept = dept
        
    def display_info(self):
        print("Student Name:", self.name)
        print("Student ID:", self.student_id)
        print("department:", self.dept)
        

s1 = student("Shrestha Biswas", 195, "Match")

s1.display_info()