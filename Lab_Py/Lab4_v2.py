# -*- coding: utf-8 -*-
import unittest
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

# 2. Выбрать блог. Для всех постов на главной странице проверить,
# краткое описание поста соответствует содержимому статьи.

class testik(unittest.TestCase):

    def test_one(self):
        d = webdriver.Chrome('D:\\Users\\BeJlka\\Desktop\\chromedriver.exe')
        d.get("https://thebestcashforhouses.home.blog/")
        elems = d.find_elements_by_class_name("entry-title")
        a = 3
        name_link = [[0] * 2 for i in range(a)]
        for i in range(3):
            name_link[i][0] = elems[i].find_element_by_tag_name("a").text
            name_link[i][1] = elems[i].find_element_by_tag_name("a").get_attribute("href")

        for i in name_link:
            # noinspection PyTypeChecker
            print("Блог \"{}\" краткое содержание соответствует полному на {:.0%}".format(i[0], check_blog(d, i[0], i[1])))
            sleep(0.5)


def check_blog(driver, name, link):
    driver.get(link)
    content = driver.find_element_by_class_name("entry-content").text
    word = name.split(" ")
    count = 0
    for w in word:
        if content.find(w) != -1:
            count = count + 1
    return count / len(word)

#
#
# if __name__ == "__main__":
#     unittest.main()
