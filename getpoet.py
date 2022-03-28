# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
file=open("poet",'a')
for i in range(105,200):
    driver = webdriver.Firefox()
    driver.get("https://www.shicimingju.com/chaxun/zuozhe/"+str(i)+".html")
    time.sleep(2)
    try:
        element=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[3]/div[1]/div[2]/a")))
        dynasty=element.text
        if dynasty=="唐":
            authcontent = []
            auth = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div[2]/div[1]/h4/a").text
            address = "https://www.shicimingju.com/chaxun/zuozhe/" + str(i) + ".html"
            Number_of_works_included = driver.find_element_by_xpath(
                "/html/body/div[3]/div[2]/div[1]/div[3]/div[2]/div[2]/a").text
            authcontent.append(auth)
            authcontent.append(dynasty)
            authcontent.append(address)
            authcontent.append(Number_of_works_included)
            print(authcontent)
            file.write(str(authcontent) + '\n')
    finally:
        driver.close()
