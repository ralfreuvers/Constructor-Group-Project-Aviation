from selenium import webdriver
import yaml
import json

conf = yaml.load(open('loginDetails.yml'))
fr24_email = conf['fr24_user']['email']
fr24_password = conf['fr24_user']['password']

driver = webdriver.Chrome()

def login(url,usernameId, username, passwordId, password, submit_buttonId):
   driver.get(url)
   driver.find_element_by_id(usernameId).send_keys(username)
   driver.find_element_by_id(passwordId).send_keys(password)
   driver.find_element_by_id(submit_buttonId).click()

login("https://www.flightradar24.com/user/signin", "email", fr24_email, "password", fr24_password, "login-submit-button")


