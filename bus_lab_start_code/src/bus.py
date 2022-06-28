class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passenger = []


    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passenger)

    def pick_up(self, people):
        self.passenger.append(people)

    def drop_off(self, people):
        self.passenger.remove(people)

    def empty(self):
        self.passenger = []

    def pick_up_from_stop(self, bus_stop):
        for people in bus_stop.queue:
            self.pick_up(people)
