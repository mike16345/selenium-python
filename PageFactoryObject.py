from seleniumpagefactory.Pagefactory import PageFactory


class PageClass(PageFactory):
    def __init__(self, driver, wait, action):
        super().__init__()
        self.driver = driver
        self.wait = wait
        self.action = action
