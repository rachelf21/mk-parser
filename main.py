from file_engine import FileEngine
from datetime import datetime

infile = 'input/input_ebay_items.csv'


def create_outfile_name(date: str) -> str:
    filename = 'output/output_ebay_item_details'
    outfile = filename + '_' + date + '.csv'
    return outfile


def get_current_timestamp() -> str:
    return datetime.now().strftime('%m%d%Y%H%M%S')


def calculate_runtime(start: datetime):
    time_begin = start
    time_end = datetime.now()
    return time_end - time_begin


if __name__ == '__main__':
    time_start = datetime.now()
    current_ts = get_current_timestamp()
    outfile = create_outfile_name(current_ts)

    file_engine = FileEngine(infile, outfile)
    file_engine.process_input_file()
    file_engine.export_csv()

    runtime = calculate_runtime(time_start).total_seconds()
    print(f"Runtime: {runtime:.2f} sec")
    print(f"Processing complete. Details have been saved to '{outfile}'.")
