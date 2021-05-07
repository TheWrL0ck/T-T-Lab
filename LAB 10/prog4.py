class Vehicle:
  def __init__(self,brand,speed,wheels):
    self.brand = brand
    self.wheels = wheels
    self.speed = speed
  def countWheels(self):
    if self.brand == "Scooty" and self.wheels == 2 and self.speed <= 50.0:
        print("Two Wheeler")
        return
    if self.brand == "Car" and self.wheels == 4 and self.speed > 50.0 and self.speed <= 90.0:
        print("Four Wheeler")
        return
    if self.brand == "Train" and self.wheels == 14 and self.speed > 90.0:
        print("Forteen Wheeler")
        return
    else:
        print("Invalid Input")
s1 = Vehicle("Scooty", 30.0, 2)
s2 = Vehicle("Car", 57.0, 4)
s3 = Vehicle("Train", 120.0, 14)
s1.countWheels()
s2.countWheels()
s3.countWheels()