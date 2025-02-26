import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginFail(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Edge()
        cls.driver.maximize_window()

    def test_login_wrong_password(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5500/login.html")

        # Đợi trang load hoàn toàn
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "emailSignin")))

        # Nhập email đúng nhưng mật khẩu sai
        driver.find_element(By.ID, "emailSignin").send_keys("tanhaorn@gmail.com")
        driver.find_element(By.ID, "passwordSignin").send_keys("wrongpassword")

        # Click nút đăng nhập
        login_button = driver.find_element(By.ID, "btn_signin")
        driver.execute_script("arguments[0].click();", login_button)

        # Chờ thông báo lỗi xuất hiện
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Sai tên đăng nhập hoặc mật khẩu')]")
        ))
        self.assertEqual(error_message.text, "Sai tên đăng nhập hoặc mật khẩu")

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
