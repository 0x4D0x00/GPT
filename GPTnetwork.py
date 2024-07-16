"""Author: 0x4D, 桐镜
#   Update Time: 2020/07/08
#   Version: 1.0
#   Description: GPT: General Purpose Tools, network: About network diagnostics or check Service Module.
"""
import subprocess
import platform
import requests
import re
class network:
    '''
    #   网络诊断模块
    #   用于执行网络 诊断 操作，检查网络连通性。
    '''
    def __init__(self):
        self.system_name = self._system_type()
        self.user_agent = "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0"
        self.cookies = ""
        self.headers = {
            "User-Agent": self.user_agent,
            "Cookie": self.cookies
        }
    def _system_type(self):
        self.system_name = platform.system()
        self.ping_cmd = ['ping', '-n', '1'] if self.system_name == 'Windows' else ['ping', '-c', '1']
        self.nslookup_cmd = ['nslookup'] if self.system_name == 'Windows' else ['dig', '+short']
        self.ip_pattern = re.compile(r'名称') if self.system_name == 'Windows' else re.compile(r'^\S+$')
        self.ipconfig_cmd = ['ipconfig'] if self.system_name == 'Windows' else ['sudo']
    def ping(self, target):
        """对指定目标执行 Ping 命令。
        #   param target: 要 Ping 的目标地址。
        #   return: 布尔值表示成功与否，以及响应结果或错误信息。
        """
        args = self.ping_cmd + [target]
        try:
            result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            return ('time=' in result.stdout or '时间=' in result.stdout, result.stdout)
        except subprocess.TimeoutExpired:
            return (False, 'Ping request timed out')
        except Exception as e:
            return (False, str(e))
    def nslookup(self, target):
        try:
            args = self.nslookup_cmd + [target]
            response = subprocess.run(args, capture_output=True, text=True, timeout=5)
            output = response.stdout.strip()
            if response.returncode != 0:
                return False, f"Error executing command: {output}"
            matches = self.ip_pattern.search(output)
            if matches:
                return True, output
            else:
                return False, "False"
        except subprocess.TimeoutExpired:
            return False, "Command timed out."
        except Exception as e:
            return False, f"An error occurred: {e}"
    def refresh(self, target="/flushdns"):
        """执行 ipconfig或sudo 命令。
        #   param target: DNS 缓存刷新命令。
        #   return: 布尔值表示成功与否，以及响应结果或错误信息。
        """
        if self.system_name != 'Windows':
            target = ['killall', '-HUP', 'dnsmasq']
        args = self.ipconfig_cmd + [target]
        try:
            result = subprocess.run(args, capture_output=True, text=True, check=True)
            return (result.stdout)
        except subprocess.TimeoutExpired:
            return (False, 'DNS cache refresh failed')
        except Exception as e:
            return (False, str(e))
    def request(self, method, target, data=None, verify=False, timeout=5):
        """
        #   发送 HTTP 请求。
        """
        self.request_method = {
            "get": requests.get,
            "post": requests.post,
            "put": requests.put,
            "delete": requests.delete,
            "patch": requests.patch,
            "head": requests.head,
            "options": requests.options
            }
        try:
            if method not in self.request_method:
                raise ValueError(None)
            else:
                method = self.request_method[method]
                response = method(target, headers=self.headers, verify=verify, timeout=timeout)if data is None else method(target, headers=self.headers, data=data, verify=verify, timeout=timeout)
                content = response.text
                self.cookies = response.cookies
                if response.status_code == 200 and "Not Found" not in content and "Forbidden" not in content and "Unauthorized" not in content and "Bad Request" not in content:
                    return f"{content}"
                else:
                    return None
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None
