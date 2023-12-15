#第一版星问卷自动填写工具

import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
from lxml import etree

url = "https://www.wjx.cn/vm/tjTwe7A.aspx#"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
}
responese = requests.get(url,headers=header)
html_txt = responese.text
# tree = etree.HTML(html_txt)

# divs = tree.xpath/("/html/body/div[1]/form/div[13]/div[4]/fieldset/div")
# for div in divs:
#     list = div.xpath("./div[2]")
#     print(list)
# print(len(divs))

soup = BeautifulSoup(html_txt,"lxml")
all_topic = soup.findAll("div",attrs={"class":"ui-controlgroup column1"})
# titles_num = soup.select('p.title')
print(len(all_topic))
print(all_topic)
choices_xpath=[]
choices_xpathnum = []
# for num in range(1,len(all_topic)+1):
for num in range(1,2):
    newxpath = '//*[@id="div{}"]/div[2]'.format(num)
    choices_xpath.append(newxpath)

# 启动浏览器
driver = webdriver.Chrome()

# 打开问卷链接
driver.get(url)
time.sleep(3)

# 填写选择题
for xpath in choices_xpath:
    try:
        # 获取所有符合xpath条件的选项
        choices = driver.find_elements(By.XPATH, xpath)
        print(type(choices))
        print(choices)
        random_choice = random.choice(choices)
        random_choice.click()
        
    except Exception as e:
        print("填写选择题时发生错误:", e)

# 提交问卷
submit_button = driver.find_element(By.XPATH, '//*[@id="ctlNext"]')
submit_button.click()

# 关闭浏览器
time.sleep(3)
driver.quit()