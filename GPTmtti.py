"""
#   Author: 0x4D, 桐镜
#   Update Time: 2020/07/08
#   Version: 1.0
#   Description: GPT:General Purpose Tools
#               mtti:Multithreading
"""
import time
from GPTbar import bar
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
class MtTi():
    """
    #   Multi functional and Multi process Service Module.
    #   Used for parallel execution of multiple tasks to improve processing efficiency.
    #   多功能多流程服务模块。
    #   用于并行执行多个任务的多功能多流程服务模块。
    """
    def __init__(self):
        """
        #   Initialize multiprocessing service.
        #   param func: The function to be executed in parallel.
        #   param iterable: The dataset that needs to be processed.
        #   param max_workers: The maximum number of working threads in the thread pool.
        #   初始化多进程服务。
        #   参数 func: 需要并行执行的函数。
        #   参数 iterable: 需要处理的数据集。
        #   参数 max_workers: 线程池中最大线程数。
        """
        pass
    def monitor_runtime(func):
        """
        #   Decorator: used to monitor function runtime.
        #   装饰器: 用于监控函数运行时间。
        """
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
        #   ThreadPoolExecutor incognito processing task
        #   ThreadPoolExecutor 无痕处理任务
        """
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(func, iterable))
        return results
    def process_execute(self, func, iterable, max_workers=None):
        """
        #   ProcessPoolExecutor incognito processing task
        #   ProcessPoolExecutor 无痕处理任务
        """
        with ProcessPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(func, iterable))
        return results
    def thread_execute_bar(self, func, iterable, task="多线程任务", max_workers=None):
        """
        #   With bar progress bar
        #   带bar进度条
        """
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(bar(executor.map(func, iterable), total=len(iterable), task=task))
        return results
    @monitor_runtime
    def thread_execute_tqdm(self, func, iterable, max_workers=None):
        """
        #   With tqdm progress bar
        #   带tqdm进度条
        """
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(tqdm(executor.map(func, iterable), total=len(iterable)))
        return results
