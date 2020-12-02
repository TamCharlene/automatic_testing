import requests
import os
from common.doExcel import DoExcel


class DoParseExcel:
    def doGetLines(self, sheet_name):
        api_excel = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/data/client_app_case.xlsx"
        datas = DoExcel.get_sheets(api_excel)
        sheet = datas[sheet_name]
        return sheet


if __name__ == '__main__':
    DoParseExcel().doGetLines('首页')
