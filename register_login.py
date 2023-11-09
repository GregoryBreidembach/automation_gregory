from selenium import webdriver
from page import PageObjectModel
from generator import password_random, username_random
import time

# Inicializa el navegador
driver = webdriver.Chrome()
# Maximiza la ventana del navegador
driver.maximize_window()
# Navega a la URL
driver.get("https://www.demoblaze.com/index.html")
time.sleep(3)

# Crear una instacia de la clase page
page = PageObjectModel(driver)

# Generar los datos aleatorios del registro
user = username_random()
password = password_random()
print(f"Usuario: {user} \nContraseña: {password}")

# Llama la funcion de register
page.register(user, password)

time.sleep(2)

# Llama la funcion que login
page.login(user, password)

# Cierra el navegador
time.sleep(3)
driver.quit()