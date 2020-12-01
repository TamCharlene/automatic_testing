import requests
import os
import json
import base64
import urllib3
from requests.cookies import RequestsCookieJar

from common.doConfig import GetInfo
from common.doExcel import DoExcel
from common.doLog import GetLog

urllib3.disable_warnings()
logger = GetLog().logger()

class HttpRequest:

    def httpRequest(self, url, data, method, headers):
        """
        接口请求
        :param url:接口url
        :param data: body
        :param method: 接口请求方式
        :param headers: 头
        :return:
        """
        if method.upper() =="GET":
            request = requests.get(url, data=json.dumps(data), headers=headers)
            res = requests.json()
            null = "null"
            false = "false"
            return request.status_code, request.json()

        elif method.upper() == "POST":
            request = requests.post(url=url, data=json.dumps(data), headers=headers)
            null = "null"
            false = "false"
            return request.status_code, request.json()
        else:
            logger.info("未知方法")

    def post_upload_file(self, url, headers, file_name, file_absolute_path, content_type):
        """post方法上传文件:
        url:上传接口的url
        headers:请求头
        file_name:上传文件的名称,如：delete_middleend_case.xlsx
        file_absolute_path:上传文件的全路径，如：r'E:\FCB_Auto_Test\FCB_Auto_Test\data\delete_middleend_case.xlsx'
        content_type:上传的Content-Type，如：application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
        """
        fl = open(file_absolute_path, 'rb')
        files = {'file': (file_name, fl,
                          content_type)}

        res = requests.post(url=url, files=files, headers=headers)
        return res

class DoHttpRequest:

    def doUrl(self):
        """
        取出接口url
        :param url:
        :return:
        """
        """
        从env_info.cfg文件中把host取出来，存到host_url变量中
        """
        cf = GetInfo(os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/config/env_info.cfg")
        cf_urls = cf.get_info_for_public("TEST_HOST")
        host_url = cf_urls.get("fcb_app_host_c")
        """
        从data目录下，Excel表格中接口的url取出来，存到url_list[]列表中
        """
        url_list = []
        apiExcel = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/data/client_app_case.xlsx"
        api_info = apiExcel.sheet_names
        for item in api_info:
            url_list.append(host_url + api_info.interfacePath)

        return url_list

    def doData(self):
        """
        取出接口data
        :param data:
        :return:
        """
        """
        从data目录下，Excel表格中接口的body取出来，存到data_list[]列表中
        """
        data_list = []
        apiExcel = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/data/client_app_case.xlsx"
        api_info = apiExcel.sheet_names
        for item in api_info:
            data_list.append(api_info.body)
        return data_list

    def doHeader(self, headers):
        """
        取出接口headers
        :param headers:
        :return:
        """
        """
        从data目录下，Excel表格中接口的body取出来，存到headers_list[]列表中
        """
        headers_list = []
        apiExcel = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/data/client_app_case.xlsx"
        api_info = apiExcel.sheet_names
        for item in api_info:
            headers_list.append(api_info.headers)
        return headers_list

