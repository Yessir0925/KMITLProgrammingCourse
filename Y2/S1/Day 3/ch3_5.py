"""  Mr. A's parking area is shaded in blue, while the red area belongs '
  'to Mr. B, who is a relative. Both Mr. A's and Mr. B's parking areas '
  'are very narrow and can only accommodate cars in a single line. Mr. '
  'B does not use his parking space but allows Mr. A to use it without '
  'parking his car there permanently. Due to the narrow alley, parking '
  '(arrive) and retrieving cars (depart) will operate as a stack. The '
  'condition is that when retrieving any car x, the order of the cars '
  'should remain the same, as shown in the diagram simulating the parking '
  'of cars in Mr. A's parking space using stack operations. Below is an 
example output.

Input: Receive 4 values in one line separated by a space (" "). The 
first position is the maximum number of cars that can park in Mr. A's '
'alley, the second position is the car currently parked in Mr. A's alley, 
the third position is the action (e.g., if it is "arrive", it will add a 
                                  car to the alley, and if it is "depart", 
                                  it will remove a car from the alley), and 
the fourth position is the number of the car to be added or removed.

Note: If there are no cars in the alley, set the input to 0 in the second position.

******** Parking Lot ********
Enter max of car / car in soi / operation : 5 / 1,2,3,4 / arrive 5
car 5 arrive! : Add Car 5
[1, 2, 3, 4, 5]

******** Parking Lot ********
Enter max of car / car in soi / operation : 5 / 1,2,3,4 / arrive 1
car 1 already in soi
[1, 2, 3, 4]


"""

print("******** Parking Lot ********")
usrinp = input("Enter max of car / car in soi / operation : ")
max_car, car_in_soi, operation = usrinp.split(' / ')
cars = [int(x) for x in car_in_soi.split(',')]

class ParkingLot:
    def __init__(self, max_car, cars):
        self.max_car = max_car
        self.cars = [y for y in cars]

    def arrive(self, car_number):
        if len(self.cars) < self.max_car:
            if car_number in self.cars:
              print(f"car {car_number} already in soi")
            else:
              self.cars.append(car_number)
              print(f"car {car_number} arrive! : Add Car {car_number}")
        else:
            print(f"car {car_number} cannot arrive : Soi Full")

    def depart(self, car_number):
        if car_number in self.cars:
            self.cars.remove(car_number)
            print(f"car {car_number} depart ! : Car {car_number} was remove")
        else:
            print(f"car {car_number} cannot depart : Dont Have Car {car_number}")

    def __str__(self):
        return str(self.cars)

parking_lot = ParkingLot(int(max_car), cars)
operation = operation.split(' ')
if operation[0] == 'arrive':
    parking_lot.arrive(int(operation[1]))
elif operation[0] == 'depart':
    parking_lot.depart(int(operation[1]))

print(parking_lot)