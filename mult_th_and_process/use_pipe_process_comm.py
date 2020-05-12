import multiprocessing
import os, time, random

# Pipe通信机制，
# Pipe常用于两个进程，两个进程分别位于管道的两端
# Pipe方法返回（conn1,conn2）代表一个管道的两个端
# Pipe方法有duplex参数，默认为True，即全双工模式，若为FALSE,conn1只负责接收信息，conn2负责发送，

#写数据进程执行的代码
def proc_send(pipe,urls):
    #print 'Process is write....'
    for url in urls:
        print('Process is send :%s' % url)
        pipe.send(url)
        time.sleep(random.random())

#读数据进程的代码
def proc_recv(pipe):
    while True:
        print('Process rev:%s' % pipe.recv())
        time.sleep(random.random())

def main():
    #父进程创建pipe，并传给各个子进程
    pipe = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=proc_send,args=(pipe[0],['url_'+str(i) for i in range(10) ]))
    p2 = multiprocessing.Process(target=proc_recv,args=(pipe[1],))
    #启动子进程，写入
    p1.start()
    p2.start()

    p1.join()
    p2.terminate()
    
if __name__ == "__main__":
    main()