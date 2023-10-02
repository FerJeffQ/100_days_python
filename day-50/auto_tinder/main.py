from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


chrome_driver_loc = "C:\Development\chromedriver.exe"
URL = "https://tinder.com/"
fb_name = "xrhstosalastor@gmail.com"
fb_pass = "nN@c1lx*aA131"


driver = webdriver.Chrome(executable_path=chrome_driver_loc)
driver.maximize_window()
driver.get(URL)


# ------- Accept Tinder cookies ----------------------------------
tinder_cookies = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="o41285377"]/div/div[2]/div/div/div[1]/button')))
tinder_cookies.click()

#----------------- Press Tinder Login Button --------------------------------
tinder_login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="o41285377"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')))
tinder_login.click()

# ----------- Name the main Tinder window --------------------
tinder_window = driver.window_handles[0]

# ------------------------ Use FB login --------------------------------
tinder_fb_login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="o-1687095699"]/div/div/div[1]/div/div[3]/span/div[2]/button')))
tinder_fb_login.click()

# ----------------- Change the focus windows to FB popup ------------------------
time.sleep(5)
fb_login = driver.window_handles[1]
driver.switch_to.window(fb_login)

# -------------------------------- maximize_window and accept FB cookies ------------------------
driver.maximize_window()
time.sleep(2)
fb_cookies = driver.find_elements(By.CSS_SELECTOR, 'button')
fb_cookies[1].click()

# ------------------- Login to FB ----------------------------------
time.sleep(2)
login_info = driver.find_elements(By.CLASS_NAME, "inputtext")
login_info[0].send_keys(fb_name)
login_info[1].send_keys(fb_pass)
login_info[1].send_keys(Keys.RETURN)

#------------- Change back to tinder window & accept location / notifications --------
driver.switch_to.window(tinder_window)

accept_loc = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="o-1687095699"]/div/div/div/div/div[3]/button[1]')))
accept_loc.click()
decline_notif = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="o-1687095699"]/div/div/div/div/div[3]/button[2]')))
decline_notif.click()

# ---------------- Like Profiles ----------------------------------------------------------
time.sleep(3)
actions = ActionChains(driver)

for i in range(20):
    try:
        actions.send_keys(Keys.ARROW_RIGHT)    
        actions.perform()    
    except Exception:
        pass
    try:
        match = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a").click()
    except Exception:
        pass
    try:    
        win_app = driver.find_element(By.XPATH, '//*[@id="o-1687095699"]/div/div/div[2]/button[2]').click()
    except Exception:
        pass

    time.sleep(3)
`
`