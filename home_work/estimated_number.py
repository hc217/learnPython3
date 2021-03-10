import math
# 人力计算
# def estimated_number(size,time):
#     number = size * 80 / time
#     if number > 1:
#         print('项目大小为%.1f个标准项目，如果需要在%.1f个工时完成，则需要人力数量为：%d人' %(size,time,number+1))
#     else:
#         print('项目大小为%.1f个标准项目，如果需要在%.1f个工时完成，则需要人力数量为：%d人' %(size,time,number))
#
# # 调用人力计算函数
# estimated_number(1,60)

# def estimated(size=1,number=None,time=None):
#     if (number == None) and (time != None):
#         number = math.ceil(size * 80 / time)
#         print('项目大小为%.1f个标准项目，如果需要在%.1f个工时完成，则需要人力数量为：%d人' %(size,time,number))
#     elif (number != None) and (time == None):
#         time = size * 80 / number
#         print('项目大小为%.1f个标准项目，使用%d个人力完成，则需要工时数量为：%.1f个' %(size,number,time))
#
# def choice():
#     types = int(input('请选择计算类型：（1-人力计算，2-工时计算）'))
#     if types == 1:
#         input1 = float(input('请输入项目大小：（1代表标准大小，可以输入小数）'))
#         input2 = float(input('请输入工时数量：（请输入小数）'))
#         estimated(size=input1, time=input2, number=None)
#     elif types == 2:
#         input1 = float(input('请输入项目大小：（1代表标准大小，可以输入小数）'))
#         input2 = int(input('请输入人力数量：（请输入整数）'))
#         estimated(size=input1, number=input2, time=None)
#
# choice()

def myinput():
    choice = input('请选择计算类型：（1-人力计算，2-工时计算')
    if choice == '1':
        size = float(input('请输入项目大小：（1代表标准大小，可以输入小数）'))
        number = None
        time = float(input('请输入工时数量：（请输入小数）'))
        return size, number, time
    elif choice == '2':
        size = float(input('请输入项目大小：（1代表标准大小，可以输入小数）'))
        number =  int(input('请输入人力数量：（请输入整数）'))
        time = None
        return size, number, time

def estimated(my_input):
    size = my_input[0]
    number = my_input[1]
    time = my_input[2]
    if (number == None) and (time != None):
        number = math.ceil(size * 80 / time)
        print('项目大小为%.1f个标准项目，如果需要在%.1f个工时完成，则需要人力数量为：%d人' %(size,time,number))
    elif (number != None) and (time == None):
        time = size * 80 / number
        print('项目大小为%.1f个标准项目，使用%d个人力完成，则需要工时数量为：%.1f个' %(size,number,time))

def main():
    my_input = myinput()
    estimated(my_input)

main()


