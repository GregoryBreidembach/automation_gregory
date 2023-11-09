from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class PageObjectModel:
    
    def __init__(self, driver):
        self.driver = driver
        
        # Selectors navbar 
        self.signup_link = (By.ID, "signin2")
        self.login_link = (By.ID, "login2")
        # Selectors sign up modal
        self.modal_signup = (By.XPATH, "//div[h5[text()='Sign up']]")
        self.modal_signup_user = (By.ID, "sign-username")
        self.modal_signup_password = (By.ID, "sign-password")
        self.modal_signup_button = (By.XPATH, "//button[@onclick='register()']")
        # Selectors Log In modal
        self.modal_login = (By.XPATH, "//div[h5[text()='Log in']]")
        self.modal_login_user = (By.ID, "loginusername")
        self.modal_login_password = (By.ID, "loginpassword")
        self.modal_login_button = (By.XPATH, "//button[@onclick='logIn()']")
        self.user_logged = (By.ID, "nameofuser")
    
    def is_element_clickable(self, by, value, timeout):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((by, value))
            )
            return True
        except Exception:
            return False
        
    def is_element_visible(self, by, value, timeout):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
            return True
        except Exception:
            return False
        
    def register(self, user, password):

        # Hacer click en sign up
        if self.is_element_clickable(*self.signup_link, 10):
            self.driver.find_element(*self.signup_link).click()
        else:
            self.driver.save_screenshot('C:/automation_gregory/screenshots/ERROR_EN_REGISTRO.png')
            assert False, "Error en el registro: No se encontró el link de 'Sign Up' o no esta habilitado"

        # Esperar a que aparezca el modal de sign up
        if self.is_element_visible(*self.modal_signup, 15):
            pass
        else:
            self.driver.save_screenshot('C:/automation_gregory/screenshots/ERROR_EN_REGISTRO.png')
            assert False, "Error en el registro: No se encontró el modal de 'Sign Up'"

        # Ingresar el user aleatorio
        if self.is_element_clickable(*self.modal_signup_user, 10):
            self.driver.find_element(*self.modal_signup_user).send_keys(user)
        else:
            self.driver.save_screenshot('C:/automation_gregory/screenshots/ERROR_EN_REGISTRO.png')
            assert False, "Error en el registro: No se encontró el campo de user o no esta habilitado"

        # Ingresar el password aleatorio
        if self.is_element_clickable(*self.modal_signup_password, 10):
            self.driver.find_element(*self.modal_signup_password).send_keys(password)
        else:
            self.driver.save_screenshot('C:/automation_gregory/screenshots/ERROR_EN_REGISTRO.png')
            assert False, "Error en el registro: No se encontró el campo de password o no esta habilitado"

        # Hacer click en el botón de sign up
        if self.is_element_clickable(*self.modal_signup_button, 10):
            self.driver.find_element(*self.modal_signup_button).click()
        else:
            self.driver.save_screenshot('C:/automation_gregory/screenshots/ERROR_EN_REGISTRO.png')
            assert False, "Error en el registro: No se encontró el boton de sign up o no esta habilitado"

        # Cerrar la ventana de exito
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()  # Acepta la alerta (cierra la ventana)
        except Exception:
            assert False, "Error en el registro: No se encontró la ventana de exito esperada"
        
    def login(self, user, password):

        # Hacer click en login
        if self.is_element_clickable(*self.login_link, 10):
            self.driver.find_element(*self.login_link).click()
        else:
            self.driver.save_screenshot('C:/automation_gregory/screenshots/ERROR_EN_LOGIN.png')
            assert False, "Error en el login: No se encontró el link de 'Log In' o no esta habilitado"

        # Esperar a que aparezca el modal de login
        if self.is_element_visible(*self.modal_login, 15):
            pass
        else:
            self.driver.save_screenshot('C:/automation_gregory/screenshots/ERROR_EN_LOGIN.png')
            assert False, "Error en el login: No se encontró el modal de login"

        # Ingresar el user
        if self.is_element_clickable(*self.modal_login_user, 10):
            self.driver.find_element(*self.modal_login_user).send_keys(user)
        else:
            self.driver.save_screenshot('C:/automation_gregory/screenshots/ERROR_EN_LOGIN.png')
            assert False, "Error en el login: No se encontró el campo de user o no esta habilitado"

        # Ingresar el password
        if self.is_element_clickable(*self.modal_login_password, 10):
            self.driver.find_element(*self.modal_login_password).send_keys(password)
        else:
            self.driver.save_screenshot('C:/automation_gregory/screenshots/ERROR_EN_LOGIN.png')
            assert False, "Error en el login: No se encontró el campo de password o no esta habilitado"

        # Hacer click en el botón de login
        if self.is_element_clickable(*self.modal_login_button, 10):
            self.driver.find_element(*self.modal_login_button).click()
        else:
            self.driver.save_screenshot('C:/automation_gregory/screenshots/ERROR_EN_LOGIN.png')
            assert False, "Error en el login: No se encontró el boton de login o no esta habilitado"

        # Verificar que el mensaje de bienvenida en el navbar coincida con el usuario logueado
        if self.is_element_visible(*self.user_logged, 15):
            nameuser = self.driver.find_element(*self.user_logged)
            if f'Welcome {user}' in nameuser.text:
                pass
            else:
                assert False, f"Error en el login: el nombre mostrado en el navbar, {nameuser.text} no coincide con el usuario ingresado {user}"
        else:
            assert False, "Error en el login: No se encontró el mensaje de bienvenida del usuario"