import pytest

from compose_test.src.api_test.api.testcases import TestBase
from compose_test.src.api_test.api.utils import get_data


class TestLogin(TestBase):
    @pytest.mark.parametrize("test_login_data", get_data("test_login", '../data/login_template.yaml'))
    def test_login(self, test_login_data):
        """
        测试获取当前用户uticket
        :param test_login_data: 获取当前用户请求参数
        :return: 断言接口返回状态是否为200,获取uticket
        """
        assert self.login.get_uticket(test_login_data).json()['state'] == '200'
