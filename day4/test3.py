class Unit:
    count = 0
    
    def __init__(self, name):
        Unit.count = Unit.count + 1
        self.name = name

    def move(self):
        print("move")

    def speak(self):
        print("앙 기모띠!")

class Dron(Unit):
    def speak(self):
        print("!!!!")

class Hydra(Unit):
    def speak(self):
        print("붹붹")



d1 = Dron("드론1")
d2 = Dron("드론2")
h1 = Hydra("히드라1")
h2 = Hydra("히드라2")

d1.move()
d1.speak()
h2.move()
h2.speak()

print("현재인구수 : %d" % (Unit.count))
