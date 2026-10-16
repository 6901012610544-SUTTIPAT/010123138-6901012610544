'''
====================================================
|                                                  |
|                   Inheritance                    |
|                                                  |
====================================================
'''


class Student:
    def __init__(self, name, age):
        self.name: str = name
        self.age: int = age

    def show_info(self):
        print(f"Name: {self.name}\nAge: {str(self.age)}")


class BodinTwo(Student):
    def __init__(self, name, age, program, id):
        super().__init__(name, age)
        self.program: str = program
        self.id: str = id

    def stud_info(self):
        self.show_info()
        print(f"{self.name} ID {self.id} studies {self.program} program")

if __name__ == "__main__":
    s1 = BodinTwo("Suttipat", 18, "IEP Math-Sci", "22629")
    s1.stud_info()