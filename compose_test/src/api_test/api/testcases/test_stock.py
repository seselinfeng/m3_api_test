import pytest

from src.api_test.api.testcases.test_base import TestBase
from src.api_test.api.utils.processingdata import get_data


class TestStock(TestBase):

    @pytest.mark.parametrize("test_stock_data", get_data("test_stock", '../data/stock_template.yaml'))
    def test_stock(self, test_stock_data):
        """
        测试获取当前时间段游戏机数量
        :param test_stock_data: 获取当前游戏机数量请求参数
        :return: 断言接口返回状态是否为200
        """
        venv_data = {
            "inDate": "2020/07/31"
        }
        assert self.stock.get_stock(str(test_stock_data), venv_data).json()['state'] == '200'
