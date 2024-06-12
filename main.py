from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from io import StringIO

import pandas as pd
from time import sleep

driver = webdriver.Chrome()

page_source = ""

def login(url,usernameId, username, passwordId, password, submit_buttonId, submit_buttonId2, link):
   driver.get(url)
   driver.find_element(By.ID, usernameId).send_keys(username)
   driver.find_element(By.ID, submit_buttonId).click()

   driver.find_element(By.ID,passwordId).send_keys(password)
   driver.find_element(By.ID,submit_buttonId2).click()
   
   driver.get("https://my.vntu.edu.ua/user/go/jetiq.cgi")
   #driver.get("https://iq.vntu.edu.ua/b04213/vspd/go2curriculum.php")
   driver.get("https://iq.vntu.edu.ua/b04213/curriculum/c_list.php?view=g&spring=1&group_id=7669&f_id=210")

   page_source = driver.page_source
   print(page_source)
   fileToWrite = open("page_source.html", "w", encoding='utf-8')
   fileToWrite.write(repr(page_source))
   fileToWrite.close()

if __name__ == '__main__':
   login("https://my.vntu.edu.uva/user/signin/", "user_field", '**-**-***', "pwd_field", '****', "do-verify-login", "do-verify-password", "app-id" )
   #pars()
   sleep(100)
   driver.quit()

