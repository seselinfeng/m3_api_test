from compose_test.src.api_test.api.login import Login
from compose_test.src.api_test.api.stock import Stock


class TestBase:
    def setup(self):
        self.stock = Stock()
        self.login = Login()
