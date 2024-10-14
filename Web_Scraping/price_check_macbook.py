'''
Scan BestBuy website daily to check current price of the Macbook Pro M3 Max
If price is under the target value an email notification is sent
Information includes product title, current price, and link to the product web page

Usage:
1) Upload code to https://www.pythonanywhere.com
2) Export environment variables for MY_EMAIL, MY_TOKEN, and TARGET_EMAIL
3) Modify smtplib address if not using a gmail account
3) Modify variable target_price if necessary
4) Run the code and wait for your price drop email
'''

import os
import smtplib
import time
import requests
from bs4 import BeautifulSoup

MY_EMAIL = os.environ.get("MY_EMAIL_ADDRESS")
MY_TOKEN = os.environ.get("MY_EMAIL_TOKEN")
TARGET_EMAIL = os.environ.get("TARGET_EMAIL_ADDRESS")

agent = {"User-Agent":"Mozilla/5.0"}
web_url = "https://www.bestbuy.com/site/apple-macbook-pro-14-laptop-m3-max-chip-36gb-memory-30-core-gpu-1tb-ssd-latest-model-silver/6534621.p?skuId=6534621"
web_page = requests.get(url=web_url, headers=agent, timeout=10).text
soup = BeautifulSoup(web_page, "html.parser")


def price_check():
    price_element = soup.find_all("div", class_="priceView-customer-price")
    split1 = str(price_element).split('"true">')
    split2 = split1[1].split("</span>")
    price = split2[0]

    title_element = soup.find_all("h1", class_="v-fw-regular")
    title = title_element[0].string

    target_price = 3000
    current_price = float(price.replace('$', '').replace(',', ''))
    if current_price < target_price:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_TOKEN)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=TARGET_EMAIL,
                msg="Subject:MacBook Pro on sale!\n\n"
                f"Item:\n{str(title)}\n"
                f"\nPrice:\n{price}\n"
                f"\nLink:\n{str(web_url)}")
    else:
        time.sleep(43200)
        price_check()


price_check()
