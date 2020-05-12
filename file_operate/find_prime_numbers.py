from math import sqrt

def is_prime(n):
    """判断素数的函数"""
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    if n == 1:
        return False
    else:
        return True
    
def main():
    filenames = ('a.txt', 'b.txt', 'c.txt') # 存放素数文件名
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w',  encoding = 'utf-8')) # 打开创建的文件
        count = 0 # 记录素数的个数
        for number in range(1, 10000):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number) + '\n')
                elif number < 1000:
                    fs_list[1].write(str(number) + '\n')
                else:
                    fs_list[2].write(str(number) + '\n')
                count += 1
    except IOError as ex: # 异常:写文件错误类型
        print(ex)
        print("写文件时发生错误!")
    finally:
        for fs in fs_list:
            fs.close()
    print("1~10000之间有素数%d个." %count)
    print("操作完成!")
    
if __name__ == '__main__':
    main()
else:
    print("error!")