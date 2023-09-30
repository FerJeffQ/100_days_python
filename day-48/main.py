import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options) 

#driver.get('https://www.amazon.com/GK-GAMAKAY-LK75-Mechanical-White-Phoenix/dp/B0CF2K19WD/ref=sr_1_1_sspa?crid=2JT400ELBKQUQ&keywords=gamakay&qid=1696020822&sprefix=gamake%2Caps%2C660&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1')

#time.sleep(5) 

#price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
#price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

#print(f"The price is {price_dollar.text}.{price_cents.text}")

driver.get("https://www.python.org")

search_bar = driver.find_element(By.NAME, value="q")
#print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))
button = driver.find_element(By.ID, value="submit")
print(button.size)
documentation_link = driver.find_element(By.CSS_SELECTOR, value=".jobs-widget a")
print(documentation_link.text)

bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

#driver.quit()

