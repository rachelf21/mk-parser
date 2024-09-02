import requests
from bs4 import BeautifulSoup


def get_description(soup: BeautifulSoup) -> str:
    description_tag = soup.find('h1', {'class': 'x-item-title__mainTitle'})
    description = description_tag.find('span', {'class': 'ux-textspans ux-textspans--BOLD'})
    if description is not None:
        description = description.get_text(strip=True)
    else:
        description = 'Description missing'
    print('description:', description)
    return description


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


def get_max_discounted_price(soup: BeautifulSoup) -> str:
    max_discounted_price_tag = soup.find('div', {'class': 'x-volume-pricing__more-text'})
    if max_discounted_price_tag is not None:
        max_discounted_price_tag = max_discounted_price_tag.find('span', {'data-testid': 'ux-textual-display'})
        if max_discounted_price_tag is not None:
            max_discounted_price = max_discounted_price_tag.find('span', {'class': 'ux-textspans ux-textspans--BOLD'})
            if max_discounted_price_tag is not None:
                max_discounted_price = max_discounted_price.get_text(strip=True)
    else:
        # max_discounted_price_tag = soup.find('span', {'id': 'mm-saleDscPrc'})  # Some listings use a different ID
        max_discounted_price = 'No Discount'
    print("max_discounted_price:", max_discounted_price)
    return max_discounted_price


def get_availability(soup: BeautifulSoup) -> str:
    availability_tag = soup.find('div', {'class': 'x-quantity__availability evo'})
    availability = availability_tag.find('span', {'class': 'ux-textspans ux-textspans--SECONDARY'})
    if availability is not None:
        availability = availability.get_text(strip=True)
    else:
        availability = 'Availability not found'
    print('availability:', availability)
    return availability



class WebCrawler:

    def get_ebay_item_details(self, item_url):
        response = requests.get(item_url)
        if response.status_code != 200:
            return 'Failed to retrieve', 'Failed to retrieve'
        soup = BeautifulSoup(response.content, 'html.parser')
        description = get_description(soup)
        price = get_price(soup)
        max_discounted_price = get_max_discounted_price(soup)
        availability = get_availability(soup)
        return description, price, max_discounted_price, availability
