from compose_test.src.api_test.api import Login
from compose_test.src.api_test.api import Stock


class TestBase:
    def setup(self):
        self.stock = Stock()
        self.login = Login()
