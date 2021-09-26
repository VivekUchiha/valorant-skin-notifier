from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
from mailer import send_mail

username = ''
password = ''

# Choose between {na, sa, eu, ap, kr}
account_region = 'ap'

# You will recieve mail to this id. Leave it empty if you just use it to check skins and not recieve mails.
email = ''

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)
driver.get("https://www.valorant.store/")
accept_cookies = driver.find_element_by_class_name('Gdpr_button__1XnYI')
accept_cookies.click()
login_button = driver.find_element_by_class_name('Button_redWhite__2cXfi')
login_button.click()

username_input = driver.find_element_by_name('username')
password_input = driver.find_element_by_name('password')
username_input.send_keys(username)
password_input.send_keys(password)

region_selector = driver.find_element_by_class_name('Region_select__1h_yh')
region_selector.click()

region = driver.find_element_by_xpath(f"//li[@data-value='{account_region}']")
region.click()

login_button = driver.find_element_by_class_name('Login_loginButton__28vTJ')
login_button.click()

result = WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.CLASS_NAME, "SkinsDaily_info__Imx7r")))

skins = driver.find_elements_by_class_name('SkinsDaily_info__Imx7r')
mail_body = ''
for skin in skins:
    print(skin.text)
    mail_body += skin.text
    mail_body += '\n'

driver.close()
if email != '':
    send_mail(mail_body, email)

