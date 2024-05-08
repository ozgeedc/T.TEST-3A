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