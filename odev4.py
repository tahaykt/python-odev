from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class TestSauce:           #test girişi login sayfasında username girilince yanlış girilirse epic sadface username is required hatasını yazdırır altına test sonucunu yazdırır
    def test_null_login(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        input()
        sleep(3)
        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(2)
        errorMessage = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage == "Epic sadface: Username is required"
        print(f"TEST SONUCU: {testResult}")

    def test_null_password(self):      #gene aynı işlemler bu sefer şifre için yapılır
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(10)
        usernameInput = driver.find_element(By.ID, "user-name")
        sleep(10)
        usernameInput.send_keys("1")
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage == "Epic sadface: Password is required"
        print(f"TEST SONUCU: {testResult}")
    
    def test_username_password(self):     #aynı işlemler bu sefer hem username hemde şifre için sorgulanır şifre için locket_out_user,şifre için secret_user girilip butona basılır eğer yanlışsa Epic sadface: Sorry, this user has been locked out hatasını gönderir
                                          
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput = driver.find_element(By.ID,"login-button")
        passwordInput = driver.find_element(By.ID,"user_name")
        sleep(2)
        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        sleep(2)
        errorMessage = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage == "Epic sadface: Sorry, this user has been locked out."
        print(f"TEST SONUCU: {testResult}")
    
    def show_error_icon_test(self):    #yanlış girdi yaparsak kırmızı renkte X işareti çıkar ona dokununca hata yazısı kalkması işlemi
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        errorIcon = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        sleep(2)
        errorIcon.click()

    def login_standard_user(self):      # kullanıcı adına secret_user şifre yerine secret_sauce yazıp gonderince inventory.html sayfasına gönderir
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        usernameInput = driver.find_element(By.ID,"login-button")
        passwordInput = driver.find_element(By.ID,"user_name")
        sleep(5)
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep()
        loginBtn = driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        sleep(2)
        self.driver.get("https://www.saucedemo.com/inventory.html")
        sleep(2)

    def show_product_count(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput = driver.find_element(By.ID,"login-button")
        usernameInput.click()
        sleep(2)
        usernameInput.send_keys("standard_user")
        passwordInput = driver.find_element(By.ID,"user_name")
        passwordInput.click()
        passwordInput.send_keys("secret_sauce")
       
        loginBtn = driver.find_element(By.ID,"login-button")    #invertory.html e girincede kullanıcıya gösterilen ürün sayısı 6 adet olması işlemleri
        sleep(2)
        loginBtn.click()
        sleep(2)
        self.driver.get("https://www.saucedemo.com/inventory.html")
        sleep(2)
        productList = driver.find_elements(By.CLASS_NAME,"inventory_item")
        if (productList.__len__()== 6):
            print(f"Product count equal to 6 : {True}")
        else:
            print(f"Product count equal to 6 : {False}")
            


test1 = TestSauce()


test1.test_null_login()
test1.test_null_password()
test1.test_username_password()
test1.show_error_icon_test()
test1.login_standard_user()
test1.show_product_count()


while True:
    continue
