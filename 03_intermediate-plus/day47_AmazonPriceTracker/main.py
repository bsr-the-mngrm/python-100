import requests
import smtplib
from bs4 import BeautifulSoup
from dotenv import load_dotenv

LOWER_LIMIT = 70


def get_amazon_price(url: str) -> float:
    """Returns the price of the product on the given URL"""
    response = requests.get(url)
    amazon_soup = BeautifulSoup(response.text, 'html.parser')
    price = float(amazon_soup.find(class_="a-offscreen").getText()[1:])

    return price


if __name__ == '__main__':
    product_amazon_url = "https://www.amazon.com/Amazon-Basics-Turntable-Speakers-Bluetooth/dp/B0BFHTPLNP/"

    product_amazon_price = get_amazon_price(product_amazon_url)

    print(product_amazon_price)
