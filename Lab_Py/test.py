# -*- coding: utf-8 -*-
import unittest
from bs4 import BeautifulSoup
import urllib.request
import webbrowser
from time import sleep
import re
from selenium import webdriver
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# 5. Открыть поисковый сайт. Набрать в поисковом поле словосочетание
# «Эффективное тестирование программ» (при наборе кавычки обязательны)
# и нажать кнопку «Найти».  Открыть повторно данный сайт и набрать в
# поисковом поле словосочетание  Эффективное тестирование программ
# (кавычек не ставить!). Проверить какие из ссылок, появившихся  при
# втором поиске, содержатся на первых трех  страницах  сайта, полученного
# в результате первого поиска. Определить количество появлений каждой из этих ссылок.

class testik(unittest.TestCase):

    def test_one(self):
        d = webdriver.Chrome('D:\\Users\\BeJlka\\Desktop\\chromedriver.exe')
        d.get("http://www.google.com")
        str = "«Эффективное тестирование программ»"
        str2 = "Эффективное тестирование программ"
        d.find_element_by_css_selector(".gLFyf.gsfi").send_keys(str)
        d.find_element_by_css_selector(".gLFyf.gsfi").send_keys(Keys.RETURN)

        input_raw = ""
        #elems = d.find_elements_by_tag_name("cite")
        elems = d.find_elements_by_xpath('.//div[@class="r"]/a')
        for i in range(0, len(elems)):
            input_raw = input_raw + " " + elems[i].get_attribute("href")
            links = input_raw
        print("Список после первой страницы")
        links = links.strip().split(" ")
        print(links)

        d.find_element_by_class_name("pn").click()
        elems = d.find_elements_by_xpath('.//div[@class="r"]/a')
        for i in range(0, len(elems)):
            input_raw = input_raw + " " + elems[i].get_attribute("href")
            links = input_raw
        print("Список после второй страницы")
        links = links.strip().split(" ")
        print(links)


        d.find_element_by_class_name("pn").click()
        elems = d.find_elements_by_xpath('.//div[@class="r"]/a')
        for i in range(0, len(elems)):
            input_raw = input_raw + " " + elems[i].get_attribute("href")
            links = input_raw
        print("Список после третьей страницы")
        links = links.strip().split(" ")
        print(links)

        d.find_element_by_css_selector(".gLFyf.gsfi").clear()
        d.find_element_by_css_selector(".gLFyf.gsfi").send_keys(str2)
        d.find_element_by_css_selector('.Tg7LZd').click()

        input_raw_2 = ""
        elems = d.find_elements_by_xpath('.//div[@class="r"]/a')
        for i in range(0, len(elems)):
            input_raw_2 = input_raw_2 + " " + elems[i].get_attribute("href")
            links2 = input_raw_2
        print("Список после нового поиска")
        links2 = links2.strip().split(" ")
        print(links2)

        print("Очищенный второй список от повторов")
        links_new_2 = list(set(links2))
        print(links_new_2)

        for i in range(0, len(links)):
            count = 0
            for j in range(0, len(links2)):
                if links[i] == links2[j]:
                    count = count + 1
            print_links(links[i], count)

        sleep(5)

def print_links(links, count):
    print("Cайт: {} найден: {} раз(а)".format(links, count))

#
#
# if __name__ == "__main__":
#     unittest.main()
