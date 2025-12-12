shopping_dict = {
    "egg": 1,
    "ham": 1,
    "water": 1,
    "soda": 1,
}
print("*** Shopping List 2 ***")
failedToBuy = False
commandInput = input("Enter some pairs of (operation, item): ").lower().split(",")
for command in commandInput:
    operation, item = command.split()
    if operation == "a":
        if item in shopping_dict:
            shopping_dict[item] += 1
        else:
            shopping_dict[item] = 1
    elif operation == "r":
        if item in shopping_dict:
            if shopping_dict[item] > 0:
                shopping_dict[item] -= 1
                if(shopping_dict[item] == 0):
                    shopping_dict.pop(item)
            else:
                # failedToBuy = True
                # break
                continue
        else:
            # failedToBuy = True
            # break
            continue

    else:
        print(f"Operation not supported!")
        failedToBuy = True
        break
if(not failedToBuy):
    print("Final shopping dict is",shopping_dict)