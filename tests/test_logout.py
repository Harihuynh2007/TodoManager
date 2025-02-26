import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogout(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Edge()
        cls.driver.maximize_window()

    def test_logout_success(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5500/login.html")

        # Đăng nhập trước
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "emailSignin")))
        driver.find_element(By.ID, "emailSignin").send_keys("tanhaorn@gmail.com")
        driver.find_element(By.ID, "passwordSignin").send_keys("123456ae")
        
        login_button = driver.find_element(By.ID, "btn_signin")
        driver.execute_script("arguments[0].click();", login_button)

        # Kiểm tra đã đăng nhập thành công
        WebDriverWait(driver, 10).until(EC.url_contains("index.html"))
        
        # Chờ preloader biến mất nếu có
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, "preloader")))
        
        # Tìm và click vào nút đăng xuất
        logout_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "btn_signout"))
        )
        driver.execute_script("arguments[0].click();", logout_button)
        
        # Kiểm tra đã quay lại trang đăng nhập bằng sự xuất hiện của emailSignin
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "emailSignin"))
        )
        
        self.assertTrue(driver.find_element(By.ID, "emailSignin"))

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
