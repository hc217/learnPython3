list1 =  [91, 95, 97, 99]
list2 =  [92, 93, 96, 98]
# list3 = list1+list2
# list3.sort()
list1.append(list2[0])
list1.append(list2[1])
list1.append(list2[2])
list1.append(list2[3])
list1.sort()
#print(list1)

def my_len(words):
    i = 0
    for i in words[:]:
        print(i)

print(my_len('三根皮带，四斤大豆'))