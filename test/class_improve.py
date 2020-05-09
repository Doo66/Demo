# 面向对象进阶
# @property装饰器 getter:访问器 setter:修改器
class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    # 访问器-getter方法
    @property # 使用@property修饰的函数，相当于类的属性
    def name(self):
        return self._name
    
    # 访问器-getter方法
    @property
    def age(self):
        return self._age;
    
    # 修改器-setter方法
    @age.setter # 利用setter对函数age()设置之后,可以进行修改操作
    def age(self, age):
        self._age = age
    
    # 修改器-setter方法
    @name.setter
    def name(self, name):
        self._name = name
    
    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)

def main():
    person = Person("王小锤",12)
    print(person.name,":",person.age) # @property修饰,属性
    person.play()
    person.age = 22
    person.name = "王大锤"
    print(person.name,":",person.age) # @property修饰,属性
    # print(person.age) # @property修饰,属性
    # print(person.name()) # 未使用@property修饰,方法
    person.play()
    
if __name__ == '__main__':
    main()
else:
    print('error')
        