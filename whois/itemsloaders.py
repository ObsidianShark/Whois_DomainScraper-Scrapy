import re

from itemloaders.processors import Identity, Join, MapCompose, TakeFirst
from scrapy.loader import ItemLoader


def remove_newlines(text):
    text = re.sub("\n", " ", text)
    return text


class DomainLoader(ItemLoader):
    default_input_processor = MapCompose(str.strip)
    default_output_processor = TakeFirst()

    status_out = Identity()
    servers_names_out = Identity()

    raw_data_in = MapCompose(remove_newlines)
    raw_data_out = Join(" ")

    scraping_date_in = MapCompose()
