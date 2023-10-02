from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options) 
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# number = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# print(number.text)
number = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
print(number.text)
#number.click()

history = driver.find_element(By.LINK_TEXT, value="View history")
#history.click()

search = driver.find_element(By.NAME, value="search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
