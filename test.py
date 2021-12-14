print('Hello World!')

power = [i*i for i in range(1, 21)]
# print(power)

for i in [1, 2, 3, 4, 5]:
    print(i)
    if i == 3:
        break
    else:
        print("only executed when no item of the list is equal to 3")