from page.app import APP


class TestBase:
    app =None
    def setup(self):
        self.app =APP()