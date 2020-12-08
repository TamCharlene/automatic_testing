import os
import json
import requests
from common.doConfig import GetInfo


class DoLoginOut:

    def getUrl(self):
        """
        从配置文件中接口url
        :return: 接口url
        """
        cf = GetInfo(os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/config/user_info.cfg")
        base_interface = cf.get_info_for_public('INTERFACE')
        return base_interface

    def getHeaders(self):
        """

        :return:
        """
        cf = GetInfo(os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/config/user_info.cfg")
        base_headers = cf.get_info_for_public('HEADERS')
        return  base_headers

    def getUser(self):
        """

        :return:
        """
        cf = GetInfo(os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/config/user_info.cfg")
        user_info = cf.get_info_for_public('USER_INFO')
        return user_info

    def getBody(self):
        """

        :return:
        """
        cf = GetInfo(os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/config/user_info.cfg")
        body = cf.get_info_for_public('BODY')
        return body

    def login(self):
        """
        1.获取验证码
        2.登录
        :return:返回json
        """
        # 从配置文件中读取host
        cf = GetInfo(os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/config/env_info.cfg")
        base_url = cf.get_info_for_public('TEST_HOST')
        base_url_re = base_url.get('fcb_app_host_c')

        #url
        data_code = {
                        "phone": DoLoginOut().getUser().get('phone'),
                        "type": DoLoginOut().getBody().get('type'),
                        "by_voice_code": DoLoginOut().getBody().get('by_voice_code')}
        data_login = {
                        "code": DoLoginOut().getUser().get('password'),
                        "phone": DoLoginOut().getUser().get('phone'),
                        "registerFrom": DoLoginOut().getBody().get('registerFrom'),
                        "terminalVersion":DoLoginOut().getBody().get('terminalVersion'),
                        "os_type": DoLoginOut().getBody().get('os_type'),
                        "clientType": DoLoginOut().getBody().get('clientType')
                    }
        res_code = requests.post(base_url_re+DoLoginOut().getUrl().get('getCode'), data=json.dumps(data_code), headers=DoLoginOut().getHeaders())
        res_login = requests.post(base_url_re+DoLoginOut().getUrl().get('login'), data=json.dumps(data_login), headers=DoLoginOut().getHeaders())

        return res_login.json()

if __name__ == '__main__':
    re = DoLoginOut().login()
    print(re)


