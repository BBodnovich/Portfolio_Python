'''
Purpose:
Scan the BestBuy website daily to check the current price of the Macbook Pro M3 Max
If the price is under the specified value you'll receive an email with the information
Information includes product title, current price, and link to the product sale page

Usage:
1) Upload code to https://www.pythonanywhere.com
2) Edit connection variables my_email, my_token, target_email
   Recommend using EXPORT instead of hard coding token
3) Modify smtplib address if not using a gmail account
3) Modify variable target_price if necessary
4) Run the code and wait for your price drop email
'''


import smtplib
import time
import requests
from bs4 import BeautifulSoup


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
        my_email = "SOURCE_EMAIL_ADDRESS"
        my_token = "YOUR_EMAIL_TOKEN"
        target_email = "TARGET_EMAIL_ADDRESS"
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_token)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs=target_email,
                msg="Subject:MacBook Pro on sale!\n\n"
                f"Item:\n{str(title)}\n"
                f"\nPrice:\n{price}\n"
                f"\nLink:\n{str(web_url)}")
    else:
        time.sleep(43200)
        price_check()


price_check()
