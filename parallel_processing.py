import time
import threading
import multiprocessing


def timit(func):
    def inner():
        start_time = time.perf_counter()
        func()
        end_time = time.perf_counter()
        print(f'Program completed in {end_time - start_time} seconds')
    return inner


def task():
    print('Sleeping for 0.5 sec')
    time.sleep(0.5)
    print('Finished sleeping')


t1: invisible thread
start_time = time.perf_counter()
t2 = threading.Thread(target=task)
t3 = threading.Thread(target=task)
t2.start()
t3.start()
t2.join()
t3.join()
end_time = time.perf_counter()
print(f'Program completed in {end_time - start_time} seconds')

# def t():
#     t = threading.Thread(target=task)
#     t.start()
#     t.join()


# @timit
# def thread_multiple():
#     threads = []
#     for i in range(10):
#         t = threading.Thread(target=task)
#         t.start()
#         threads.append(t)
#
#     for j in threads:
#         j.join()


# thread_multiple()


# t1 -- execute in cpu --> either completed or waiting for some resource where it is not using cpu
# t2 -- execute


## multiprocessing

# @timit
# def multiprocess_task():
#     processes = []
#     for i in range(10):
#         p = multiprocessing.Process(target=task)
#         p.start()
#         processes.append(p)
#
#     for p in processes:
#         p.join()
#
#
# multiprocess_task()

if __name__ == '__main__':
    processes = []
    start_time = time.perf_counter()

    for i in range(10):
        p = multiprocessing.Process(target=task)
        p.start()
        processes.append(p)

    for j in processes:
        j.join()

    end_time = time.perf_counter()
    print(f'Program completed in {end_time - start_time} seconds')
