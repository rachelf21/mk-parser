import csv
import pandas as pd

from web_crawler import WebCrawler


class FileEngine:

    def __init__(self, in_file: str, out_file: str):
        self.input_csv_file = in_file
        self.output_csv_file = out_file
        self.web_crawler = WebCrawler()
        self.df = pd.DataFrame(columns=['Description', 'Price', 'Max Discounted Price', 'Availability', 'Out_of_Stock', 'Item_URL'])

    def process_input_file(self):
        with open(self.input_csv_file, mode='r', newline='', encoding='utf-8') as infile:
            reader = csv.reader(infile)

            # Iterate over each URL in the input CSV
            for row in reader:
                item_url = row[0]
                print(item_url)
                description, price, max_discounted_price, availability, out_of_stock  = self.web_crawler.get_ebay_item_details(item_url)
                record = [description, price, max_discounted_price, availability, out_of_stock, item_url]
                self.__add_to_df(record)

    def export_csv(self):
        print(self.df.head(5))
        print(f"\nNumber of records processed: {len(self.df)}")
        pd.DataFrame.to_csv(self.df, self.output_csv_file, index=False)

    def __add_to_df(self, record: list):
        self.df.loc[len(self.df)] = record
