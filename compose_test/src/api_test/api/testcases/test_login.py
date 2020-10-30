import pytest
import allure

from api_test.api.testcases.test_base import TestBase
from api_test.api.utils.processingdata import get_data


@allure.feature('登录模块')
class TestLogin(TestBase):
    test_data = get_data("test_login", '../data/manager_login_template.yaml')

    @classmethod
    def setUpClass(cls):
        pass

    @allure.story("登录成功")
    @pytest.mark.parametrize("manager_login", test_data, indirect=True)
    def test_login(self, manager_login):
        """
        测试获取当前用户uticket
        :param test_login_data: 获取当前用户请求参数
        :return: 断言接口返回状态是否为200,获取uticket
        """
        print(manager_login)

