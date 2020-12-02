import requests
import json
from common.doParseExcel import DoParseExcel


class RestApi:

    def parse_request(self, line):
        base_url = 'https://customer-sit-api.fcb.com.cn'

        case_id = line['caseid']
        path = line['interfacePath']
        method = line['method']
        headers = line['headers']
        headers = headers.replace('" ', '"')  # headers写得不规范，有空格，这里去除
        headers = json.loads(headers)  # 转换成json格式
        body = line['body']
        desc = line['description']

        print(base_url + path) # 打印api地址
        res = requests.post(base_url + path, data=json.dumps(body), headers=headers)
        return res


if __name__ == '__main__':
    lines = DoParseExcel().doGetLines('首页')
    for line in lines:
        res = RestApi().parse_request(line)
        if res.text != '':
            print(res.json())
