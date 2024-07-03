class Car:
    def start(self):
        print("this car have started")
        return self
    def drive(self):
        print("Drive this car")
        return self
    def breaks(self):
        print("Apply brakes to stop")
        return self
    def poweroff(self):
        print("Turn this car of")
        return self


car=Car()
car.start()\
    .drive()\
    .breaks()\
    .poweroff()
        