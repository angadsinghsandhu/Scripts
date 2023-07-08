from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup as bs

import re, time


link = "https://www.jiosaavn.com/s/playlist/b286962264a530026fd2eafb2594cd3b/2018_part_1____phone___fb___1545166199___imported/eLFUU7qBf8hFo9wdEAzFBA__"

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get(link)

# click "Load More" button
# class: class="c-btn c-btn--primary c-btn--small"
# text: Load more
btn = driver.find_element("xpath", '//button[@class="c-btn c-btn--primary c-btn--small"]')
print(btn)
while True:
    try:
        driver.execute_script("arguments[0].click();", btn)
        time.sleep(5)
        btn = driver.find_element("xpath", '//button[@class="c-btn c-btn--primary c-btn--small"]')
    except:
        break

# l.click()

# WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="c-btn c-btn--primary c-btn--small"]'))).click()

songs = []

content = driver.page_source
soup = bs(content, features="html.parser")

scr = soup.findAll('script', attrs={"class": None, "data-chunk": None, "src": None, "type": None})[-1]
info = scr.get_text()

pattern = r'(?<="be_subtitle":\[\{"text":")[^"]*'
matches = re.findall(pattern, info)

print(f"The number of songs scraped: {len(matches)}\n\nSongs:\n")

for i in matches:
    print(i)

driver.quit()
