from behave import when, then
from selenium.webdriver.common.by import By

@when('I click the "{button_text}" button')
def step_impl(context, button_text):
    button = context.browser.find_element(By.XPATH, f"//button[text()='{button_text}']")
    button.click()

@then('I should see "{text}" on the page')
def step_impl(context, text):
    assert text in context.browser.page_source

@then('I should not see "{text}" on the page')
def step_impl(context, text):
    assert text not in context.browser.page_source

@then('I should see a message "{message}"')
def step_impl(context, message):
    assert message in context.browser.page_source
