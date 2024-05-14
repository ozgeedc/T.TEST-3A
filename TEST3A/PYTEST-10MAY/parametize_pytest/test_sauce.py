#1) Başarılı giriş yaptıktan sonra sepete ekleyip satın alma işlemini tamamlar.
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


# Parametrize fonksiyonu ile 3 farklı veriyle test

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class test_SauceDemo:
    def setup_method(self):
        # her test başlangıcında çalışacak fonksiyon
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

    def teardown_method(self):
        # her test bitiminde çalışacak fonksiyon
        self.driver.quit()

    @pytest.mark.parametrize("credentials", [
        {"username": "standard_user", "password": "secret_sauce", "expected_success": True, "error_message": ""},
        {"username": "locked_out_user", "password": "secret_sauce", "expected_success": False, "error_message": "Epic sadface: Sorry, this user has been locked out."},
        {"username": "deneme_test", "password": "secret_sauce", "expected_success": False, "error_message": "Epic sadface: Username and password do not match any user in this service"},
    ])
    def test_paramatize_login(self, credentials):
        usernameInput = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "user-name")))
        usernameInput.send_keys(credentials["username"])
        passwordInput = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "password")))
        passwordInput.send_keys(credentials["password"])
        loginButton = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "login-button")))
        loginButton.click()

        # Başarılı veya başarısız giriş durumunu kontrol et
        if credentials["expected_success"]:
            assert "inventory.html" in self.driver.current_url
            print(f"{credentials['username']} kullanıcısı başarıyla giriş yaptı.")
        else:
            # Hata mesajını kontrol et ve doğru mesajı yazdır
            error_message_element = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')))
            assert error_message_element.text == credentials["error_message"]
            print(f"{credentials['username']} kullanıcısı giriş yapamadı. Hata Mesajı: {credentials['error_message']}")

if __name__ == "__main__":
    pytest.main(["-v", "--html=report.html"])

