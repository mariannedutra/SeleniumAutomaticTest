from selenium import webdriver

def before_all(context):
    context.driver = webdriver.Chrome()
def after_all(context):
    # Fecha o navegador após todos os testes
    context.driver.quit()
