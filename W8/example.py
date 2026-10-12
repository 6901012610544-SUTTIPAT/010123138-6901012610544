class Car:

  def __init__(self, brand, color):  #Constructor
    self.__brand = brand  #Attribute
    self.color = color

  def drive(self):  #Method
    print(f"รถ {self.__brand} สี {self.color} กำลังแล่น...")


#สร้าง Object
car1 = Car("Toyota", "แดง")
car1.drive()