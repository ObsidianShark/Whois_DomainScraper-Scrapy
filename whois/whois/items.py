# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DomainItem(scrapy.Item):
    # Domain info
    domain_name = scrapy.Field()
    registered_on = scrapy.Field()
    expires_on = scrapy.Field()
    updated_on = scrapy.Field()
    status = scrapy.Field()
    servers_names = scrapy.Field()
    # Registrant info
    registrant_name = scrapy.Field()
    registrant_organization = scrapy.Field()
    registrant_street = scrapy.Field()
    registrant_city = scrapy.Field()
    registrant_state = scrapy.Field()
    registrant_postal_code = scrapy.Field()
    registrant_country = scrapy.Field()
    registrant_phone = scrapy.Field()
    registrant_fax = scrapy.Field()
    # Administrative info
    admin_name = scrapy.Field()
    admin_organization = scrapy.Field()
    admin_street = scrapy.Field()
    admin_city = scrapy.Field()
    admin_state = scrapy.Field()
    admin_postal_code = scrapy.Field()
    admin_country = scrapy.Field()
    admin_phone = scrapy.Field()
    admin_fax = scrapy.Field()
    # Tech info
    tech_name = scrapy.Field()
    tech_organization = scrapy.Field()
    tech_street = scrapy.Field()
    tech_city = scrapy.Field()
    tech_state = scrapy.Field()
    tech_postal_code = scrapy.Field()
    tech_country = scrapy.Field()
    tech_phone = scrapy.Field()
    tech_fax = scrapy.Field()
    # Raw domain info
    raw_data = scrapy.Field()
    # Spider info
    spider = scrapy.Field()
    url = scrapy.Field()
    scraping_date = scrapy.Field()
