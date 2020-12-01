import requests
import os
from common.doExcel import DoExcel


class DoParseExcel:
    def doGetLines(self):
        apiExcel = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/data/client_app_case.xlsx"
        # api_info = apiExcel.sheet_names
        datas = DoExcel.get_sheets(apiExcel)
        sheet = datas['首页']
        return sheet


if __name__ == '__main__':
    DoParseExcel().doGetLines()
