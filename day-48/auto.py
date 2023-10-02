from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options) 
driver.get("http://secure-retreat-92358.herokuapp.com/")

data = ["Fernando","Quisaguano","fer@example.com"]
names_ = ["fName","lName","email"]

for n in range(len(data)):
    search = driver.find_element(By.NAME, value=names_[n])
    search.send_keys(data[n])

button = driver.find_element(By.XPATH, value='/html/body/form/button')
button.click()


#driver.quit()