from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.request
import os
import requests
import time

if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path="./chromedriver",options=Options().add_argument("--disable-infobar"))
    driver.get("https://cumsdtu.in/registration_student/login/login.jsp")
    img_src=driver.find_element_by_xpath('//*[@id="captchaImg"]').get_attribute('src')
    print(img_src)
    # path="./captcha_data"
    # if not os.path.exists(path):
    #     os.makedirs(path)
    # for _ in range(2000):
    #     name = f"./captcha_data/captcha{_+1}.jpeg" 
    #     urllib.request.urlretrieve(img_src,name)
    #     print(f'the captcha is ------------ captcha{_+1}.jpeg')
    #     time.sleep(0.01)
    # img = requests.get(img_src.content)

    # with open('captcha.jpg','wb') as f:
    #     f.write(img)
