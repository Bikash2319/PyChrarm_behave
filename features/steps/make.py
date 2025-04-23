from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

@given(u'Navigate to Make module')
def navigate_to_make(context):
    context.driver.get("https://release.gensom.sharajman.com/make")


@when(u'User click on Add Make button')
def add_new_make_button(context):
    make_button = context.wait.until(ec.element_to_be_clickable\
                                         ((By.XPATH, "//div[@ngbtooltip='Add Make']")))
    make_button.click()


@when(u'Enter new make details')
def enter_make(context):
    context.driver.find_element(By.XPATH, "//input[@formcontrolname='make_name']")\
        .send_keys("Test Make")


@then(u'Click on Save button')
def click_save_button(context):
    context.driver.find_element(By.XPATH, "//button[text()='Save']").click()

@when(u'user entered special characters and numbers in input field')
def enter_invalid_characters(context):
    context.driver.find_element(By.XPATH, "//input[@formcontrolname='make_name']")\
        .send_keys("!@#$!@#4123456")

@then(u'Click on Save button and user should prompted to enter valid characters')
def validate_error_message_of_input_field(context):
    input_error = context.driver.find_element\
        (By.XPATH, "//div[contains(@class, 'cst-input-error')]//small[text()=' Only alphanumeric characters are allowed. ']")
    error_message = input_error.text

    assert error_message == 'Only alphanumeric characters are allowed. ', "Incorrect error message is displaying under the make input field."