import pathlib
from datetime import datetime

import scrapy
from whois.items import DomainItem
from whois.itemsloaders import DomainLoader

DOMAINS_PATH = pathlib.Path("domains_list.txt")


class DomainsSpider(scrapy.Spider):
    name = "whois"
    allowed_domains = ["whois.com"]
    custom_settings = {
        "AUTOTHROTTLE_ENABLED": True,
        "AUTOTHROTTLE_DEBUG": True,
        # 'HTTPCACHE_ENABLED': True,
    }

    def start_requests(self):
        # Request each domain in a .txt file
        domains_list = open(DOMAINS_PATH, "r")
        for domain in domains_list:
            url = f"https://www.whois.com/whois/{domain}"
            yield scrapy.Request(url=url, callback=self.parse_domain)

    def parse_domain(self, response):
        domain_info = DomainLoader(item=DomainItem(), selector=response)
        # Domain info
        domain_info.add_xpath(
            "domain_name",
            "//div[@class='df-row'][div[contains(text(), 'Domain:')]]/div[@class='df-value']/text()",
        )
        domain_info.add_xpath(
            "registered_on",
            "//div[@class='df-row'][div[contains(text(), 'Registered On:')]]/div[@class='df-value']/text()",
        )
        domain_info.add_xpath(
            "expires_on",
            "//div[@class='df-row'][div[contains(text(), 'Expires On:')]]/div[@class='df-value']/text()",
        )
        domain_info.add_xpath(
            "updated_on",
            "//div[@class='df-row'][div[contains(text(), 'Updated On:')]]/div[@class='df-value']/text()",
        )
        domain_info.add_xpath(
            "status",
            "//div[@class='df-row'][div[contains(text(), 'Status:')]]/div[@class='df-value']/text()",
        )
        domain_info.add_xpath(
            "servers_names",
            "//div[@class='df-row'][div[contains(text(), 'Name Servers:')]]/div[@class='df-value']/text()",
        )
        # Registrant info
        domain_info.add_xpath(
            "registrant_name",
            "//div[@class='df-block'][div[@class='df-heading'][contains(text(), 'Registrant Contact')]]//div[@class='df-row'][div[contains(text(), 'Name:')]]/div[@class='df-value']/text()",
        )
        domain_info.add_xpath(
            "registrant_organization",
            "//div[@class='df-block'][div[@class='df-heading'][contains(text(), 'Registrant Contact')]]//div[@class='df-row'][div[contains(text(), 'Organization:')]]/div[@class='df-value']/text()",
        )
        domain_info.add_xpath(
            "registrant_street",
            "//div[@class='df-block'][div[@class='df-heading'][contains(text(), 'Registrant Contact')]]//div[@class='df-row'][div[contains(text(), 'Street:')]]/div[@class='df-value']/text()",
        )
        domain_info.add_xpath(
            "registrant_city",
            "//div[@class='df-block'][div[@class='df-heading'][contains(text(), 'Registrant Contact')]]//div[@class='df-row'][div[contains(text(), 'City:')]]/div[@class='df-value']/text()",
        )
        domain_info.add_xpath(
            "registrant_state",
            "//div[@class='df-block'][div[@class='df-heading'][contains(text(), 'Registrant Contact')]]//div[@class='df-row'][div[contains(text(), 'State:')]]/div[@class='df-value']/text()",
        )
        domain_info.add_xpath(
            "registrant_postal_code",
            "//div[@class='df-block'][div[@class='df-heading'][contains(text(), 'Registrant Contact')]]//div[@class='df-row'][div[contains(text(), 'Postal Code:')]]/div[@class='df-value']/text()",
        )
        domain_info.add_xpath(
            "registrant_country",
            "//div[@class='df-block'][div[@class='df-heading'][contains(text(), 'Registrant Contact')]]//div[@class='df-row'][div[contains(text(), 'Country:')]]/div[@class='df-value']/text()",
        )
        domain_info.add_xpath(
            "registrant_phone",
            "//div[@class='df-block'][div[@class='df-heading'][contains(text(), 'Registrant Contact')]]//div[@class='df-row'][div[contains(text(), 'Phone:')]]/div[@class='df-value']/text()",
        )
        domain_info.add_xpath(
            "registrant_fax",
            "//div[@class='df-block'][div[@class='df-heading'][contains(text(), 'Registrant Contact')]]//div[@class='df-row'][div[contains(text(), 'Fax:')]]/div[@class='df-value']/text()",
        )
        # Administrative info
        domain_info.add_xpath(
            "admin_name",
            "//div[@class='df-block'][div[@class='df-heading'][contains(text(), 'Administrative Contact')]]//div[@class='df-row'][div[contains(text(), 'Name:')]]/div[@class='df-value']/text()",
        )
        domain_info.add_xpath(
            "admin_organization",
            "//div[@class='df-block'][div[@class='df-heading'][contains(text(), 'Administrative Contact')]]//div[@class='df-row'][div[contains(text(), 'Organization:')]]/div[@class='df-value']/text()",
        )
        domain_info.add_xpath(
            "admin_street",
            "//div[@class='df-block'][div[@class='df-heading'][contains(text(), 'Administrative Contact')]]//div[@class='df-row'][div[contains(text(), 'Street:')]]/div[@class='df-value']/text()",
        )
        domain_info.add_xpath(
            "admin_city",
            "//div[@class='df-block'][div[@class='df-heading'][contains(text(), 'Administrative Contact')]]//div[@class='df-row'][div[contains(text(), 'City:')]]/div[@class='df-value']/text()",
        )
        domain_info.add_xpath(
            "admin_state",
            "//div[@class='df-block'][div[@class='df-heading'][contains(text(), 'Administrative Contact')]]//div[@class='df-row'][div[contains(text(), 'State:')]]/div[@class='df-value']/text()",
        )
        domain_info.add_xpath(
            "admin_postal_code",
            "//div[@class='df-block'][div[@class='df-heading'][contains(text(), 'Administrative Contact')]]//div[@class='df-row'][div[contains(text(), 'Postal Code:')]]/div[@class='df-value']/text()",
        )
        domain_info.add_xpath(
            "admin_country",
            "//div[@class='df-block'][div[@class='df-heading'][contains(text(), 'Administrative Contact')]]//div[@class='df-row'][div[contains(text(), 'Country:')]]/div[@class='df-value']/text()",
        )
        domain_info.add_xpath(
            "admin_phone",
            "//div[@class='df-block'][div[@class='df-heading'][contains(text(), 'Administrative Contact')]]//div[@class='df-row'][div[contains(text(), 'Phone:')]]/div[@class='df-value']/text()",
        )
        domain_info.add_xpath(
            "admin_fax",
            "//div[@class='df-block'][div[@class='df-heading'][contains(text(), 'Administrative Contact')]]//div[@class='df-row'][div[contains(text(), 'Fax:')]]/div[@class='df-value']/text()",
        )
        # Tech info
        domain_info.add_xpath(
            "tech_name",
            "//div[@class='df-block'][div[@class='df-heading'][contains(text(), 'Technical Contact')]]//div[@class='df-row'][div[contains(text(), 'Name:')]]/div[@class='df-value']/text()",
        )
        domain_info.add_xpath(
            "tech_organization",
            "//div[@class='df-block'][div[@class='df-heading'][contains(text(), 'Technical Contact')]]//div[@class='df-row'][div[contains(text(), 'Organization:')]]/div[@class='df-value']/text()",
        )
        domain_info.add_xpath(
            "tech_street",
            "//div[@class='df-block'][div[@class='df-heading'][contains(text(), 'Technical Contact')]]//div[@class='df-row'][div[contains(text(), 'Street:')]]/div[@class='df-value']/text()",
        )
        domain_info.add_xpath(
            "tech_city",
            "//div[@class='df-block'][div[@class='df-heading'][contains(text(), 'Technical Contact')]]//div[@class='df-row'][div[contains(text(), 'City:')]]/div[@class='df-value']/text()",
        )
        domain_info.add_xpath(
            "tech_state",
            "//div[@class='df-block'][div[@class='df-heading'][contains(text(), 'Technical Contact')]]//div[@class='df-row'][div[contains(text(), 'State:')]]/div[@class='df-value']/text()",
        )
        domain_info.add_xpath(
            "tech_postal_code",
            "//div[@class='df-block'][div[@class='df-heading'][contains(text(), 'Technical Contact')]]//div[@class='df-row'][div[contains(text(), 'Postal Code:')]]/div[@class='df-value']/text()",
        )
        domain_info.add_xpath(
            "tech_country",
            "//div[@class='df-block'][div[@class='df-heading'][contains(text(), 'Technical Contact')]]//div[@class='df-row'][div[contains(text(), 'Country:')]]/div[@class='df-value']/text()",
        )
        domain_info.add_xpath(
            "tech_phone",
            "//div[@class='df-block'][div[@class='df-heading'][contains(text(), 'Technical Contact')]]//div[@class='df-row'][div[contains(text(), 'Phone:')]]/div[@class='df-value']/text()",
        )
        domain_info.add_xpath(
            "tech_fax",
            "//div[@class='df-block'][div[@class='df-heading'][contains(text(), 'Technical Contact')]]//div[@class='df-row'][div[contains(text(), 'Fax:')]]/div[@class='df-value']/text()",
        )
        # Raw domain info
        domain_info.add_xpath(
            "raw_data", "//pre[@id='registrarData'][@class='df-raw']/text()"
        )
        # Spider info
        domain_info.add_value("spider", self.name)
        domain_info.add_value("url", response.request.url)
        domain_info.add_value("scraping_date", datetime.now())

        yield domain_info.load_item()
