from selenium import webdriver
from selenium.webdriver.common.by import By


class Make:
    def __init__(self, driver):
        self.driver = driver

    def click_on_add_make_button(self, driver):
        self.driver.find_element(By.XPATH, "//div[@ngbtooltip='Add Make']").click()

    def enter_make(self, driver, make):
        self.driver.find_element(By.XPATH, "//input[@formcontrolname='make_name']").send_keys("make")

    def click_on_save_button(self, driver):
        self.driver.find_element(By.XPATH, "//button[text() = 'Save']").click()

    def verify_error_message_of_make_field(self, driver):
        actual_message = self.driver.find_element(By.XPATH, "//input[@formcontrolname='make_name']/following::span").text
        expected_message = 'This field is required.'
        assert actual_message.__eq__(expected_message)

    def click_on_cancel_button(self, driver):
        self.driver.find_element(By.XPATH, "//button[text() = 'Cancel']").click()
