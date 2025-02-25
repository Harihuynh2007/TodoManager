import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Edge()
        cls.driver.maximize_window()

    def test_login_success(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5500/login.html")

        # Đợi trang load hoàn toàn
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "emailSignin")))

        # Nhập thông tin đăng nhập
        driver.find_element(By.ID, "emailSignin").send_keys("tanhaorn@gmail.com")
        driver.find_element(By.ID, "passwordSignin").send_keys("123456ae")

        # Đợi preloader biến mất nếu có
        WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.ID, "preloader")))

        # Click nút đăng nhập
        login_button = driver.find_element(By.ID, "btn_signin")
        driver.execute_script("arguments[0].click();", login_button)

        # Kiểm tra đăng nhập thành công
        WebDriverWait(driver, 10).until(EC.title_contains("TodoManager"))

        self.assertIn("TodoManager", driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
