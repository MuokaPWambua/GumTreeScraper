class FirefoxDriverHelper:
    
    def __init__(self):
        self.driver = None

    def initialize_driver(self):
        options = FirefoxOptions()
        options.headless = True
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--window-size=1280,800")
        
        self.driver = webdriver.Firefox(options=options)
        self.driver.implicitly_wait(30)

    def cleanup_driver(self):
        try:
            if self.driver:
                self.driver.quit()
                self.driver = None
        except:
            pass
            
    def __enter__(self):
        self.initialize_driver()
        return self.driver

    def __exit__(self, exc_type, exc_value, traceback):
        self.cleanup_driver()
