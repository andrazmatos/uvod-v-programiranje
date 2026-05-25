from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
# DRŽAVNOZBORSKE VOLITVE 2026
driver.get("https://volitve.dvk-rs.si/dz2026/#/rezultati")

time.sleep(2)
gumb = driver.find_element(By.ID, "p-tabpanel-4-label")
gumb.send_keys(Keys.RETURN)

time.sleep(15)

with open(f"teorija\\volitve\\DZ2026_2.html", "w", encoding="UTF-8") as dat:
    dat.write(driver.page_source)

# DRŽAVNOZBORSKE VOLITVE 2000
for i in range(1:8):
    driver.get(f"https://www.dvk-rs.si/arhivi/dz2000/rez_vo{i}.html")

time.sleep(2)
gumb = driver.find_element(By.ID, "p-tabpanel-4-label")
gumb.send_keys(Keys.RETURN)

time.sleep(15)

with open(f"teorija\\volitve\\DZ2026_2.html", "w", encoding="UTF-8") as dat:
    dat.write(driver.page_source)

