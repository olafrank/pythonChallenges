class Flight():
    def __init__(self,capacity):
        self.capacity=capacity
        self.passenger=[]

    def add_passenger(self,name):
        if not self.open_seat():
            return False
        self.passenger.append(name)
        return True

    def open_seat(self):
        return self.capacity-len(self.passenger)

flight=Flight(3)      

people=["harry","victor","james","dinebari"]
for person in people:
    success=flight.add_passenger(person)
    if success:
        print(f'you added {person} successfully')
    else:
        print(f'No available space for {person}')    