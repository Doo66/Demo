# Python中每个文件就代表了一个模块（module）

# import library as lib 给库library生成一个别名lib 
import module1 as m1
import module2 as m2

# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    m1.foo()
else:
    m2.foo()