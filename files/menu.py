from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def language():
    print("\033[95m[+]\033[0m Choose your prefer language for random quotes")
    print()
    print("\033[95m[+]\033[0m 1 - English")
    print("\033[95m[+]\033[0m 2 - Portuguese-BR")
    print()
    choice = str(input("\033[95m[+]\033[0m Language: "))
    if choice == '1':
        return 'english'
    elif choice == '2':
        return 'pt-br'
    else:
        print("\033[95m[+]\033[0m Invalid choice. Defaulting to English.")
        return 'english'

def get_quote():
    while True:
        random = False
        check = input('\033[95m[+]\033[0m Do you want to use random quotes? (y or n): ').lower()
        if check == 'y':
            random = True
            return random
        elif check == 'n':
            quote = input('\033[95m[+]\033[0m Enter the quote to be spammed: ')
            return quote
        else:
            print("\033[95m[+]\033[0m Invalid input. Please enter 'y' or 'n'.")

def get_info():
    username = str(input('\033[95m[+]\033[0m Enter username: '))
    return username

def get_id(username):
    url = 'https://ngl.link/' + username
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options=options)
    try:
        print("\033[95m[+]\033[0m Getting deviceId...")
        driver.get(url)
        wait = WebDriverWait(driver, 2)
        input_deviceId = wait.until(EC.presence_of_element_located((By.ID, 'deviceId')))
        deviceId = input_deviceId.get_attribute('value')
        return deviceId
    finally:
        driver.quit()
