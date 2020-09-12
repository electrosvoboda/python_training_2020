from selenium import webdriver


def test_open_google(self):
    self.wd = webdriver.Firefox()

    self.wd.get("https://www.google.ru/")
    self.driver.set_window_size(1024, 768)
    self.wd.find_element_by_name("q").send_keys("jazz")
    self.wd.find_element_by_name("btnK").click()
    self.driver.quit()