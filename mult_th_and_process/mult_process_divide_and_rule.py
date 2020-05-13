from multiprocessing import Process, Queue
from random import randint
from time import time

def task_handler(cur_list, result_queue):
    total = 0
    for number in cur_list:
        total += number
    result_queue.put(total)

def main():
    process = []
    number_list = [x for x in range(1,50000001)]
    result_queue = Queue()
    index = 0
    # 启动8个进程将数据切片后进行计算
    for _ in range(5):
        p = Process(target=task_handler, args=(number_list[index:index+10000000], result_queue))
        index += 10000000
        process.append(p)
        p.start()
    # 记录所有进程执行完成花费的时间
    start = time()
    for p in process:
        p.join()
    # 合并执行结果
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print('Execution time:%.3fs' % (end-start))

if __name__ == "__main__":
    main()