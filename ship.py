class SpaceShip:
    Fuel = 400
    Passengers = ["John", "Steve", "Sam", "Danielle"]
    Shields = True
    Speedometer = 0

    def list_passengers(self):
        for passenger in self.Passengers:
            print(f"Passenger: {passenger}")

    def add_passenger(self, new_passenger):
        self.Passengers.append(new_passenger)
        print(f"{new_passenger} was added to the ship")

    def travel(self, distance):
        print(f"trying to travel: {distance}")
        if self.Fuel == 0:
            return print("can't go further, tank is empty")
        self.Fuel = self.Fuel - (distance / 2)
        if self.Fuel < 0:
            distance = distance - (self.Fuel * -2)
            print(f"can only travel: {distance}")
            self.Fuel = 0
        self.Speedometer += distance
        if self.Fuel < 30 and self.Fuel != 0:
            self.Shields = False
            print("fuel is low, turning off shields...")
        print(f"the Spaceship is at: {self.Speedometer}")
        print(f"the spaceship has: {self.Fuel} fuel")


mySpaceShip = SpaceShip()

mySpaceShip.list_passengers()
mySpaceShip.add_passenger('Lindsay')
mySpaceShip.list_passengers()
mySpaceShip.travel(750)
mySpaceShip.travel(200)
mySpaceShip.travel(100)