import requests
from bs4 import BeautifulSoup


def get_availability(soup: BeautifulSoup) -> str:
    availability_tag = soup.find('div', {'class': 'x-quantity__availability evo'})
    availability = availability_tag.find('span', {'class': 'ux-textspans ux-textspans--SECONDARY'})
    if availability is not None:
        availability = availability.get_text(strip=True)
    else:
        availability = 'Availability not found'
    print('availability:', availability)
    return availability


def get_price(soup: BeautifulSoup) -> str:
    price_tag = soup.find('div', {'class': 'x-price-primary'})
    price = price_tag.find('span', {'class': 'ux-textspans'})
    if price is not None:
        price = price.get_text(strip=True)
    else:
        # price_tag = soup.find('span', {'id': 'mm-saleDscPrc'})  # Some listings use a different ID
        price = 'Not found'
    print("price:", price)
    return price


class WebCrawler:

    def get_ebay_item_details(self, item_url):
        response = requests.get(item_url)
        if response.status_code != 200:
            return 'Failed to retrieve', 'Failed to retrieve'
        soup = BeautifulSoup(response.content, 'html.parser')
        price = get_price(soup)
        availability = get_availability(soup)
        return price, availability
