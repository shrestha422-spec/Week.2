class student:
    def __init__(self, name, student_id, dept):
        self.name = name
        self.student_id = student_id
        self.dept = dept
    def display_info(self):
        print("Student Name:", self.name)
        print("Student ID:", self.student_id)
        print("department:", self.dept)
        
        
s1 = student("Souvik", 56, "English")

s1.display_info()