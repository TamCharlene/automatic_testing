import pandas
from pandas import DataFrame
import os
from typing import Dict, List

class DoExcel:

    @staticmethod
    def get_sheet(path: str, sheet_name: str or int = 0) -> List:
        """
        获取工作表数据，并用列表形式返回
        :param path: Excel文件地址
        :param sheet_name: 工作表的名称或者下标
        :return:
        """
        df = pandas.read_excel(path, sheet_name=sheet_name)
        data = df.to_dict(orient='records')
        DoExcel.delete_nan(data)
        return data

    @staticmethod
    def get_sheets(path: str) -> Dict:
        """
        获取工作表数据，并用字典形式返回
        :param path: Excel文件地址
        :return: 工作表的名称或者下标
        """
        df = pandas.read_excel(path, sheet_name=None)
        data = {}
        for i in df:
            da = df[i].to_dict(orient='records')
            data[i] = da
        DoExcel.delete_nan(data)
        return data

    @staticmethod
    def delete_nan(data):
        """
        去除字符串中的NAN
        :param data:
        :return:
        """
        for i in data:
            if isinstance(i, dict) or isinstance(i, list):
                DoExcel.delete_nan(i)
            elif isinstance(i, str):
                if isinstance(data, list):
                    if pandas.isnull(i):
                        data.pop(i)
                        data.append(None)
                elif isinstance(data[i], list) or isinstance(data[i], dict):
                    DoExcel.delete_nan(data[i])
                else:
                    if pandas.isnull(data[i]):
                        data[i] = None

if __name__ == '__main__':
    apiExcel = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/data/client_app_case.xlsx"
    datas = DoExcel.get_sheets(apiExcel)
    #datas['首页'][0]['interfacePath']
    print(datas)