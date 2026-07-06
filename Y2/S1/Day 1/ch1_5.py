"""
Create a simulation of a Vickrey auction. A Vickrey auction is a type of auction where the winner is the person who submits the highest bid
, but the actual price paid is the second-highest bid.

Display output as examples.

word
"Enter All Bid : "
"not enough bidder"
"error : have more than one highest bid"
"winner bid is $ need to pay $"

Enter All Bid : 5 10 20 5 16
winner bid is 20 need to pay 16

"""

bids = [int(e) for e in input("Enter All Bid : ").split()]

if len(bids) < 2:
    print("not enough bidder")
    raise SystemExit

for i in range(len(bids)-1):
    for j in range(len(bids)-i-1):
        if bids[j] > bids[j+1]:
            bids[j], bids[j+1] = bids[j+1], bids[j]

if bids[len(bids)-1] == bids[len(bids)-2]:
    print("error : have more than one highest bid")
    raise SystemExit
else:
    print(f"winner bid is {bids[len(bids)-1]} need to pay {bids[len(bids)-2]}")