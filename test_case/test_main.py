import pytest
import yaml

from page.app import APP
from test_case.test_base import TestBase


class TestMain(TestBase):
    @pytest.mark.parametrize('value1,value2',yaml.safe_load(open('./test_main.yaml')))
    def test_main(self,value1,value2):

        self.app.start().main().goto_serach()
        print(value1)
        print(value2)

