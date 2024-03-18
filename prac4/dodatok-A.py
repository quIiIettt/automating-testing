from selenium import webdriver  # Імпорт класу webdriver з бібліотеки Selenium
from selenium.webdriver.common.by import By  # Імпорт класу By з пакету webdriver.common.by

link = "https://chmnu.edu.ua/"  # Встановлення URL-адреси для тестування

browser = webdriver.Chrome()  # Створення нового екземпляру браузера Google Chrome
browser.get(link)  # Відкриття веб-сторінки у відкритому браузері
button = browser.find_element(By.ID, "s")  # Пошук елемента на веб-сторінці за ID
button.click()  # Клік по знайденому елементу

# Закриваємо браузер після всіх маніпуляцій
browser.quit()
