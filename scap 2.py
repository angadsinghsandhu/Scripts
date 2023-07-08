from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
import time



link = "https://www.jiosaavn.com/s/playlist/b286962264a530026fd2eafb2594cd3b/2017____phone___fb___1545166199___imported/5VIRI9yDZA3uCJW60TJk1Q__"
# link = ""

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get(link)

# click "Load More" button
# class: class="c-btn c-btn--primary c-btn--small"
# text: Load more

while True:
    try:
        btn = driver.find_element("xpath", '//button[@class="c-btn c-btn--primary c-btn--small"]')
        driver.execute_script("arguments[0].click();", btn)
        time.sleep(1)
    except:
        break

songs = []

content = driver.page_source
soup = bs(content, features="html.parser")

cnt = 0
for song in soup.find_all("figure", class_=['o-flag', 'o-flag--action', 'o-flag--stretch', 'o-flag--mini', 'u-link']):
    try:
        name = song.find("a", class_='u-color-js-gray').text
        artist = song.find("a", attrs={"screen_name": "artist_screen"}).text
        print(f"{artist} - {name}")
        cnt += 1
    except:
        continue

print(f"\n Total Songs: {cnt}")

driver.quit()
