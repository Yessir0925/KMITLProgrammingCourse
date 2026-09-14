l = list(map(int, input("Enter Input : ").split()))

step = 0
for last in range(len(l) - 1, 0, -1):
    step += 1
    move = None
    for j in range(last):
        if l[j] > l[j + 1]:
            move = l[j]
            l[j], l[j + 1] = l[j + 1], l[j]
    if move is None or last == 1:
        print(f"last step : {l} move[{move}]")
        break
    print(f"{step} step : {l} move[{move}]")
else:
    print(f"last step : {l} move[None]")
