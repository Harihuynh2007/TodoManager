import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta

class TestAddTask(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Edge()
        cls.driver.maximize_window()

    def test_add_task(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5500/login.html")

        # Đăng nhập vào hệ thống
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "emailSignin")))
        driver.find_element(By.ID, "emailSignin").send_keys("tanhaorn@gmail.com")
        driver.find_element(By.ID, "passwordSignin").send_keys("123456ae")
        
        login_button = driver.find_element(By.ID, "btn_signin")
        driver.execute_script("arguments[0].click();", login_button)

        # Kiểm tra đã đăng nhập thành công
        WebDriverWait(driver, 10).until(EC.url_contains("index.html"))

        # Chờ preloader biến mất
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, "preloader")))
        
        # Chờ trang index tải hoàn toàn
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "main-content")))
        WebDriverWait(driver, 10).until(EC.url_contains("index.html"))

        # Click vào nút '+' trên bảng "To do"
        add_task_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//i[@class='fas fa-plus board-header-icon' and @data-status='todo']"))
        )
        driver.execute_script("arguments[0].click();", add_task_button)
        
        # Chờ form mở hoàn toàn
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "add-task-content"))
        )
        
        # Nhập thông tin công việc
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "title"))).send_keys("Học Selenium")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "category"))).send_keys("Kiểm thử")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "description"))).send_keys("Làm bài tập kiểm thử tự động")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "due_date"))).send_keys("2025-02-26")
        
        # Sửa lỗi nhập ngày
        valid_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        due_date_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "due_date")))
        driver.execute_script("arguments[0].value = arguments[1];", due_date_input, valid_date)
        


        # Nhấn nút lưu công việc
        save_task_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn_add")))
        driver.execute_script("arguments[0].click();", save_task_button)

        # Kiểm tra công việc mới xuất hiện trong danh sách "To do"
        task_list = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Học Selenium')]")
        ))
        self.assertTrue(task_list)

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()

