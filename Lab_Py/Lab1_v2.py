# -*- coding: utf-8 -*-
import unittest
import urllib.request
import webbrowser
from time import sleep

from selenium import webdriver
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# 2. В текстовом файле содержится список из web – адресов 10 сайтов. Считать
# файл и открыть сайты в случайном порядке. Модифицировать список в соответствии
# с данным порядком и закрыть открытые сайты в обратном порядке.

class testik(unittest.TestCase):
    def test_one(self):
        d = webdriver.Chrome('D:\\Users\\BeJlka\\Desktop\\chromedriver.exe')
        f = open('sites.txt', 'r')
        l = []
        print("Файл содержит: ")
        for line in f:
            l.append(line.replace("\n", ""))
            print(line.replace("\n", ""))
        random.shuffle(l)
        s = "window.open('"
        e = "');"
        print("Открываем в случайном порядке: ")
        for line in l:
            print(line)
            n = s + line + e
            d.execute_script(n)
        l.reverse()
        tabs = d.window_handles
        print("Закрываем в обратном порядке")
        for line in tabs:
            d.switch_to.window(line)
            d.close()
            sleep(1)

#
#
# if __name__ == "__main__":
#     unittest.main()

