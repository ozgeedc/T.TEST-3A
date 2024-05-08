#4)Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir. 
#Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
    
    def test_valid_login(self, username, password):
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name")))
        username_field.send_keys(username)
        
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))
        password_field.send_keys(password)
        
        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "login-button")))
        login_button.click()
        
        inventory_page_title = WebDriverWait(self.driver, 10).until(EC.title_contains("Swag Labs"))
        assert "inventory.html" in self.driver.current_url
        print("entry success.")
    
    def check_product_count(self):
        product_count = len(self.driver.find_elements(By.CLASS_NAME, "inventory_item"))
        assert product_count == 6
        print(f"product count: {product_count} product listed")
    
    def run_tests(self):
        self.test_valid_login("standard_user", "secret_sauce")
        self.check_product_count()
        self.driver.quit()

# Testleri çalıştırmak için:
test = TestLogin()
test.run_tests()

