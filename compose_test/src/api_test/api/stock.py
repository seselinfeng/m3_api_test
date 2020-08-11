# 在api package中是代表所有的接口信息的具体的实现，一个公共方法代表一个接口

from src.api_test.api.base_api import BaseApi


class Stock(BaseApi):

    def get_stock(self, test_stock_data, venv_data):
        """获取stock存量"""
        req = self.template(test_stock_data, venv_data)
        r = self.requests_http(req)
        return r
