# Python中每个文件就代表了一个模块（module）

# 1.import library as lib # 给库library生成一个别名lib
# 2.from lib import fun   # 引用lib库中的fun函数
# 3.import lib #导入lib模块
# 2,3区别为使用2使用fun函数时，须注明哪个模块的fun函数，3直接引用即可
import module1 as m1
import module2 as m2

# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    m1.foo()
else:
    m2.foo()