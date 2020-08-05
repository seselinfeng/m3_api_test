from api.login import Login
from api.stock import Stock


class TestBase:
    def setup(self):
        self.stock = Stock()
        self.login = Login()
