class Student:
    def __init__(self, id, name, course, age):
        self.student_id: str = id
        self.name: str = name
        self.course: str = course
        self.age: int = age

    def show(self):
        print(f"{self.student_id} {self.name}, age {str(self.age)}. Is enrolled in {self.course}.")

def show_youngest(student_array):
    if not student_array:
        print("No data")
        return

    youngest_student = student_array[0]
    for student in student_array:
        if student.age < youngest_student.age:
            youngest_student = student

    youngest_student.show()

def main():
    student_list = []
    file_name: str = "data.txt"

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for lines in file:
                data = lines.strip().split(", ")

                if len(data) == 4:
                    stud_id, name, course, age = data
                    student = Student(stud_id, name, course, age)
                    student_list.append(student)
    except:
        print("File not found.")

    print("----Youngest Student----")
    show_youngest(student_list)


if __name__ == "__main__":
    main()