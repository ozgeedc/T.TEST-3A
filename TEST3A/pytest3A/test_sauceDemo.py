

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.support import expected_conditions as EC



class Test_sauceDemo:
    def setup_method(self): 
        # peş peşe testlerde, her test öncesi çalışacak fonksiyon
        self.driver = webdriver.Chrome()
        self.driver.maximize_window() 
        self.driver.get("https://www.saucedemo.com/")

    def teardown_method(self):  
        # her test bitiminde çalılacak fonksiyon.
        self.driver.quit()   
        
    def test_invalid_login(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.ID,"user-name")
        username.send_keys("1") #kullanıcı adı yanlış 
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        password = self.driver.find_element(By.NAME,"password")
        password.send_keys("1") #şifre yanlış
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"

    def test_two_invalid_login(self): 
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.ID,"user-name")
        username.send_keys("standard_user") #kullanıcı adı doğru 
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        password = self.driver.find_element(By.NAME,"password")
        password.send_keys("1")# sifre yanlış
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"   

    def test_three_invalid_login(self): 
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.ID,"user-name")
        username.send_keys("yanlis") #kullanıcı adı yanlış 
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        password = self.driver.find_element(By.NAME,"password")
        password.send_keys("secret_sauc")# sifre doğru
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"


# Kullanıcının zorunlu alanları boş geçmesi 
    def test_four_invalid_login(self): 
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.ID,"user-name")
        username.send_keys() #kullanıcı adı boş
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        password = self.driver.find_element(By.NAME,"password")
        password.send_keys()# sifre boş
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text == "Epic sadface: Username is required"         

#Başarılı giriş

    def test_valid_login(self):
       
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.ID,"user-name")
        username.send_keys("standard_user")   
      
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        password = self.driver.find_element(By.NAME,"password")
        password.send_keys("secret_sauce") 
    
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID,"login-button")
       
        loginButton.click()
        appLogo = self.driver.find_element(By.CLASS_NAME,"app_logo")
        assert appLogo.text == "Swag Labs" 

   # kulanıcının blokeli hesapla giriş yapması 
    def test_locked_login(self):
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
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out." 


    # Kullanıcı giriş yaptıktan sonra Liste ekranına yönlendirilmesi    

    def test_list_login(self):
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name")))
        username_field.send_keys("standard_user")
        
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))
        password_field.send_keys("secret_sauce")
        
        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "login-button")))
        login_button.click()
        
        inventory_page_title = WebDriverWait(self.driver, 10).until(EC.title_contains("Swag Labs"))
        assert "inventory.html" in self.driver.current_url
        print("entry success.")
    
    def check_product_count(self):
        product_count = len(self.driver.find_elements(By.CLASS_NAME, "inventory_item"))
        assert product_count == 6
        print(f"product count: {product_count} product listed")

   #Add to cart edip ürünün sepete eklendiğini kontrol etme          
   
    def test_baskets_login(self):
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name")))
        username_field.send_keys("standard_user")
        
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))
        password_field.send_keys("secret_sauce")
        
        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "login-button")))
        login_button.click()

        add_to_cart_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        add_to_cart_button.click()

        shopping_cart_container = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="shopping_cart_container"]/a')))
        shopping_cart_container.click()
        cart_items = self.driver.find_elements(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]')
        
        if cart_items:
            print("Ürün sepete başarıyla eklendi.")
        else:
            print("Ürün sepete eklenemedi.") 

# ürünün sipariş verilmesi 

    def test_order_login(self):
        username = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "user-name")))
        username.send_keys("standard_user")
        password = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "password")))
        password.send_keys("secret_sauce")
        loginButton = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "login-button")))
        loginButton.click()
    
    #test_add_to_cart:
        
        add_to_cart_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        add_to_cart_button.click()
        go_to_basket = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="shopping_cart_container"]/a')))
        go_to_basket.click()
        checkout_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout"]')))
        checkout_button.click()

    #test_checkout_information:
        first_name = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "first-name")))
        first_name.send_keys("Furkan")
        last_name = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "last-name")))
        last_name.send_keys("Gümüşkaya")
        postal_code = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "postal-code")))
        postal_code.send_keys("34250")
        continue_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="continue"]')))
        continue_button.click()

   # test_finish_shopping:
        finish_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="finish"]')))
        finish_button.click()
        thank_you_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_complete_container"]/h2')))
        assert thank_you_message.text == "Thank you for your order!"
                      
     
          

