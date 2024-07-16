<br>"""
<br>#   About all GPT usage method.txt
<br>"""
<br>"""
<br>#   about mtti usage method
<br>#   关于多线程工具使用方法
<br>"""
<br>if __name__ == '__main__':
<br>    demo_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
<br>    def demo(x):
<br>    return x * x
<br>    from GPTmtti import MtTi
<br>    mtti = MtTi()
<br>    # thread_list = mtti.thread_execute(demo, demo_list)
<br>    thread_list = mtti.thread_execute_bar(demo, demo_list)
<br>    # or thread_list = mtti.thread_execute_bar(demo, demo_list, task="My Task", max_workers=10)
<br>    print(thread_list)
<br>"""
<br>#   about bar usage method
<br>#   关于进度条工具使用方法
<br>"""
<br>class task:
<br>    def __init__(self):
<br>    self.newlist = []
<br>    def test(self, mylist):
<br>    """
<br>    #   Following the logic of the display function, after executing the test2 function, continue adding tasks using the add method.
<br>    #   按照展示函数逻辑, 执行结束test2函数之后, 通过add方法继续添加任务。
<br>    """
<br>    self.pbar.add(mylist, last=True, task="test")
<br>    for i in self.pbar:
<br>    #   Focus on the above 2 lines.
<br>    #   重点关注以上 2 行。
<br>    if i % 2 == 0:
<br>    time.sleep(0.05)
<br>    self.newlist.append(i)
<br>    return self.newlist
<br>    def test2(self):
<br>    mylist = []
<br>    """
<br>    #   Inherit the upper and lower tasks, and dynamically add the number of tasks using the add method (tasks are iterable objects).
<br>    #   继承上下任务,动态添加任务数量时使用add方法添加任务(任务为可迭代对象)。
<br>    """
<br>    self.pbar=bar()
<br>    self.pbar.add(range(100), task="test2")
<br>    for i in self.pbar:
<br>    #   Focus on the above 3 lines.
<br>    #   重点关注以上 3 行。
<br>    time.sleep(0.05)
<br>    mylist.append(i)
<br>    newlist = self.test(mylist)
<br>    return newlist
<br>    def test3(self):
<br>    """
<br>    #   When setting a progress bar independently for a task without using inheritance, use this method.
<br>    #   不使用继承的方式, 为任务独立设定进度条时,使用此方法。
<br>    """
<br>    test3list = []
<br>    for i in bar(range(10,20)):
<br>    #   Focus on the above 1 lines.
<br>    #   重点关注以上 1 行。
<br>    time.sleep(1)
<br>    test3list.append(i)
<br>    return test3list
<br>if __name__ == "__main__":
<br>    test1 = task()
<br>    newlist = test1.test2()
<br>    print(newlist)
<br>    test3list = test1.test3()
<br>    print(test3list)
