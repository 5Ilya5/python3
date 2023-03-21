ints_list = [1, 2, 3, 4, 5, 5, 3, 2, 6, 7, 7, 8, 9]

temp = []

for x in ints_list:
    if x not in temp:
        temp.append(x)

ints_lsit = temp
print (f'обновленный список после удаления дубликатов = {temp}')