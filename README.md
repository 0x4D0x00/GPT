```python
"""Author: 0x4D, 桐镜
#   Update Time: 2020/07/08
#   Version: 1.0
#   Description: GPT: General Purpose Tools
"""

"""
#   About all GPT usage method.txt
"""

#    当你在奇怪为什么有的函数只传一个字符串,有的函数传列表时,请结合多线程模块 mtti 考虑.

"""
#   about mtti usage method
#   关于多线程工具使用方法
"""
if __name__ == '__main__':
    demo_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    def demo(x):
    return x * x
    from GPTmtti import MtTi
    mtti = MtTi()
    # thread_list = mtti.thread_execute(demo, demo_list)
    thread_list = mtti.thread_execute_bar(demo, demo_list)
    # or thread_list = mtti.thread_execute_bar(demo, demo_list, task="My Task", max_workers=10)
    print(thread_list)





"""
#   about bar usage method
#   关于进度条工具使用方法
"""
class task:
    def __init__(self):
        self.newlist = []
    def test(self, mylist):
        """
        #   Following the logic of the display function, after executing the test2 function, continue adding tasks using the add method.
        #   按照展示函数逻辑, 执行结束test2函数之后, 通过add方法继续添加任务。
        """
        self.pbar.add(mylist, last=True, task="test")
        for i in self.pbar:
            #   Focus on the above 2 lines.
            #   重点关注以上 2 行。
            if i % 2 == 0:
                time.sleep(0.05)
                self.newlist.append(i)
        return self.newlist
    def test2(self):
        mylist = []
        """
        #   Inherit the upper and lower tasks, and dynamically add the number of tasks using the add method (tasks are iterable objects).
        #   继承上下任务,动态添加任务数量时使用add方法添加任务(任务为可迭代对象)。
        """
        self.pbar=bar()
        self.pbar.add(range(100), task="test2")
        for i in self.pbar:
            #   Focus on the above 3 lines.
            #   重点关注以上 3 行。
            time.sleep(0.05)
            mylist.append(i)
        newlist = self.test(mylist)
        return newlist
    def test3(self):
        """
        #   When setting a progress bar independently for a task without using inheritance, use this method.
        #   不使用继承的方式, 为任务独立设定进度条时,使用此方法。
        """
        test3list = []
        for i in bar(range(10,20)):
            #   Focus on the above 1 lines.
            #   重点关注以上 1 行。
            time.sleep(1)
            test3list.append(i)
        return test3list
if __name__ == "__main__":
    test1 = task()
    newlist = test1.test2()
    print(newlist)
    test3list = test1.test3()
    print(test3list)





"""
#   about network usage method
#   关于网络诊断工具示例用法
"""
if __name__ == '__main__':
    diagnostics = network()
    domain = 'www.baidu.com'
    """
    #   ping 操作示例用法
    """
    success, response = diagnostics.ping(domain)
    print('Ping successful:', success)
    print('Response:', response)
    """
    #   nslookup 操作示例用法
    """
    output = diagnostics.nslookup(domain)
    print(f"Result: {output[0]}, Info: {output[1]}")
    """
    #   refresh 操作示例用法
    """
    success = diagnostics.refresh()
    print('Refresh successful:', success)
    """
    #   request 操作示例用法
    """
    target = "https://www.baidu.com"
    data = {
        "username": "admin",
        "password": "password"
    }
    response = diagnostics.request("get", target)
    print(len(response))





"""
#   about gain usage method
#   关于 gain 示例用法
"""
if __name__ == '__main__':
    get = gain()
    """
    #   提取IP地址
    """
    ip = get.extract_ip('Example text with IP 192.168.1.1 in it')
    print('Extracted IP:', ip)
    """
    #   提取域名
    """
    domain = get.extract_domain('Example text with Domain example.com in it')
    print('Extracted Domain:', domain)
    """
    #   获取文件大小
    """
    logs_path = '正面攻击告警日志20240712165359.xls'
    file_size = get.extract_file_size(logs_path)
    print(file_size)




"""
#   about readwrite usage methods
#   关于读写工具示例用法
"""
if __name__ == '__main__':
    rw = readwrite()
    file_path = 'domain_list.txt'
    logs_path = '正面攻击告警日志20240712165359.xls'
    """
    #   read_file
    #   读文件,to_list是生成列表
    """
    rw.read_file(file_path)
    rw.read_file_to_list(file_path)
    """
    #   write_file
    #   写文件,lines是列表
    """
    rw.write_file(file_path, lines=['0x4D', '0x4D', '0x4D'])
    """
    #   read_excel
    #   读excel,生成列表
    """
    index = rw.read_excel(logs_path)
    print(index)
```
