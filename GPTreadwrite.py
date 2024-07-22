"""Author: 0x4D, 桐镜
#   Update Time: 2020/07/08
#   Version: 1.0
#   Description: GPT: General Purpose Tools, readwrite: ReadWrite Service Module.
"""
import pandas
import warnings
from GPTbar import bar
class readwrite:
    """
    :文件读写服务模块
    :提供读取和写入文本文件的功能，用于处理域名列表等数据的存取。
    """
    def __init__(self):
        """初始化读写服务。
        :param file_path: 文件路径，用于指定读取和写入的文件。
        """
        warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl.styles.stylesheet")
        self.excel_path = "test.xlsx"
        self.txt_path = "test.txt"
    
    def read_text(self, file_path=None, read_method='r', to_list=True, encoding='utf-8'):
        """读取文本文件内容。
        :return: 返回文件中每行的列表，排除空行。
        """
        try:
            with open(file_path, read_method, encoding=encoding) as file:
                return [line.strip() for line in bar(file, task=f"Reading {file_path}") if line.strip()] if to_list else file.read()
        except Exception as e:
            pass
    def write_text(self, file_path=None, write_method='w', encoding='utf-8', lines=None):
        """将列表中的数据写入文本文件。
        :param lines: 字符串列表，每个元素代表一行写入的内容。
        """
        try:
            with open(file_path, write_method, encoding=encoding) as file:
                file.write('\n'.join(lines))
            return True
        except Exception as e:
            try:
                with open(file_path, write_method, encoding=encoding) as file:
                    for line in bar(lines, task="Writing lines"):
                        file.write(f"{line}" + '\n')
                return True
            except:
                print(f'写入文件错误: {e}')
                return False

    def read_excel(self, file_path=None, to_list=True, sheet_name=0, header=None, start_row=0):
        """直接读取excel文件, 返回DataFrame。
        :param lines: 字符串列表，每个元素代表一行写入的内容。
        """
        try:
            read_data = pandas.read_excel(file_path, sheet_name, header=header, skiprows=start_row) if to_list else pandas.read_excel(file_path, sheet_name, header=header, skiprows=start_row, nrows=1)
            return [' 20% '.join(map(str, row.fillna('null').tolist())) for index, row in bar(read_data.iterrows(), task=f"Reading {file_path}")] if to_list else [' 20% '.join(map(str, row.fillna('null').tolist())) for index, row in read_data.iterrows()][0]
        except Exception as e:
            pass
    def write_excel(self, file_path=None, data=None, sheet_name="Sheet1"):
        try:
            pandas.DataFrame(data).to_excel(file_path, sheet_name=sheet_name, index=False)
        except:
            pandas.DataFrame({list(data.keys())[0]: data[list(data.keys())[0]]}).to_excel(file_path, sheet_name=sheet_name, index=False)
