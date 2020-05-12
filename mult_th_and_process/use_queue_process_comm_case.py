from multiprocessing import Process, Queue
import os,time,random

# Queue用于多进程通信
# Put方法：以插入数据到队列中
# Get方法：从队列读取并且删除一个元素

# 写数据进程执行的代码
def proc_write(q, urls):
    print("process is write...")
    for url in urls:
        q.put(url)
        print("put %s to queue..." % url)
        time.sleep(random.random())

# 读数据进程执行的代码
def proc_read(q):
    print("process is read...")
    while True:
        url = q.get(True)
        print("Get %s from queue" % url)

def main():
    # 主进程创建Queue,并传给各个子进程
    q = Queue()
    proc_write1 = Process(target=proc_write, args=(q,['url_1', 'url_2', 'url_3']))
    proc_write2 = Process(target=proc_write, args=(q,['url_4', 'url_5', 'url_6']))
    proc_reader = Process(target=proc_read, args=(q,))
    
    # 启动子进程,写入
    proc_write1.start()
    proc_write2.start()
    # 启动读进程,读取
    proc_reader.start()
    
    # 等待写进程终止
    proc_write1.join()
    proc_write2.join()
    # 读进程为死循环,强制终止
    proc_reader.terminate()

if __name__ == "__main__":
    main()