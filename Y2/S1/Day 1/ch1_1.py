"""
*** Rabbit & Turtle ***
Enter Input : 10 1 2 300
3000.00
"""

"""the hare is running ahead of the tortoise by a distance of d meters. 
The hare travels at a constant speed Vr meters per second, while the 
tortoise travels at a constant speed Vt meters per second. In this story, 
the tortoise is always faster than the hare. A fly is perched on the tortoise's 
head, flying at a constant speed Vf meters per second. When the fly reaches the 
hare, it flies back to the tortoise at the same speed. The fly will continue 
flying back and forth between the hare and the tortoise until the tortoise 
catches up to the hare (the tortoise must catch up because it is traveling 
at a faster speed than the hare). """

#d, Vr, Vt, and Vf
distance = None
print(f"*** Rabbit & Turtle ***")

try:
    
    d, Vr, Vt, Vf = input("Enter Input : ").split()
    d = int(d)
    Vr = int(Vr)
    Vt = int(Vt)
    Vf = int(Vf)

    if d < 5000 and Vr < 5000 and Vt < 5000 and Vf < 5000 and Vt > Vr:
        distance = d * Vf / (Vt - Vr)
        print("{:.2f}".format(distance))
    else:
        raise ValueError()

except:
    print("Invalid Input")
    raise SystemExit