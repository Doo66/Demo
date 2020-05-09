# 初识类
class Student(object):
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法可以为学生对象绑定name和age两个属性
    def __init__(self, name, age, color):
        self.name = name # public
        self.age = age   # public
        self.__bed_color = color # private
    
    def study(self, couse_name):
        print('%s正在学习%s.' % (self.name, couse_name))
        
    def see_bed_color(self):
        print('%s床的颜色是%s.' % (self.name, self.__bed_color))
        
    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看小猪佩奇.' % self.name)
        else:
            print('%s正在观看大电影.' % self.name)

def main():
    stu1 = Student('hinata', 16, 'blue')
    stu1.study('白眼')
    stu1.watch_movie()
    stu1.see_bed_color()
    stu2 = Student('jiraya', 30, 'yellow')
    stu2.study('通灵术')
    stu2.watch_movie()
    stu2.see_bed_color()

if __name__ == '__main__':
    main()
else:
    print("error")