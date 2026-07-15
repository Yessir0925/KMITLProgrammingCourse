"""PSD48 (P-Saderd 48 Group) is a currently popular idol group, with their hit song "Jee Hoi" (Clam). PSD48 is 
about to hold a handshake event, and the rule is that if someone in line is from the Survey Corps, they will
have priority and can go to the front of the line immediately (but if the person at the front is also from
the Survey Corps, they will have to queue behind them). PSD48 wants you to write a program to 
find out which Ota IDs will get to participate in the handshake event.

Soundtrack: https://youtu.be/Jd4Hd-HFgls

Input :
EN <value> is just an ordinary otaku. id = value
ES <value> is an otaku of the Survey Corps. id = value
D is a command to display the value of the row leader. If there is no one in the row, it will display "Empty". 

Enter Input : EN 1,EN 2,D,D,D,EN 3,D
1
2
Empty
3
"""

usrinp = input("Enter Input : ")
usrlist = [x.strip() for x in usrinp.split(',')]
UserQueue = []
Output = []

for step in usrlist:
    if step == 'D':
        if UserQueue:
            Output.append(UserQueue.pop(0))
            continue
        else:
            Output.append("Empty")

    else:
        stepsplit = step.split(' ')
        if stepsplit[0] == 'EN':
            UserQueue.append(stepsplit[1])
        elif stepsplit[0] == 'ES':
            UserQueue = [stepsplit[1]] + UserQueue

for p in Output:
    print(p)