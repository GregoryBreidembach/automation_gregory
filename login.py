from selenium import webdriver
from page import PageObjectModel
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

# Llama la funcion de login
page.login("duncanryan", "L&#V5S;3L$)@")


# Cierra el navegador
time.sleep(3)
driver.quit()