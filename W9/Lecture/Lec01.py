class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, " + self.name)



if __name__ == '__main__':
    Auddy = Person("Auddy", 18)
    Auddy.greet()