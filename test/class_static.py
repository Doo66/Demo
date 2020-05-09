from math import sqrt

class Triangle(object):
    # 限定Triangle对象只能绑定_a,_b,_c属性
    __slot__ = ('_a', '_b', '_c')
    
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
    
    @staticmethod
    def is_valid(a, b, c):
        a = int(a)
        b = int(b)
        c = int(c)
        return a+b > c and b+c > a and a+c > b
    # 周长
    def perimeter(self):
        return self._a + self._b + self._c
    # 面积
    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) *
                    (half - self._b) *
                    (half - self._c))

def main():
    a,b,c = 3,4,5
    if Triangle.is_valid(a, b, c):
        print("2")
        t = Triangle(a, b, c)
        print(t.perimeter())
        # 也可以通过给类发消息来调用对象方法但是要传入接收消息的对象作为参数
        # print(Triangle.perimeter(t))
        print(t.area())
        # print(Triangle.area(t))
    else:
        print('无法构成三角形.')

if __name__ == '__main__':
    main()