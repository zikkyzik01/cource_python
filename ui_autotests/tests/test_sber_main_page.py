import pytest
from selenium import webdriver
import time

def test_open_sber_main_page():
    driver = webdriver.Chrome("C:\Program Files (x86)\ChromeDriverSB\sberbrowser_driver_2.0.0.0.exe")
    driver.implicitly_wait(10)
    driver.get("http://www.sberbank.ru/ ")
    driver.maximize_window()

    driver.find_elements_by_id("main-page")
    driver.find_element_by_tag_name("span")
    driver.find_element_by_css_selector("#pid6\:saVTAQjrtbcXI1uY0u51 > div")
    driver.find_element_by_xpath("//a[text()='СберБанк Онлайн']")
    driver.find_element_by_xpath("//a[text()='СберБанк Онлайн']/following::div[1]")
    driver.find_element_by_xpath("//a[text()='СберБанк Онлайн']/following::div[1]/a[1]")
    driver.find_element_by_xpath("//a[text()='СберБанк Онлайн']/parent::div")

    driver.find_element_by_xpath("(//a[text()='Курсы валют'])[1]")
    driver.find_element_by_xpath("(//a[text()='Офисы'])[1]")

    driver.find_element_by_xpath("(//a[text()='Москва'])[1]")
    driver.find_element_by_xpath("(//a[text()='ENG'])[1]")
    driver.find_element_by_xpath("//*[@id='pid6:saVTAQjrtbcXI1uY0u51']/div/section/div/div/div[2]/header/div/div[2]/div[1]/a")
