import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

browse = webdriver.Firefox()

browse.get('http://www.facebook.com')

username = browse.find_element_by_id('email')
password = browse.find_element_by_id( 'pass')
submit = browse.find_element_by_id('u_0_b')

username.send_keys('SomeKindaOf@email.com')
password.send_keys('SomeKindaPassword')
submit.click()