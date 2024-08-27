from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import pytesseract
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = 'D:\\USERS\\05056434132\\Downloads\\chromedriver_win32 (1)'
service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service)


# Abrir o reCAPTCHA Demo do Google
driver.get("https://www.google.com/recaptcha/api2/demo")

# Esperar até que o captcha seja carregado
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[src^='https://www.google.com/recaptcha/api2/anchor']")))

# Localizar e clicar no botão "I'm not a robot"
driver.find_element(By.ID, "rc-anchor-container").click()

# Voltar para o frame principal
driver.switch_to.default_content()

# Esperar até que a janela de desafio do captcha seja aberta
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[src^='https://www.google.com/recaptcha/api2/bframe']")))

# Localizar e obter a imagem do captcha
captcha_image_element = driver.find_element(By.CSS_SELECTOR, "img[src^='https://www.google.com/recaptcha/api2/payload']")
captcha_image_url = captcha_image_element.get_attribute("src")
response = webdriver.requests.get(captcha_image_url, stream=True)
captcha_image = Image.open(response.raw)

# Pré-processamento da imagem
captcha_image = captcha_image.convert("L")  # Converter para escala de cinza
captcha_image = captcha_image.point(lambda x: 0 if x < 128 else 255)  # Limiarização

# Reconhecimento do texto
captcha_text = pytesseract.image_to_string(captcha_image)

# Preencher o texto do captcha
driver.switch_to.default_content()
driver.find_element(By.ID, "rc-anchor-container").send_keys(captcha_text)

# Enviar o formulário
driver.find_element(By.ID, "recaptcha-demo-submit").click()

# Esperar até que a resposta seja exibida
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "rc-message-success")))

# Fechar o navegador
driver.quit()
