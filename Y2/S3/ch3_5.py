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
"""
