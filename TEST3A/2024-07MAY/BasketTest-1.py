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