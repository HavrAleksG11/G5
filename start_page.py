import logging
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestStartPage:
    log = logging.getLogger("[Start Page]")

    def test_incorrect_login(self):
        # Create driver
        driver = webdriver.Chrome()

        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # Fill login
        login = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login.send_keys("User11")
        sleep(1)

        # Fill password
        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.send_keys("Psw11")
        sleep(1)

        # Click button
        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        button.click()
        sleep(1)

        # Verify error
        error_element = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        assert error_element.text == "Invalid username / pasword", f"Actual message: {error_element.text}"

        # Close driver
        driver.close()

    def test_register_done(self):
        driver = webdriver.Chrome()

        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        login = driver.find_element(by=By.XPATH, value=".//input [@placeholder='Pick a username']")
        login.send_keys("Vas")
        sleep(1)

        email = driver.find_element(by=By.XPATH, value=".//input [@placeholder='you@example.com']")
        email.send_keys("12345@gmail.com")
        sleep(1)

        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Create a password']")
        password.send_keys("12345678910111213")
        sleep(1)

        button = driver.find_element(by=By.XPATH, value=".//button[@type='submit']")
        button.click()
        sleep(1)
        self.log.info(driver.current_url)
        driver.close()

    def test_login_done(self):
        driver = webdriver.Chrome()
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        login = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login.send_keys("Vas")
        sleep(1)

        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.send_keys("12345678910111213")
        sleep(1)
        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        button.click()
        sleep(1)
        self.log.info(driver.current_url)
        driver.close()

    def test_profile(self):
        driver = webdriver.Chrome()

        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        login = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login.send_keys("Vas")
        sleep(1)

        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.send_keys("12345678910111213")
        sleep(1)

        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        button.click()
        sleep(1)

        profile_button = driver.find_element(by=By.XPATH, value=".//html/body/header/div/div/a[2]/img")
        profile_button.click()
        sleep(1)
        self.log.info(driver.current_url)
        driver.close()

    # Пробний тест)
    def test_new_post(self):
        driver = webdriver.Chrome()
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        login = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login.send_keys("Vas")
        sleep(1)

        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.send_keys("12345678910111213")
        sleep(1)

        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        button.click()
        sleep(1)

        profile_button = driver.find_element(by=By.XPATH, value=".//html/body/header/div/div/a[2]/img")
        profile_button.click()
        sleep(1)

        create_post = driver.find_element(by=By.XPATH, value=".//html/body/header/div/div/a[3]")
        create_post.click()
        sleep(1)

        title = driver.find_element(by=By.XPATH,
                                    value=".//input[@class='form-control form-control-lg form-control-title']")
        title.send_keys("Test Title")
        sleep(1)

        body_text = driver.find_element(by=By.XPATH,
                                        value=".//textarea[@class= 'body-content tall-textarea form-control']")
        body_text.send_keys("Hello World")
        sleep(1)

        button = driver.find_element(by=By.XPATH, value=".//button[@class= 'btn btn-primary']")
        button.click()
        sleep(1)

        self.log.info(driver.current_url)

        driver.close()
