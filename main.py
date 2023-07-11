class Vehicle():
    def start(self):
        print("Vehicle Started")

    def stop(self):
        print("Vehicle stopped")

class car(Vehicle):
    def start(self):
        print("Car Started")

    def stop(self):
        print("Car Stopped")

class Motocycle(Vehicle):
    def start(self):
        print("Motocycle Started")

    def stop(self):
        print("Motocycle Stopped")

Tvs=Motocycle()
Tvs.start()
Tvs.stop()
Tata=car()
Tata.start()
Tata.stop()
