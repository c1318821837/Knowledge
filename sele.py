# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
browser.get("http://bmfw.www.gov.cn/zcdwpt/index.html#/")
time.sleep(1)
def getcontent(browser):
    cont = []
    try:
        qelement = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[1]/h2")))
        question = qelement.text
        celement = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[1]/div[1]")))
        content = celement.text
        aelement = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[1]")))
        ap = aelement.text
        telement=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[2]")))
        ti = telement.text
        cont.append(question)
        cont.append(content)
        cont.append(ap)
        cont.append(ti)
        return cont
    finally:
        time.sleep(1)

def read_page(browser,index):
    for i in range(2, 7):
        print(i)
        try:
            element=WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[' + str(i) + ']/div/p/span")))
            element.click()
            content = getcontent(browser)
            print(content)
            browser.back()
            time.sleep(1)
            file = open(str(index), 'a')
            file.write(str(content) + '\n')
        finally:
            time.sleep(1)

for i in range(1,100):
    read_page(browser,i)
    print("page:"+str(i))
    browser.find_element_by_xpath('//*[@id="nextPage"]').click()
    time.sleep(1)
