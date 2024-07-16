"""
#   Author: 0x4D, 桐镜
#   Update Time: 2020/07/08
#   Version: 1.0
#   Description: GPT:General Purpose Tools
#                bar:Progress bar
"""
import sys
import time
import io
class bar:
    def __init__(self, iterable=None, total=0, task="Current progress"):
        self.task = task.ljust(20)
        self.start_time = time.time()
        self.iterable = iter(iterable) if iterable is not None else None
        self.output_buffer =  sys.stdout if total == 0 else io.StringIO()
        self.total = total
        self.current = 0
        self._is_completed = True
        if iterable is not None and total == 0:
            try:
                self.total = len(iterable)
            except TypeError as e:
                self.total = None
    def __iter__(self):
        if self.iterable is None:
            return
        else:
            self.__update(0)
            try:
                while True:
                    yield next(self.iterable)
                    self.__update()
            except StopIteration:
                self.__buffer(buffer=None)
    def add(self, iterable=None, last=False, task="Current progress"):
        self.task = task.ljust(20)
        self._is_completed = last
        self.iterable = iter(iterable) if iterable is not None else None
        self.output_buffer = sys.stdout
        if iterable is not None:
            try:
                self.total += len(iterable)
            except TypeError:
                self.total = None
    def __update(self, current=1):
        def output(output_str):
            self.output_buffer.write(output_str)
            self.output_buffer.flush()
        self.current += current
        self.elapsed_time = time.time() - self.start_time
        speed = self.current / self.elapsed_time if self.elapsed_time > 0 else 0
        formatted_time = time.strftime("%M:%S", time.gmtime(self.elapsed_time))
        if self.total is None:
            output_str = f"\r[{self.task}] | {self.current} [{formatted_time}, {speed:.2f} it/s]"
            output(output_str)
            return
        if self.total < 1:
            self.total = len(self.iterable)
        if self.current > self.total:
            self.current = self.total
        remaining_time = (self.total - self.current) / speed if speed > 0 else '?'
        remaining_time_str = f"{int(remaining_time // 60):02}:{int(remaining_time % 60):02}" if remaining_time != '?' else '?'
        bar_length = 50
        percent = int(round((self.current / self.total) * 100))
        filled_length = int(round(bar_length * percent / 100))
        bar = '█' * filled_length + ' ' * (bar_length - filled_length)
        output_str = f"\r[{self.task}] | {percent:6.2f}% | {bar} | {self.current}/{self.total} [{formatted_time}<{remaining_time_str}, {speed:.2f} it/s]"
        output(output_str)
    def __buffer(self, buffer):
        if self._is_completed and buffer is not None:
            self.output_buffer = io.StringIO()
            self.__update()
            self.output_buffer.write('\n')
        elif self._is_completed:
            self.output_buffer = sys.stdout
            self.__update()
            print()
