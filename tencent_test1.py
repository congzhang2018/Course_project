# #coding=utf-8
# # 本题为考试单行多行输入输出规范示例，无需提交，不计分。
# import sys
# def lcm(alist):
#     greater = max(alist)
#     length = len(alist)
#     counter = 0
#     # print(counter, length,greater)
#     while(True):
#         for i in alist:
#             if (greater % i == 0):
#                 counter += 1
#         if counter == length:
#             lcm = greater
#             break
#         greater += 1
#         counter = 0
#     return lcm
# def add(x):
#     return x+1
#
# if __name__ == "__main__":
#     # for line in sys.stdin:
#     #     n = int(line.split()) + 1
#     n = 4
#     m = n
#     while(True):
#         num1 = list(map(int, range(n,m+1)))
#         num2 = list(map(add, range(m)))
#         a = lcm(num1)
#         b = lcm(num2)
#         if a == b:
#             print(m)
#             break
#         m += 1
# coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys




def compute(n, alist):
    counter = 0
    for i in range(n + 1):
        x = 0
        y = 0
        for a in range(0, 2, len(alist)):
            if alist[a] == i:
                x += 1
            y = count_y(i, alist)
        if y > x:
            counter += 1
    print(counter)


def count_y(city, alist):
    y = 0
    for a in range(0, 2, len(alist)):
        if alist[a + 1] == city:
            city1 = alist[a + 1]
            y += 1
        return y + count_y(city1, alist)


if __name__ == "__main__":
    # 读取第一行的n
    n, m = int(sys.stdin.readline().strip())
    road = []
    for i in range(m):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        road = road + values
    compute(n, road)
