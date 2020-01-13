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

# 5. http://www.psychicscience.org/random.aspx - генератор случайных  чисел;

class testik(unittest.TestCase):
    def test_one(self):
        d = webdriver.Chrome('D:\\Users\\BeJlka\\Desktop\\chromedriver.exe')
        d.get("http://www.psychicscience.org/random.aspx")
        a = 3
        b = 30
        c = 150
        d.find_element_by_id("num").send_keys(a)
        d.find_element_by_id("st").send_keys(b)
        d.find_element_by_id("en").send_keys(c)
        d.find_element_by_css_selector('.btn.btn-success.btn-lg').click()
        sleep(3)
        ta = d.find_element_by_id("output").get_attribute("value")
        nums = ta.split("\n")[0]
        nums = nums.split(" ")
        for i in range(0, a):
            if b <= int(nums[i]) <= c:
                print(nums[i] + " vhodit v diapazon")
            else:
                print(nums[i] + " ne vhodit v diapazon")
        sleep(5)
#
#
# if __name__ == "__main__":
#     unittest.main()

