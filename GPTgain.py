"""Author: 0x4D, 桐镜
#   Update Time: 2020/07/08
#   Version: 1.0
#   Description: GPT: General Purpose Tools, bar: Progress bar Service Module.
"""
import re
from pathlib import Path

class gain:
    """
    #   获取ip地址,域名,文件大小的模块
    #   用于从给定的文本中提取第一个有效的 IP 地址。
    """
    def __init__(self):
        """初始化 IP 提取器。
        #   param target: 包含 IP 地址的目标文本。
        """
        self.ip_pattern = re.compile(r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}')  # IP 地址的正则表达式
        self.domain_pattern = re.compile(r'[a-zA-Z0-9][a-zA-Z0-9-]{1,61}[a-zA-Z0-9](?:\.[a-zA-Z]{2,})+')

    def extract_ip(self, target):
        """从目标文本中提取 IP 地址。
        #   return: 提取到的第一个 IP 地址，如果没有找到则返回 None。
        """
        match = self.ip_pattern.search(target)
        return match.group() if match else None
    
    def extract_domain(self, target):
        """从目标文本中提取域名。
        #   return: 提取到的第一个域名，如果没有找到则返回 None。
        """
        match = self.domain_pattern.search(target)
        return match.group() if match else None
    def extract_file_size(self, file_path):
        """获取文件大小。
        #   return: 根据文件字节长度返回文件大小
        """
        file_path = Path(file_path)
        if file_path.exists() and file_path.is_file():
            size = file_path.stat().st_size
            if size >= 1073741824:
                return f"{size / 1073741824:.2f}GB"
            elif size >= 1048576 and size < 1073741824:
                return f"{size / 1048576:.2f}MB"
            elif size >= 1024 and size < 1048576:
                return f"{size / 1024:.2f}KB"
            else:
                return f"{size}B"
