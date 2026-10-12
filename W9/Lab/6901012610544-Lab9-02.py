#====================================================
#                                                   |
#        6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ        |
#                                                  |
#====================================================

class Person:
    def __init__(self, name, address, weight, height):
        self.name: str = name
        self.address: str = address
        self.weight: float = weight
        self.height: float = height

    def show(self):
        print(f"Name: {self.name}\nAddress: {self.address}\nWeight: {self.weight}\nHeight: {self.height}")

    def getBMI(self):
        return f"BMI: {self.weight / ((self.height / 100)**2):.2f}"

class Student(Person):
    def __init__(self, name, address, weight, height, student_id, course, gpa):
        super().__init__(name, address, weight, height)
        self.student_id: str = student_id
        self.course: str = course
        self.gpa: float = gpa

    def show(self):
        super().show()
        print(f"Student ID: {self.student_id}\nCourse enroll: {self.course}\nGPA: {self.gpa}")

class Employee(Person):
    def __init__(self, name, address, weight, height, employee_id, department, salary):
        super().__init__(name, address, weight, height)
        self.employee_id: str = employee_id
        self.department: str = department
        self.salary: float = salary

    def show(self):
        super().show()
        print(f"Employee ID: {self.employee_id}\nDepartment: {self.department}\nSalary: {self.salary}")

if __name__ == "__main__":
    person1 = Person("Suttipat Euaphattanakit", "Phraya suren Rd.", 78.7, 175)
    student1 = Student("Chanasin Na nakorn", "Liab Khlong song Rd.", 76.0, 178, "6901012610544", "Pre-cadet Academy", 3.96)
    employee1 = Employee("Anonymous", "Ramkamhaeng Rd.", 80, 177, "22629", "Public Relations", 23_500)

    person1.show()
    print(student1.getBMI())

    print("="*45)

    student1.show()
    print(student1.getBMI())

    print("="*45)

    employee1.show()
    print(employee1.getBMI())