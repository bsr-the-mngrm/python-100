import requests
import smtplib
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

LOWER_LIMIT = 70


def get_amazon_price(url: str) -> float:
    """Returns the price of the product on the given URL"""
    response = requests.get(url)
    amazon_soup = BeautifulSoup(response.text, 'html.parser')
    price = float(amazon_soup.find(class_="a-offscreen").getText()[1:])

    return price


def send_email_alert(source: str, product_name: str, price: float, url: str):
    load_dotenv()

    email_address = os.getenv('EMAIL_ADDRESS')
    email_app_password = os.getenv('EMAIL_APP_PASSWORD')
    email_host = os.getenv('EMAIL_HOST')
    email_host_port = os.getenv('EMAIL_HOST_PORT')

    with smtplib.SMTP_SSL(host=email_host, port=email_host_port) as connection:
        connection.login(user=email_address, password=email_app_password)
        connection.sendmail(
            from_addr=email_address,
            to_addrs=email_address,
            msg=f"SUBJECT:{source} Price Alert\n\n"
                f"{product_name} is now ${price}\n\n"
                f"LINK: {url}"
        )


if __name__ == '__main__':
    product_amazon_url = "https://www.amazon.com/Amazon-Basics-Turntable-Speakers-Bluetooth/dp/B0BFHTPLNP/"

    product_amazon_price = get_amazon_price(product_amazon_url)

    if product_amazon_price < LOWER_LIMIT:
        send_email_alert('Amazon', 'Amazon Basics Turntable Record Player', product_amazon_price, product_amazon_url)
