# 水仙花数
def shuixianhua():
    for num in range(100, 1000):
        low = num % 10
        mid = num // 10 % 10
        high = num // 100
        if num == low ** 3 + mid ** 3 + high **3:
            print(num)

# 只有被python解释器直接执行的模块才被命名为__main__
if __name__ == '__main__':
    shuixianhua()
else:
    print("error")
    