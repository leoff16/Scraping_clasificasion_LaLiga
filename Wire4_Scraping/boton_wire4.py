from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import credenciales

# Inicializar el navegador Chrome con el controlador
driver = webdriver.Chrome()


# Navega a la página de inicio de sesión
login_url = 'https://app.wire4.mx/#/login'
driver.get(login_url)

#time.sleep(5)

# Rellena el formulario de inicio de sesión
username = credenciales.USER
password = credenciales.PASSWD

wait = WebDriverWait(driver, 10)

# Encuentra los campos de entrada de usuario 
text_field = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-public-layout/main/div[2]/app-login/div/form/div[1]/div/div/input')))

# Llenar el campo de Usuario
text_field.send_keys(username)

# Encuentra los campos de entrada de contraseña
text_field = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-public-layout/main/div[2]/app-login/div/form/div[2]/div/div/input')))

# Llenar el campo de Contraseña
text_field.send_keys(password)


# Hacer click en el boton de Iniciar Sesion
boton = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-public-layout/main/div[2]/app-login/div/form/div[4]/div/button[2]"))).click()

time.sleep(5)

webhook_url = 'https://app.wire4.mx/#/webhooks/management'

driver.get(webhook_url)

time.sleep(5)

boton_activacion = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-private-layout/main/div[2]/app-webhooks-management/div[2]/div/div/div/div/div[3]/div[1]/label[1]"))).text


if boton_activacion == 'Inactivo':
    # Hacer click en activar
    boton_activacion = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-private-layout/main/div[2]/app-webhooks-management/div[2]/div/div/div/div/div[3]/div[1]/label[2]/span"))).click()


time.sleep(3)

# Click en boton para luego dar click en salir
wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-private-layout/app-header/ul/li[2]/a"))).click()

time.sleep(3)

# Click en boton para cerrar sesion
wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-private-layout/app-header/ul/li[2]/div/a[3]/div"))).click()


time.sleep(5)


