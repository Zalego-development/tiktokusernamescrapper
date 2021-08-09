from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.utils import os_architecture
import time

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get('https://app.popularpays.com/search/off-platform?brandId=bf0f61a7-c6d1-46ad-9926-40ba0356bd3a&follower_count_gteq=150000&follower_count_lteq=180000')
element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("identification"))
username = driver.find_element_by_id("identification")
password = driver.find_element_by_id("password")
submit   = driver.find_element_by_class_name("button--full-width")
username.send_keys("seffu.kioi@zalda.net")
password.send_keys("Rawadh2020&")
submit.click()

time.sleep(10)
timeout = time.time() + 60*30
element2 = driver.find_element_by_class_name("off-platform-profiles")
while True:
    element2.send_keys(Keys.PAGE_DOWN)
    loader = driver.find_element_by_class_name("infinity-loader")
    if time.time() > timeout:
        break

print("now scraping")
data = driver.find_elements_by_class_name("off-platform-profile")
full_list = []
for items in data:
    details = []
    handle = items.find_element_by_class_name("off-platform-profile__handle")
    details.append(handle.text)
    # name = items.find_element_by_class_name("off-platform-profile__name")
    # details.append(name.text)
    # followers = items.find_element_by_class_name("off-platform-profile__stat-value")
    # details.append(followers.text)
    # if items.find_element_by_class_name("off-platform-profile__email-text"):
    #     email = items.find_element_by_class_name("off-platform-profile__email-text")
    full_list.append(details)

with open('influencers.txt', 'w') as pt:
    pt.write("%s\n" % full_list)
