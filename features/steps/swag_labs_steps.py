from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given('que o usuário acessa a página de login do SauceDemo')
def step_user_on_login_page(context):
    context.driver.get('https://www.saucedemo.com/')
    time.sleep(2)

@when('o usuário faz login com o nome de usuário "{username}" e a senha "secret_sauce"')
def step_user_logs_in(context, username):
    context.driver.find_element(By.ID, 'user-name').send_keys(username)
    context.driver.find_element(By.ID, 'password').send_keys("secret_sauce")
    context.driver.find_element(By.ID, 'login-button').click()
    time.sleep(2)

@when('o usuário adiciona "Sauce Labs Fleece Jacket" ao carrinho')
def step_user_adds_item_to_cart(context):
    jacket = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[text()="Sauce Labs Fleece Jacket"]/ancestor::div[@class="inventory_item"]//button'))
    )
    jacket.click()
    time.sleep(1)

@when('o usuário vai para o carrinho')
def step_user_goes_to_cart(context):
    context.driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    time.sleep(1)

@when('o usuário inicia o processo de checkout')
def step_user_begins_checkout(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'checkout'))
    ).click()

@when('o usuário preenche as informações de checkout com nome "{first_name}", sobrenome "{last_name}" e CEP "{postal_code}"')
def step_user_fills_checkout_info(context, first_name, last_name, postal_code):
    context.driver.find_element(By.ID, 'first-name').send_keys(first_name)
    context.driver.find_element(By.ID, 'last-name').send_keys(last_name)
    context.driver.find_element(By.ID, 'postal-code').send_keys(postal_code)
    context.driver.find_element(By.ID, 'continue').click()

@when('o usuário finaliza o pedido')
def step_user_completes_order(context):
    finish_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'finish'))
    )
    finish_button.click()

@then('a página de confirmação de pedido deve ser exibida')
def step_order_confirmation_page(context):
    confirmation_message = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'complete-header'))
    )
    actual_text = confirmation_message.text
    print(f"Texto da confirmação encontrado: {actual_text}")
    assert actual_text == "Thank you for your order!", f"O pedido não foi finalizado com sucesso: '{actual_text}'"
