# yliluokka

class Car:
    def __init__(self, register_number, max_speed):
        self.register_number = register_number
        self.odometer = 0
        self.speed = 0
        self.max_speed = max_speed

    def print_info(self):
        print(f"Auton rekisteri: {self.register_number} matkamittari: {self.odometer}")

    def drive(self, trip_change):
        self.odometer = self.odometer + trip_change * self.speed

    def accelerate(self, speed_change):
        self.speed = speed_change + self.speed
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < 0:
            self.speed = 0

# aliluokka

class Sähköauto(Car):
    def __init__(self, register_number, max_speed, akkukapasiteetti):
        super().__init__(register_number, max_speed)
        self.akkukapasiteetti = akkukapasiteetti

# aliluokka

class Polttomoottoriauto(Car):
    def __init__(self, register_number, max_speed, bansatankin_koko):
        super().__init__(register_number, max_speed)
        self.bensatankin_koko = bansatankin_koko

# pääohjelma

s = Sähköauto("ABC-15", 180, 52.5)
p = Polttomoottoriauto("ACD-123", 165, 32.3)
s.accelerate(25)
p.accelerate(50)
s.drive(3)
p.drive(3)
s.print_info()
p.print_info()