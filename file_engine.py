import csv
import pandas as pd

from web_crawler import WebCrawler


class FileEngine:

    def __init__(self, in_file: str, out_file: str):
        self.input_csv_file = in_file
        self.output_csv_file = out_file
        self.web_crawler = WebCrawler()
        self.df = pd.DataFrame(columns=['Item_URL', 'Price', 'Availability'])

    def process_input_file(self):
        with open(self.input_csv_file, mode='r', newline='', encoding='utf-8') as infile:
            reader = csv.reader(infile)

            # Iterate over each URL in the input CSV
            for row in reader:
                item_url = row[0]
                print(item_url)
                price, availability = self.web_crawler.get_ebay_item_details(item_url)
                record = [item_url, price, availability]
                self.__add_to_df(record)

    def export_csv(self):
        print(self.df.head(5))
        print(f"\nNumber of records processed: {len(self.df)}")
        pd.DataFrame.to_csv(self.df, self.output_csv_file, index=False)

    def __add_to_df(self, record: list):
        self.df.loc[len(self.df)] = record
