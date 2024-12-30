from pathlib import Path

import scrapy

from scrapy.http.response import Response
from typing import Any


class ZohoAPIDocsSpider(scrapy.Spider):
    name = "zoho_api_docs"

    def start_requests(self):
        urls = [
            "https://www.zoho.com/books/api/v3/invoices/#create-an-invoice",
            # "https://www.zoho.com/books/api/v3/invoices/#list-invoices",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response: Response, **kwargs: Any) -> Any:
        for endpoint in response.css("div.endpoints-wrapper > div.endpoints-innerwrapper a"):
            endpoint_doc_url = endpoint.css("::attr('href')").get()
            endpoint_content = endpoint.css("div.endpoints-content")
            http_method = endpoint_content.css("div.endpoints-bottom-text-method ::text").get()
            http_method = http_method.strip() if http_method is not None else 'N/A'
            url_path = endpoint_content.css("div.endpoints-bottom-text-url ::text").get()
            path_parameters = extract_path_parameters(url_path)
            splits = endpoint_doc_url.split("#")
            if len(splits) == 2:
                h2_id = splits[1]
            else:
                h2_id = "N/A"

            h2_element = response.css(f"h2#{h2_id} ")
            api_doc_element = h2_element.xpath('..').xpath('..').xpath('..')

            api_doc = self.parse_api_doc(api_doc_element)

            yield {"endpoint_doc_url": endpoint_doc_url,
                   "http_method": http_method,
                   "url_path": url_path,
                   "h2_id": h2_id,
                   "path_parameters": path_parameters,
                   "api_doc": api_doc,
                   }

    def parse_api_doc(self, api):
        print(f"api: {api}")
        h2_element = api.css("h2")
        description_element = api.css("h2 ~ p")
        arguments_element = api.css("h2 ~ h3#arguments + div.parameter")
        query_param_element = api.css("h2 ~ h3#queryparams + div.parameter")
        name = h2_element.css("::text").get()
        api_description = description_element.css("::text").get()
        arguments = []
        for property_element in arguments_element.css("div.row"):
            is_sub_attribute = False if len(property_element.xpath('ancestor::details').getall()) == 0 else True
            if is_sub_attribute:
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

            sub_attributes = []
            sub_attribute_elements = property_element.css("details div.attribute-wrapper div.attribute "
                                                          "div.property-wrapper")
            for sub_attribute_element in sub_attribute_elements:
                sub_attribute = {
                    'name': sub_attribute_element.css("div.property ::text").get().strip(),
                    'data_type': sub_attribute_element.css("div.property-datatype ::text").get().strip(),
                    'required': sub_attribute_element.css("div.property-kind::attr('id')").get().strip(),
                }
                if len(sub_attribute_element.css("div.prop-descrip").getall()) > 0:
                    sub_attribute['description'] = sub_attribute_element.css("div.prop-descrip ::text").get().strip()
                else:
                    sub_attribute['description'] = ""

                sub_attributes.append(sub_attribute)
            if len(sub_attributes) > 0:
                argument['sub_attributes'] = sub_attributes

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
                'data_type': 'string',
                'required': param_kind,
                'description': param_description,
            }
            query_params.append(param)
        if name is not None:
            return {
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


import re


def extract_path_parameters(endpoint: str) -> list[str]:
    # Use a regular expression to find all strings within curly braces
    return re.findall(r'\{(.*?)\}', endpoint)

# response.css("h2::text").getall() : list of apis
#  response.css("div.wrapper h2 ~ h3#arguments ~ div.parameter").css("div.row").css("div.property ::text").getall()
# scrapy crawl zoho_api_docs -O apis.json
# scrapy shell 'https://www.zoho.com/books/api/v3/invoices/#create-an-invoice'
