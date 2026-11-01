import random
import string

COHORT_NUMBER = "54"      
DOMAIN = "yandex.ru"     

def generate_email():
    name = ''.join(random.choices(string.ascii_lowercase, k=6))
    surname = ''.join(random.choices(string.ascii_lowercase, k=7))

    three_digits = ''.join(random.choices(string.digits, k=3))

    return f"{name}_{surname}_{COHORT_NUMBER}_{three_digits}@{DOMAIN}"


def generate_password(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))
