
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Task 7a: Button Click
@when('I click the button "{button_name}"')
def step_click_button(context, button_name):
    button = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, f"//button[normalize-space()='{button_name}']")
        )
    )
    button.click()


# Task 7b: Verify specific text is present
@then('I should see "{text}"')
def step_verify_text_present(context, text):
    page_text = context.browser.find_element(
        By.TAG_NAME, "body"
    ).text

    assert text in page_text, (
        f"Expected text '{text}' was not found"
    )


# Task 7c: Verify specific text is NOT present
@then('I should not see "{text}"')
def step_verify_text_not_present(context, text):
    page_text = context.browser.find_element(
        By.TAG_NAME, "body"
    ).text

    assert text not in page_text, (
        f"Unexpected text '{text}' was found"
    )


# Task 7d: Verify a specific message is present
@then('I should see the message "{message}"')
def step_verify_message(context, message):
    page_text = context.browser.find_element(
        By.TAG_NAME, "body"
    ).text

    assert message in page_text, (
        f"Message '{message}' was not displayed"
    )
