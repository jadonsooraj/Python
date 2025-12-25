from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd


options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service=Service(),
    options=options
)

# Open LeetCode and sign In
driver.get("https://leetcode.com/accounts/login/")
# driver.find_element(
#     By.CSS_SELECTOR,
#     "div.nav-menu > a:nth-of-type(5)"
# ).click()
driver.find_element(By.ID,'id_login').send_keys('jadonsuraj49@gmail.com')
driver.find_element(By.ID,'id_password').send_keys('Sooryaa@1029')
time.sleep(10)


#go to list page and extract list
list_url = "https://leetcode.com/problem-list/mke5rjqc/"
driver.get(list_url)
time.sleep(5)

questions = []

rows = driver.find_elements(By.CSS_SELECTOR, ".SortableItem")

for row in rows:
    try:
        title = row.find_element(By.CSS_SELECTOR, "div[class='ellipsis line-clamp-1'").text
        link = row.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
        difficulty = row.text.split("\n")[-1]

        questions.append({
            "Title": title,
            "Difficulty": difficulty,
            "Link": link
        })
    except:
        continue

# time.sleep(4)
driver.close()

df = pd.DataFrame(questions)
df.to_excel("leetcode_String_list.xlsx", index=False)
print(questions)