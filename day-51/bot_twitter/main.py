from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



USERNAME = "ferjeff11"
PASSWORD = "1nf1n1t0"

X_URL = "https://twitter.com/"
URL = "https://www.speedtest.net/"


class Bot_Twitter:
    """
    Class to publish twit about my speed of internet
    """
    def __init__(self) -> None:
        """
        attach windows, maximize and open window of twitter
        """
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        #self.driver = webdriver.Chrome()       
        self.up = 0
        self.down = 0

    def login(self):
        self.driver.get(X_URL)
        sleep(1)        
        btn_sign = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div')
        btn_sign.click()
        sleep(3)        
        input_name = self.driver.find_element(By.NAME, value='text')
        input_name.send_keys(USERNAME)
        sleep(1)        
        btn_next = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        btn_next.click()
        sleep(1)        
        input_pass = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        input_pass.send_keys(PASSWORD)
        sleep(1)        
        btn_log = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
        btn_log.click()

      

    def get_internet_speed(self):
        self.driver.get('https://fast.com/')
        sleep(16)
        # time.sleep()
        show_more_info_btn = self.driver.find_element(By.ID, value='show-more-details-link')
        show_more_info_btn.click()
        sleep(3)
        down_speed = self.driver.find_element(By.ID, value='speed-value')
        print(down_speed.text)

        up_speed = self.driver.find_element(By.ID, value='upload-value')
        print(up_speed.text)
        # print(down_speed)
    def tweet(self):
        sleep(5)
        tweet_compose = self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up"
        tweet_compose.send_keys(tweet)
        sleep(5)
        self.driver.quit()

def main():  
    x_test = Bot_Twitter()
    x_test.get_internet_speed()
    #print(x_test.up)
    #print(x_test.down)
    x_test.login()
    x_test.tweet()


if __name__ == "__main__":
    main()