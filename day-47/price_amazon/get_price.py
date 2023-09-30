import requests
import lxml
from bs4 import BeautifulSoup

class Price:
    def __init__(self):
        self.url = "https://www.amazon.com/GK-GAMAKAY-LK75-Mechanical-White-Phoenix/dp/B0CF2K19WD/ref=sr_1_2_sspa?crid=YWWWOKFK8WXW&keywords=gamakay&qid=1696015796&sprefix=gamaka%2Caps%2C190&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
        self.header = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
        }

    def getPrice(self):
        """get title and price product of amazon
        Returns:
            str: title
            float: price
        """
        response = requests.get(self.url, headers=self.header)

        soup = BeautifulSoup(response.content, "lxml")
        #print(soup.prettify())
        title = soup.find(id="productTitle").get_text().strip()
        price = soup.find(class_="a-offscreen").get_text()
        price_without_currency = price.split("$")[1]
        price_as_float = float(price_without_currency)
        return title, price_as_float





