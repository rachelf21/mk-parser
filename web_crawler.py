import requests
from bs4 import BeautifulSoup


def get_description(soup: BeautifulSoup) -> str:
    description = 'Description missing'
    try:
        description_tag = soup.find('h1', {'class': 'x-item-title__mainTitle'})
        description = description_tag.find('span', {'class': 'ux-textspans ux-textspans--BOLD'})
        if description is not None:
            description = description.get_text(strip=True)
    except Exception as e:
        print(f'An error occurred while retrieving Description info: {str(e)}')
    finally:
        print('description:', description)
        return description


def get_price(soup: BeautifulSoup) -> str:
    price = 'Not found'
    try:
        price_tag = soup.find('div', {'class': 'x-price-primary'})
        price_with_text = price_tag.find('span', {'class': 'ux-textspans'})
        if price_with_text is not None:
            price: str = price_with_text.get_text(strip=True)
            price = price.replace('US $', '').replace('/ea', '')
    except Exception as e:
        print(f'An error occurred while retrieving price info: {str(e)}')
    finally:
        print("price:", price)
        return price


def get_max_discounted_price(soup: BeautifulSoup) -> str:
    max_discounted_price = 'No Discount'
    try:
        max_discounted_price_tag = soup.find('div', {'class': 'x-volume-pricing__more-text'})
        if max_discounted_price_tag is not None:
            max_discounted_price_tag = max_discounted_price_tag.find('span', {'data-testid': 'ux-textual-display'})
            if max_discounted_price_tag is not None:
                max_discounted_price = max_discounted_price_tag.find('span', {'class': 'ux-textspans ux-textspans--BOLD'})
                if max_discounted_price_tag is not None:
                    max_discounted_price = max_discounted_price.get_text(strip=True)
    except Exception as e:
        print(f'An error occurred while retrieving Discount info: {str(e)}')
    finally:
        print("max_discounted_price:", max_discounted_price)
        return max_discounted_price


def get_availability(soup: BeautifulSoup) -> str:
    availability = 'Availability not found'
    try:
        availability_tag = soup.find('div', {'class': 'x-quantity__availability'})
        availability = availability_tag.find('span', {'class': 'ux-textspans ux-textspans--SECONDARY'})
        availability = availability.get_text(strip=True)
    except Exception as e:
        print(f'An error occurred while retrieving Availability info: {str(e)}')
    finally:
        print('availability:', availability)
        return availability


def is_out_of_stock(soup: BeautifulSoup) -> str:
    out_of_stock = ''
    try:
        out_of_stock_tag = soup.find('div', {'class': 'ux-message__title'})
        if out_of_stock_tag is not None:
            out_of_stock_tag = soup.find('span', {'data-testid': 'ux-textual-display'})
            if out_of_stock_tag is not None:
                out_of_stock = 'OUT OF STOCK!'
    except Exception as e:
        print(f'An error occurred while retrieving Stock info: {str(e)}')
    finally:
        print(out_of_stock)
        return out_of_stock


class WebCrawler:

    def get_ebay_item_details(self, item_url):
        response = requests.get(item_url)
        if response.status_code != 200:
            return 'Failed to retrieve items from ebay'
        soup = BeautifulSoup(response.content, 'html.parser')
        description = get_description(soup)
        price = get_price(soup)
        max_discounted_price = get_max_discounted_price(soup)
        availability = get_availability(soup)
        out_of_stock = is_out_of_stock(soup)
        return description, price, max_discounted_price, availability, out_of_stock