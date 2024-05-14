#1)Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class Test_Sauce:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window() #ekranı büyütür
        self.driver.get("https://www.saucedemo.com/")

    def test_invalid_login(self):
        WebDriverWait(self.driver,15).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.ID,"user-name")
        username.send_keys()
        WebDriverWait(self.driver,15).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        password = self.driver.find_element(By.NAME,"password")
        password.send_keys()
        WebDriverWait(self.driver,15).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        expected_message = "Epic sadface: Username is required" # beklenen hata mesajı alanı 
        actual_message = self.driver.find_element(By.XPATH, "//div[contains(@class, 'error-message-container')]").text # sayfadaki hata mesajını yakalar ve actual_message adlı değişkende saklar.
        assert expected_message == actual_message, f"Expected: {expected_message}, Actual: {actual_message}" # bu kısımda Actual Mesajda sakladığı mesajı alır Expected mesaj ile karşılaştırır
        testResult = expected_message == "Epic sadface: Username is required"
        print(f"TEST SONUCU: {testResult}")

testClass = Test_Sauce()
testClass.test_invalid_login() 

#2)Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class Test_Sauce:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window() #ekranı büyütür
        self.driver.get("https://www.saucedemo.com/")

    def test_invalid_login(self):
        WebDriverWait(self.driver,15).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.ID,"user-name")
        username.send_keys("irembalci")
        WebDriverWait(self.driver,15).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        password = self.driver.find_element(By.NAME,"password")
        password.send_keys()
        WebDriverWait(self.driver,15).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        
        print(f"TEST SONUCU:  {testResult}")
       
testClass = Test_Sauce()
testClass.test_invalid_login()

#3)Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class Test_Sauce:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window() #ekranı büyütür
        self.driver.get("https://www.saucedemo.com/")

    def test_invalid_login(self):
        WebDriverWait(self.driver,15).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.ID,"user-name")
        username.send_keys("locked_out_user")
        WebDriverWait(self.driver,15).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        password = self.driver.find_element(By.NAME,"password")
        password.send_keys("secret_sauce")
        WebDriverWait(self.driver,15).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"TEST SONUCU:  {testResult}")
       
testClass = Test_Sauce()
testClass.test_invalid_login()

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

#Add to cart edip ürünün sepete eklendiğini kontrol etme 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Test_sepet_kontrol:
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

    def test_add_to_cart(self):
        add_to_cart_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        add_to_cart_button.click()

    def shopping_cart_container(self): 
        shopping_cart_container = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="shopping_cart_container"]/a')))
        shopping_cart_container.click()
        cart_items = self.driver.find_elements(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]')
        
        if cart_items:
            print("Ürün sepete başarıyla eklendi.")
        else:
            print("Ürün sepete eklenemedi.")

    def run_tests(self):
        self.test_valid_login("standard_user", "secret_sauce")
        self.test_add_to_cart()
        self.shopping_cart_container()
        sleep(10)

# Testleri çalıştırmak için
test = Test_sepet_kontrol()
test.run_tests()