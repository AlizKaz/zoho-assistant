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
            query_param_element = api.css("h2 ~h3#queryparams ~ div.parameter")

            name = h2_element.css("::text").get()
            api_description = description_element.css("::text").get()

            arguments = []
            for property_element in arguments_element.css("div.row"):
                sub_attribute = False if len(property_element.xpath('ancestor::details').getall()) == 0 else True
                if sub_attribute:
                    continue
                argument_name = property_element.css("div.property ::text").get()
                argument_name = argument_name.strip() if argument_name is not None else ''
                argument_data_type = property_element.css("div.property-datatype ::text").get()
                argument_data_type = argument_data_type.strip() if argument_data_type is not None else ''
                argument_kind = property_element.css("div.property-kind::attr('id')").get()
                argument_description = property_element.css("div.prop-descrip ::text").get()
                availability_info = property_element.css("*.availability-info-wrapper span ::text").get()
                argument = {
                    'name': argument_name,
                    'data_type': argument_data_type,
                    'required': argument_kind,
                    'description': argument_description,
                }
                if availability_info is not None:
                    argument['availability_info'] = availability_info.strip()

                arguments.append(argument)

                if argument_description is not None and "Variants" in argument_description:
                    variants = property_element.css("div.prop-descrip code ::text").getall()
                    for variant_name in variants:
                        variant = {
                            'name': variant_name.strip(),
                            'data_type': argument_data_type.strip() if argument_data_type is not None else '',
                            'required': argument_kind,
                            'description': argument_description,
                            'variant': "true",
                            'variant_of': argument_name
                        }
                        if availability_info is not None:
                            argument['availability_info'] = availability_info.strip()
                        arguments.append(variant)


            query_params = []
            for property_element in query_param_element.css("div.row"):
                param_name = property_element.css("div.property ::text").get()
                param_data_type = property_element.css("div.property-datatype ::text").get()
                param_kind = property_element.css("div.row div.property-kind::attr('id')").get()
                param_description = property_element.css("div.prop-descrip ::text").get()
                param = {
                    'name': param_name.strip() if param_name is not None else '',
                    'data_type': param_data_type.strip() if param_data_type is not None else '',
                    'required': param_kind,
                    'description': param_description,
                }
                query_params.append(param)

            if name is not None:
                yield {
                    "name": name.strip(),
                    "description": api_description.strip(),
                    "arguments": arguments,
                    "query_params": query_params,
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
