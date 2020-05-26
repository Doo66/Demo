# 异步处理:从调度程序的任务队列中挑选任务，该调度程序以交叉的形式执行这些任务，
# 我们并不能保证任务将以某种顺序去执行，因为执行顺序取决于队列中的一项任务是否
# 愿意将CPU处理时间让位给另一项任务。异步任务通常通过多任务协作处理的方式来实现，
# 由于执行时间和顺序的不确定，因此需要通过回调式编程或者future对象来获取任务执行的结果
"""
通过asyncio模块和await和async关键字来支持异步处理
"""

"""
异步I/O - async/await
"""
import asyncio

def num_generator(m, n):
    """指定范围的数字生成器"""
    yield from range(m, n+1)

async def prime_filter(m, n):
    """素数过滤器"""
    primes = []
    for i in num_generator(m, n):
        flag = True
        for j in range(2, int(i ** 0.5 + 1)):
            if i % j == 0:
                flag = False
                break
        if flag:
            print('Prime => ', i)
            primes.append(i)
        await asyncio.sleep(0.001)
    return tuple(primes)

async def square_mapper(m, n):
    """平方映射器"""
    squares = []
    for i in num_generator(m, n):
        print('Square => ', i * i)
        squares.append(i*i)
        await asyncio.sleep(0.001)
    return squares

def main():
    """主函数"""
    # get_event_loop()获取系统默认的事件循环
    loop = asyncio.get_event_loop()
    # 通过gatter函数可以获得一个future对象
    future = asyncio.gather(prime_filter(2, 100), square_mapper(1, 100))
    # add_done_callback可以添加执行完成时的回调函数
    future.add_done_callback(lambda x : print(x.result()))
    # run_until_complete方法可以等待通过future对象获得协程执行结果
    loop.run_until_complete(future)
    # 处理完成之后，关闭事件循环
    loop.close()

if __name__ == "__main__":
    main()
    