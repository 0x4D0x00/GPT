'''
#   Author: 0x4D, 桐镜
#   Update Time: 2020/07/08
#   Version: 1.0
#   Description: GPT:General Purpose Tools
#               mtti:Multithreading
'''
import time
from bar import bar
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
class MtTi():
    '''
    #   多功能多进程服务模块
    #   用于并行执行多个任务，提高处理效率。
    '''
    def __init__(self):
        """初始化多进程服务。
        :param func: 要并行执行的函数。
        :param iterable: 需要处理的数据集。
        :param max_workers: 线程池中的最大工作线程数。
        """
        pass
    def monitor_runtime(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            runtime = end_time - start_time
            print(f"{func.__name__} Runtime: {runtime:.4f} seconds")
            return result
        return wrapper
    def thread_execute(self, func, iterable, max_workers=None):
        """
        #   无痕处理任务
        #   执行并行处理网络/读写任务。
        #   return: 执行结果列表。
        """
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(func, iterable))
        return results
    def process_execute(self, func, iterable, max_workers=None):
        """
        #   无痕处理任务
        #   执行并行处理本地计算任务。
        #   return: 执行结果列表。
        """
        with ProcessPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(func, iterable))
        return results
    def thread_execute_bar(self, func, iterable, task="多线程任务", max_workers=None):
        """
        #   带bar进度条
        #   执行并行处理网络/读写任务。
        #   return: 执行结果列表。
        """
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(bar(executor.map(func, iterable), total=len(iterable), task=task))
        return results
    @monitor_runtime
    def thread_execute_tqdm(self, func, iterable, max_workers=None):
        """
        #   带tqdm进度条
        #   执行并行处理网络/读写任务。
        #   return: 执行结果列表。
        """
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(tqdm(executor.map(func, iterable), total=len(iterable)))
        return results
