# 递归函数的形成条件
# 1.函数自己调用自己
# 2.函数必须有一个终止条件


def get_age(num):
    """
    求第 num 个人的年龄，每想邻的两个人的年龄差两岁， 已知第一人的年龄是18岁
    :param num:
    :return:
    """
    if num == 1:
        return 18
    # 求第num 个人的年龄，只需要num-1 这个人的年龄+2
    age = get_age(num-1) + 2
    return age

print(get_age(4))

