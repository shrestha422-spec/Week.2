class student:
    def __init__(self, name, student_id, dept):
        self.name = name
        self.student_id = student_id
        self.dept = dept
        
    def display_info(self):
        print("student name:", self.name)
        print("student ID:", self.student_id)
        print("department:", self.dept)
        
        
s1 = student("Shrestha", 101, "English")

s1.display_info()