# 定义两个函数：第一个函数功能为根据工作月数返回奖金额，第二个函数功能为打印出'该员工来了XX个月，获得奖金XXX元'。
def bonus(month):
    if month < 6:
        bonus = 500
    elif 6 <= month <= 12:
        bonus = month * 120
    else:
        bonus = month * 180
    return bonus


def notice(staff, month):
    number = bonus(month)
    print("%s来了%d个月，获得奖金%d元" %(staff, month, number))

notice('大聪', 24)