
class Car:

    def __init__(self, year_model, rttake, speed=0):
        self.year_model = year_model
        self.rttake = rttake
        self.speed = speed

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def get_speed(self):
        print(self.speed)

car = Car(2000, 'Tesla', 0)
car.accelerate()
car.get_speed()
car.accelerate()
car.get_speed()
car.accelerate()
car.get_speed()
car.accelerate()
car.get_speed()
car.accelerate()
car.get_speed()
car.brake()
car.get_speed()
car.brake()
car.get_speed()
car.brake()
car.get_speed()
car.brake()
car.get_speed()
car.brake()
car.get_speed()