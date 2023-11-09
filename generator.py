from faker import Faker
import random
import string
import secrets

fake = Faker()

# Función que genera nombres de usuarios aleatorios
def username_random():
    return fake.user_name()

# Función que genera contraseñas aleatorias
def password_random():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(caracteres) for i in range(12))
    return password

# Función que genera los numeros de telefono
def phone_number_random():
    area_code = "131"
    seven_digits_random = ''.join([str(random.randint(0, 9)) for _ in range(7)])
    phone_number = area_code + seven_digits_random
    return phone_number
