from selenium import webdriver

class Driver:
    def set_up_driver(self, headless=True):
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--window-size=800,800')
        return webdriver.Chrome(options=options)