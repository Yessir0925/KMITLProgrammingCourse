print(" *** Creating Dictionary ***")
datas = input("Enter text : ").split()
curr_indx = 0
my_dict = {}
key =""
val = 0
for data in datas:
    if(curr_indx % 2 == 0):
        key = data
    else:
        val = int(data)
        if(key in my_dict):
            my_dict[key] += val
        else:
            my_dict[key] = val
    curr_indx += 1
print(my_dict)
print("===== End of program =====")