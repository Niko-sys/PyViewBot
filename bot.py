import selenium
import time
import config
from selenium import webdriver
from time import sleep
from config import path,url1,url2,url3,url4

driver1 = webdriver.Chrome(executable_path="path")
driver2 = webdriver.Chrome(executable_path="path")
driver3 = webdriver.Chrome(executable_path="path")
driver4 = webdriver.Chrome(executable_path="path")

driver1.get("url1")
driver2.get("url2")
driver3.get("url3")
driver4.get("url4")
 
while True:
    sleep(10)
    driver1.refresh()
    driver2.refresh()
    driver3.refresh()
    driver4.refresh()
