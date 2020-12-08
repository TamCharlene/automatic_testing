import os
import requests
import json

from common.doConfig import GetInfo
from common.doParseExcel import DoParseExcel


class RestApi:

    def parse_request(self, line):
        """
        1.从/config/env_info.cfg文件中把url读取出来
        2.调用doParseExcel把测试用例从Excel中读取出来
        3.使用request请求接口
        :param line: Excel用例
        :return: json
        """
        # 1.从/config/env_info.cfg文件中把url读取出来
        cf = GetInfo(os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/config/env_info.cfg")
        base_url = cf.get_info_for_public('TEST_HOST')
        base_url_re = base_url.get('fcb_app_host_c')

        #2.调用doParseExcel把测试用例从Excel中读取出来
        case_id = line['caseid']
        path = line['interfacePath']
        method = line['method']
        headers = line['headers']
        headers = headers.replace('" ', '"')  # headers写得不规范，有空格，这里去除
        headers = json.loads(headers)  # 转换成json格式
        body = line['body']
        desc = line['description']

        #3.使用request请求接口
        print(base_url_re + path) # 打印api地址
        res = requests.post(base_url_re + path, data=json.dumps(body), headers=headers)
        return res

if __name__ == '__main__':
    lines = DoParseExcel().doGetLines('首页')
    for line in lines:
        res = RestApi().parse_request(line)
        if res.text != '':
            print(res.json())
