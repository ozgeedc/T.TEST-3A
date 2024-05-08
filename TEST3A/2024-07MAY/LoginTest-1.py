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