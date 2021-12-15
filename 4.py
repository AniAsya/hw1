class Car:
    def __init__(self, speed, colour, name, is_police=False):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police

    def go(self):
        print("GO!")

    def stop(self):
        print("STOP!")

    def turn(self, direction):
        print(f"Car turned to {direction}")

    def show_speed(self):
        print(f"Current speed is {self.speed}")

class Towncar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Speed limit violated!")

class Sportcar(Car):
    pass

class Workcar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Speed limit violated!")

class Policecar(Car):
    def __init__(self, speed, colour, name):
        super().__init__(speed, colour, name, True)

town = Towncar(90, "yellow", "Town")
sport = Sportcar(120, "green", "Sport")
work = Workcar(41, "red", "Work")
police = Policecar(100, "black", "Police")

town.show_speed()
work.show_speed()

work.speed = 30
work.show_speed()

police.turn("Left")
