from pathlib import Path

import scrapy


class ZohoAPIDocsSpider(scrapy.Spider):
    name = "zoho_api_docs"

    def start_requests(self):
        urls = [
            "https://www.zoho.com/books/api/v3/invoices/#create-an-invoice",
            # "https://www.zoho.com/books/api/v3/invoices/#list-invoices",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for api in response.css("div.wrapper"):
            print(f"api: {api}")
            h2_element = api.css("h2")
            description_element = api.css("h2 ~ p")
            arguments_element = api.css("h2 ~ h3#arguments ~ div.parameter")

            name = h2_element.css("::text").get()
            api_description = description_element.css("::text").get()

            arguments = []
            for property_element in arguments_element.css("div.row"):
                argument_name = property_element.css("div.property ::text").get()
                argument_data_type = property_element.css("div.property-datatype ::text").get()
                argument_kind = property_element.css("div.row div.property-kind::attr('id')").get()
                argument_description = property_element.css("div.prop-descrip ::text").get()
                argument = {
                    'name': argument_name.strip() if argument_name is not None else '',
                    'data_type': argument_data_type.strip() if argument_data_type is not None else '',
                    'required': argument_kind,
                    'description': argument_description,
                }
                arguments.append(argument)

            if name is not None:
                yield {
                    "name": name.strip(),
                    "description": api_description.strip(),
                    "arguments": arguments,
                }

    def parse_old(self, response):
        page = response.url.split("/")[-2]
        filename = f"zoho-api-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")

# response.css("h2::text").getall() : list of apis
#  response.css("div.wrapper h2 ~ h3#arguments ~ div.parameter").css("div.row").css("div.property ::text").getall()
# scrapy crawl zoho_api_docs -O apis.json
# scrapy shell 'https://www.zoho.com/books/api/v3/invoices/#create-an-invoice'