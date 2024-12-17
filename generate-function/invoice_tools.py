tools = [
    {
        "type": "function",
        "function": {
            "name": "create_an_invoice",
            "description": "Create an invoice for your customer.",
            "parameters": {
                "type": "object",
                "properties": {
                    "customer_id": {
                        "type": "string",
                        "description": "ID of the customer the invoice has to be created."
                    },
                    "currency_id": {
                        "type": "string",
                        "description": "The currency id of the currency"
                    },
                    "contact_persons": {
                        "type": "array",
                        "description": "Array of contact person(s) for whom invoice has to be sent.",
                        "items": {
                            "type": "string"
                        }
                    },
                    "invoice_number": {
                        "type": "string",
                        "description": "Search invoices by invoice number.Variants: "
                    },
                    "invoice_number_startswith": {
                        "type": "string",
                        "description": "Search invoices by invoice number.Variants: "
                    },
                    "invoice_number_contains": {
                        "type": "string",
                        "description": "Search invoices by invoice number.Variants: "
                    },
                    "place_of_supply": {
                        "type": "string",
                        "description": "Place where the goods/services are supplied to. (If not given, "
                    },
                    "vat_treatment": {
                        "type": "string",
                        "description": "(Optional) VAT treatment for the invoices. VAT treatment denotes the location of the customer, if the customer resides in UK then the VAT treatment is "
                    },
                    "tax_treatment": {
                        "type": "string",
                        "description": "VAT treatment for the invoice .Choose whether the contact falls under: "
                    },
                    "is_reverse_charge_applied": {
                        "type": "boolean",
                        "description": "(Required if customer tax treatment is "
                    },
                    "gst_treatment": {
                        "type": "string",
                        "description": "Choose whether the contact is GST registered/unregistered/consumer/overseas. Allowed values are "
                    },
                    "gst_no": {
                        "type": "string",
                        "description": "15 digit GST identification number of the customer."
                    },
                    "cfdi_usage": {
                        "type": "string",
                        "description": "Choose CFDI Usage. Allowed values:"
                    },
                    "reference_number": {
                        "type": "string",
                        "description": "The reference number of the invoice"
                    },
                    "template_id": {
                        "type": "string",
                        "description": "ID of the pdf template associated with the invoice."
                    },
                    "date": {
                        "type": "string",
                        "description": "Search invoices by invoice date. Default date format is yyyy-mm-dd."
                    },
                    "payment_terms": {
                        "type": "integer",
                        "description": "Payment terms in days e.g. 15, 30, 60. Invoice due date will be calculated based on this. Max-length [100]"
                    },
                    "payment_terms_label": {
                        "type": "string",
                        "description": "Used to override the default payment terms label. Default value for 15 days is \"Net 15 Days\". Max-length [100]"
                    },
                    "due_date": {
                        "type": "string",
                        "description": "Search invoices by due date. Default date format is yyyy-mm-dd. "
                    },
                    "discount": {
                        "type": "number",
                        "description": "Discount applied to the invoice. It can be either in % or in amount. e.g. 12.5% or 190. Max-length [100]"
                    },
                    "is_discount_before_tax": {
                        "type": "boolean",
                        "description": "Used to specify how the discount has to applied. Either before or after the calculation of tax."
                    },
                    "discount_type": {
                        "type": "string",
                        "description": "How the discount is specified. Allowed values: "
                    },
                    "is_inclusive_tax": {
                        "type": "boolean",
                        "description": "Used to specify whether the line item rates are inclusive or exclusivr of tax."
                    },
                    "exchange_rate": {
                        "type": "number",
                        "description": "Exchange rate of the currency."
                    },
                    "recurring_invoice_id": {
                        "type": "string",
                        "description": "ID of the recurring invoice from which the invoice is created."
                    },
                    "invoiced_estimate_id": {
                        "type": "string",
                        "description": "ID of the invoice from which the invoice is created."
                    },
                    "salesperson_name": {
                        "type": "string",
                        "description": "Name of the salesperson. Max-length [200]"
                    },
                    "custom_fields": {
                        "type": "array",
                        "description": "Custom fields for an invoice.",
                        "items": {
                            "type": "object",
                            "properties": {
                                "customfield_id": {
                                    "type": "integer",
                                    "description": ""
                                },
                                "value": {
                                    "type": "string",
                                    "description": "Value of the Custom Field"
                                }
                            }
                        }
                    },
                    "line_items": {
                        "type": "array",
                        "description": "Search invoices by item id.",
                        "items": {
                            "type": "object",
                            "properties": {
                                "item_id": {
                                    "type": "string",
                                    "description": "Search invoices by item id."
                                },
                                "project_id": {
                                    "type": "string",
                                    "description": "ID of the Project."
                                },
                                "time_entry_ids": {
                                    "type": "array",
                                    "description": "IDs of the time entries associated with the project.",
                                    "items": {
                                        "type": "string"
                                    }
                                },
                                "product_type": {
                                    "type": "string",
                                    "description": "Enter"
                                },
                                "hsn_or_sac": {
                                    "type": "string",
                                    "description": "Add HSN/SAC code for your goods/services"
                                },
                                "sat_item_key_code": {
                                    "type": "string",
                                    "description": "Add SAT Item Key Code for your goods/services. Download the"
                                },
                                "unitkey_code": {
                                    "type": "string",
                                    "description": "Add SAT Unit Key Code for your goods/services. Download the"
                                },
                                "warehouse_id": {
                                    "type": "string",
                                    "description": "Enter warehouse ID"
                                },
                                "expense_id": {
                                    "type": "string",
                                    "description": "Add billable expense id which needs to be convert to invoice"
                                },
                                "bill_id": {
                                    "type": "string",
                                    "description": "Add billable bill id which needs to be convert to invoice"
                                },
                                "bill_item_id": {
                                    "type": "string",
                                    "description": "Add billable bill item id which needs to be convert to invoice"
                                },
                                "expense_receipt_name": {
                                    "type": "string",
                                    "description": ""
                                },
                                "name": {
                                    "type": "string",
                                    "description": "The name of the line item. Max-length [100]"
                                },
                                "description": {
                                    "type": "string",
                                    "description": "The description of the line items. Max-length [2000]"
                                },
                                "item_order": {
                                    "type": "integer",
                                    "description": "The order of the line item_order"
                                },
                                "bcy_rate": {
                                    "type": "number",
                                    "description": "base currency rate"
                                },
                                "rate": {
                                    "type": "number",
                                    "description": "Rate of the line item."
                                },
                                "quantity": {
                                    "type": "number",
                                    "description": "The quantity of line item"
                                },
                                "unit": {
                                    "type": "string",
                                    "description": "Unit of the line item e.g. kgs, Nos. Max-length [100]"
                                },
                                "discount_amount": {
                                    "type": "number",
                                    "description": "The discount amount on the line item"
                                },
                                "discount": {
                                    "type": "number",
                                    "description": "Discount applied to the invoice. It can be either in % or in amount. e.g. 12.5% or 190. Max-length [100]"
                                },
                                "tags": {
                                    "type": "array",
                                    "description": "Filter all your reports based on the tag",
                                    "items": {
                                        "type": "string"
                                    }
                                },
                                "tag_id": {
                                    "type": "string",
                                    "description": "ID of the reporting tag"
                                },
                                "tag_option_id": {
                                    "type": "string",
                                    "description": "ID of the reporting tag's option"
                                },
                                "tax_id": {
                                    "type": "string",
                                    "description": "ID of the tax."
                                },
                                "tds_tax_id": {
                                    "type": "string",
                                    "description": "ID of the TDS tax."
                                },
                                "tax_name": {
                                    "type": "string",
                                    "description": "The name of the tax"
                                },
                                "tax_type": {
                                    "type": "string",
                                    "description": "The type of the tax"
                                },
                                "tax_percentage": {
                                    "type": "number",
                                    "description": "The  percentage of tax levied"
                                },
                                "tax_treatment_code": {
                                    "type": "string",
                                    "description": "Specify reason for using out of scope.Supported values for UAE are"
                                },
                                "header_name": {
                                    "type": "string",
                                    "description": "Name of the item header"
                                },
                                "salesorder_item_id": {
                                    "type": "string",
                                    "description": "ID of the sales order line item which is invoices."
                                }
                            }
                        }
                    },
                    "payment_options": {
                        "type": "object",
                        "description": "Payment options for the invoice, online payment gateways and bank accounts. Will be displayed in the pdf.",
                        "properties": {
                            "payment_gateways": {
                                "type": "array",
                                "description": "Online payment gateways through which payment can be made.",
                                "items": {
                                    "type": "string"
                                }
                            },
                            "configured": {
                                "type": "boolean",
                                "description": "Boolean check to see if a payment gateway has been configured"
                            },
                            "additional_field1": {
                                "type": "string",
                                "description": "Paypal payment method. Allowed Values:"
                            },
                            "gateway_name": {
                                "type": "string",
                                "description": "Name of the payment gateway associated with the invoice. E.g. paypal, stripe.Allowed Values:"
                            }
                        }
                    },
                    "allow_partial_payments": {
                        "type": "boolean",
                        "description": "Boolean to check if partial payments are allowed for the contact"
                    },
                    "custom_body": {
                        "type": "string",
                        "description": "no description provided"
                    },
                    "custom_subject": {
                        "type": "string",
                        "description": "no description provided"
                    },
                    "notes": {
                        "type": "string",
                        "description": "The notes added below expressing gratitude or for conveying some information."
                    },
                    "terms": {
                        "type": "string",
                        "description": "The terms added below expressing gratitude or for conveying some information."
                    },
                    "shipping_charge": {
                        "type": "string",
                        "description": "Shipping charges applied to the invoice. Max-length [100]"
                    },
                    "adjustment": {
                        "type": "number",
                        "description": "Adjustments made to the invoice."
                    },
                    "adjustment_description": {
                        "type": "string",
                        "description": "Customize the adjustment description. E.g. Rounding off."
                    },
                    "reason": {
                        "type": "string",
                        "description": "no description provided"
                    },
                    "tax_authority_id": {
                        "type": "string",
                        "description": "ID of the tax authority. Tax authority depends on the location of the customer. For example, if the customer is located in NY, then the tax authority is NY tax authority."
                    },
                    "tax_exemption_id": {
                        "type": "string",
                        "description": "ID of the tax exemption."
                    },
                    "billing_address_id": {
                        "type": "string",
                        "description": "This is the ID of the billing address you want to apply to the invoice. "
                    },
                    "shipping_address_id": {
                        "type": "string",
                        "description": "This is the ID of the shipping address you want to apply to the invoice. "
                    },
                    "avatax_use_code": {
                        "type": "string",
                        "description": "Used to group like customers for exemption purposes. It is a custom value that links customers to a tax rule. Select from Avalara [standard codes][1] or enter a custom code. Max-length [25]"
                    },
                    "avatax_exempt_no": {
                        "type": "string",
                        "description": "Exemption certificate number of the customer. Max-length [25]"
                    },
                    "tax_id": {
                        "type": "string",
                        "description": "ID of the tax."
                    },
                    "expense_id": {
                        "type": "string",
                        "description": "Add billable expense id which needs to be convert to invoice"
                    },
                    "salesorder_item_id": {
                        "type": "string",
                        "description": "ID of the sales order line item which is invoices."
                    },
                    "avatax_tax_code": {
                        "type": "string",
                        "description": "A tax code is a unique label used to group Items (products, services, or charges) together. Refer the [link][2] for more deails. Max-length [25]"
                    },
                    "time_entry_ids": {
                        "type": "array",
                        "description": "IDs of the time entries associated with the project.",
                        "items": {
                            "type": "string"
                        }
                    },
                    "send": {
                        "type": "string",
                        "description": "Send the invoice to the contact person(s) associated with the invoice. Allowed values "
                    },
                    "ignore_auto_number_generation": {
                        "type": "string",
                        "description": "Ignore auto invoice number generation for this invoice. This mandates the invoice number. Allowed values "
                    }
                },
                "required": [
                    "customer_id",
                    "line_items"
                ]
            },
            "required": [
                "customer_id",
                "line_items"
            ]
        }
    },
    {
        "type": "function",
        "function": {
            "name": "update_an_invoice_using_a_custom_field_s_unique_value",
            "description": "A custom field will have unique values if it's configured to not accept duplicate values. Now, you can use that custom field's value to update an invoice by providing its API name in the X-Unique-Identifier-Key header and its value in the X-Unique-Identifier-Value header. Based on this value, the corresponding invoice will be retrieved and updated. Additionally, there is an optional X-Upsert header. If the X-Upsert header is true and the custom field's unique value is not found in any of the existing invoices, a new invoice will be created if the necessary payload details are available",
            "parameters": {
                "type": "object",
                "properties": {
                    "customer_id": {
                        "type": "string",
                        "description": "ID of the customer the invoice has to be created."
                    },
                    "currency_id": {
                        "type": "string",
                        "description": "The currency id of the currency"
                    },
                    "contact_persons": {
                        "type": "array",
                        "description": "Array of contact person(s) for whom invoice has to be sent.",
                        "items": {
                            "type": "string"
                        }
                    },
                    "invoice_number": {
                        "type": "string",
                        "description": "Search invoices by invoice number.Variants: "
                    },
                    "invoice_number_startswith": {
                        "type": "string",
                        "description": "Search invoices by invoice number.Variants: "
                    },
                    "invoice_number_contains": {
                        "type": "string",
                        "description": "Search invoices by invoice number.Variants: "
                    },
                    "place_of_supply": {
                        "type": "string",
                        "description": "Place where the goods/services are supplied to. (If not given, "
                    },
                    "vat_treatment": {
                        "type": "string",
                        "description": "(Optional) VAT treatment for the invoices. VAT treatment denotes the location of the customer, if the customer resides in UK then the VAT treatment is "
                    },
                    "tax_treatment": {
                        "type": "string",
                        "description": "VAT treatment for the invoice .Choose whether the contact falls under: "
                    },
                    "is_reverse_charge_applied": {
                        "type": "boolean",
                        "description": "(Required if customer tax treatment is "
                    },
                    "gst_treatment": {
                        "type": "string",
                        "description": "Choose whether the contact is GST registered/unregistered/consumer/overseas. Allowed values are "
                    },
                    "cfdi_usage": {
                        "type": "string",
                        "description": "Choose CFDI Usage. Allowed values:"
                    },
                    "cfdi_reference_type": {
                        "type": "string",
                        "description": "Choose CFDI Reference Type. Allowed values:"
                    },
                    "reference_invoice_id": {
                        "type": "string",
                        "description": "Associate the reference invoice."
                    },
                    "gst_no": {
                        "type": "string",
                        "description": "15 digit GST identification number of the customer."
                    },
                    "reference_number": {
                        "type": "string",
                        "description": "The reference number of the invoice"
                    },
                    "template_id": {
                        "type": "string",
                        "description": "ID of the pdf template associated with the invoice."
                    },
                    "date": {
                        "type": "string",
                        "description": "Search invoices by invoice date. Default date format is yyyy-mm-dd."
                    },
                    "payment_terms": {
                        "type": "integer",
                        "description": "Payment terms in days e.g. 15, 30, 60. Invoice due date will be calculated based on this. Max-length [100]"
                    },
                    "payment_terms_label": {
                        "type": "string",
                        "description": "Used to override the default payment terms label. Default value for 15 days is \"Net 15 Days\". Max-length [100]"
                    },
                    "due_date": {
                        "type": "string",
                        "description": "Search invoices by due date. Default date format is yyyy-mm-dd. "
                    },
                    "discount": {
                        "type": "number",
                        "description": "Discount applied to the invoice. It can be either in % or in amount. e.g. 12.5% or 190. Max-length [100]"
                    },
                    "is_discount_before_tax": {
                        "type": "boolean",
                        "description": "Used to specify how the discount has to applied. Either before or after the calculation of tax."
                    },
                    "discount_type": {
                        "type": "string",
                        "description": "How the discount is specified. Allowed values: "
                    },
                    "is_inclusive_tax": {
                        "type": "boolean",
                        "description": "Used to specify whether the line item rates are inclusive or exclusivr of tax."
                    },
                    "exchange_rate": {
                        "type": "number",
                        "description": "Exchange rate of the currency."
                    },
                    "recurring_invoice_id": {
                        "type": "string",
                        "description": "ID of the recurring invoice from which the invoice is created."
                    },
                    "invoiced_estimate_id": {
                        "type": "string",
                        "description": "ID of the invoice from which the invoice is created."
                    },
                    "salesperson_name": {
                        "type": "string",
                        "description": "Name of the salesperson. Max-length [200]"
                    },
                    "custom_fields": {
                        "type": "array",
                        "description": "Custom fields for an invoice.",
                        "items": {
                            "type": "object",
                            "properties": {
                                "customfield_id": {
                                    "type": "integer",
                                    "description": ""
                                },
                                "value": {
                                    "type": "string",
                                    "description": "Value of the Custom Field"
                                }
                            }
                        }
                    },
                    "line_items": {
                        "type": "array",
                        "description": "Search invoices by item id.",
                        "items": {
                            "type": "object",
                            "properties": {
                                "item_id": {
                                    "type": "string",
                                    "description": "Search invoices by item id."
                                },
                                "project_id": {
                                    "type": "string",
                                    "description": "ID of the Project."
                                },
                                "time_entry_ids": {
                                    "type": "array",
                                    "description": "IDs of the time entries associated with the project.",
                                    "items": {
                                        "type": "string"
                                    }
                                },
                                "product_type": {
                                    "type": "string",
                                    "description": "Enter"
                                },
                                "hsn_or_sac": {
                                    "type": "string",
                                    "description": "Add HSN/SAC code for your goods/services"
                                },
                                "sat_item_key_code": {
                                    "type": "string",
                                    "description": "Add SAT Item Key Code for your goods/services. Download the"
                                },
                                "unitkey_code": {
                                    "type": "string",
                                    "description": "Add SAT Unit Key Code for your goods/services. Download the"
                                },
                                "warehouse_id": {
                                    "type": "string",
                                    "description": "Enter warehouse ID"
                                },
                                "expense_id": {
                                    "type": "string",
                                    "description": "Add billable expense id which needs to be convert to invoice"
                                },
                                "expense_receipt_name": {
                                    "type": "string",
                                    "description": ""
                                },
                                "name": {
                                    "type": "string",
                                    "description": "The name of the line item. Max-length [100]"
                                },
                                "description": {
                                    "type": "string",
                                    "description": "The description of the line items. Max-length [2000]"
                                },
                                "item_order": {
                                    "type": "integer",
                                    "description": "The order of the line item_order"
                                },
                                "bcy_rate": {
                                    "type": "number",
                                    "description": "base currency rate"
                                },
                                "rate": {
                                    "type": "number",
                                    "description": "Rate of the line item."
                                },
                                "quantity": {
                                    "type": "number",
                                    "description": "The quantity of line item"
                                },
                                "unit": {
                                    "type": "string",
                                    "description": "Unit of the line item e.g. kgs, Nos. Max-length [100]"
                                },
                                "discount_amount": {
                                    "type": "number",
                                    "description": "The discount amount on the line item"
                                },
                                "tags": {
                                    "type": "array",
                                    "description": "Filter all your reports based on the tag",
                                    "items": {
                                        "type": "string"
                                    }
                                },
                                "tag_id": {
                                    "type": "string",
                                    "description": "ID of the reporting tag"
                                },
                                "tag_option_id": {
                                    "type": "string",
                                    "description": "ID of the reporting tag's option"
                                },
                                "discount": {
                                    "type": "number",
                                    "description": "Discount applied to the invoice. It can be either in % or in amount. e.g. 12.5% or 190. Max-length [100]"
                                },
                                "tax_id": {
                                    "type": "string",
                                    "description": "ID of the tax."
                                },
                                "tds_tax_id": {
                                    "type": "string",
                                    "description": "ID of the TDS tax."
                                },
                                "tax_name": {
                                    "type": "string",
                                    "description": "The name of the tax"
                                },
                                "tax_type": {
                                    "type": "string",
                                    "description": "The type of the tax"
                                },
                                "tax_percentage": {
                                    "type": "number",
                                    "description": "The  percentage of tax levied"
                                },
                                "tax_treatment_code": {
                                    "type": "string",
                                    "description": "Specify reason for using out of scope.Supported values for UAE are"
                                },
                                "header_name": {
                                    "type": "string",
                                    "description": "Name of the item header"
                                },
                                "header_id": {
                                    "type": "string",
                                    "description": "ID of the item header"
                                }
                            }
                        }
                    },
                    "payment_options": {
                        "type": "object",
                        "description": "Payment options for the invoice, online payment gateways and bank accounts. Will be displayed in the pdf.",
                        "properties": {
                            "payment_gateways": {
                                "type": "array",
                                "description": "Online payment gateways through which payment can be made.",
                                "items": {
                                    "type": "string"
                                }
                            },
                            "configured": {
                                "type": "boolean",
                                "description": "Boolean check to see if a payment gateway has been configured"
                            },
                            "additional_field1": {
                                "type": "string",
                                "description": "Paypal payment method. Allowed Values:"
                            },
                            "gateway_name": {
                                "type": "string",
                                "description": "Name of the payment gateway associated with the invoice. E.g. paypal, stripe.Allowed Values:"
                            }
                        }
                    },
                    "allow_partial_payments": {
                        "type": "boolean",
                        "description": "Boolean to check if partial payments are allowed for the contact"
                    },
                    "custom_body": {
                        "type": "string",
                        "description": "no description provided"
                    },
                    "custom_subject": {
                        "type": "string",
                        "description": "no description provided"
                    },
                    "notes": {
                        "type": "string",
                        "description": "The notes added below expressing gratitude or for conveying some information."
                    },
                    "terms": {
                        "type": "string",
                        "description": "The terms added below expressing gratitude or for conveying some information."
                    },
                    "shipping_charge": {
                        "type": "string",
                        "description": "Shipping charges applied to the invoice. Max-length [100]"
                    },
                    "adjustment": {
                        "type": "number",
                        "description": "Adjustments made to the invoice."
                    },
                    "adjustment_description": {
                        "type": "string",
                        "description": "Customize the adjustment description. E.g. Rounding off."
                    },
                    "reason": {
                        "type": "string",
                        "description": "no description provided"
                    },
                    "tax_authority_id": {
                        "type": "string",
                        "description": "ID of the tax authority. Tax authority depends on the location of the customer. For example, if the customer is located in NY, then the tax authority is NY tax authority."
                    },
                    "tax_exemption_id": {
                        "type": "string",
                        "description": "ID of the tax exemption."
                    },
                    "avatax_use_code": {
                        "type": "string",
                        "description": "Used to group like customers for exemption purposes. It is a custom value that links customers to a tax rule. Select from Avalara [standard codes][1] or enter a custom code. Max-length [25]"
                    },
                    "avatax_exempt_no": {
                        "type": "string",
                        "description": "Exemption certificate number of the customer. Max-length [25]"
                    },
                    "tax_id": {
                        "type": "string",
                        "description": "ID of the tax."
                    },
                    "expense_id": {
                        "type": "string",
                        "description": "Add billable expense id which needs to be convert to invoice"
                    },
                    "salesorder_item_id": {
                        "type": "string",
                        "description": "ID of the sales order line item which is invoices."
                    },
                    "avatax_tax_code": {
                        "type": "string",
                        "description": "A tax code is a unique label used to group Items (products, services, or charges) together. Refer the [link][2] for more deails. Max-length [25]"
                    },
                    "line_item_id": {
                        "type": "string",
                        "description": "The line item id"
                    }
                },
                "required": [
                    "customer_id",
                    "line_items"
                ]
            },
            "required": [
                "customer_id",
                "line_items"
            ]
        }
    },
    {
        "type": "function",
        "function": {
            "name": "list_invoices",
            "description": "List all invoices with pagination.",
            "parameters": {
                "type": "object",
                "properties": {
                    "invoice_number": {
                        "type": "string",
                        "description": "Search invoices by invoice number.Variants: "
                    },
                    "item_name": {
                        "type": "string",
                        "description": "Search invoices by item name.Variants: "
                    },
                    "item_id": {
                        "type": "string",
                        "description": "Search invoices by item id."
                    },
                    "item_description": {
                        "type": "string",
                        "description": "Search invoices by item description.Variants: "
                    },
                    "reference_number": {
                        "type": "string",
                        "description": "The reference number of the invoice"
                    },
                    "customer_name": {
                        "type": "string",
                        "description": "The name of the customer. Max-length [100]"
                    },
                    "recurring_invoice_id": {
                        "type": "string",
                        "description": "ID of the recurring invoice from which the invoice is created."
                    },
                    "email": {
                        "type": "string",
                        "description": "Search contacts by email id. Max-length [100]"
                    },
                    "total": {
                        "type": "string",
                        "description": "The total amount to be paid"
                    },
                    "balance": {
                        "type": "string",
                        "description": "The unpaid amount"
                    },
                    "custom_field": {
                        "type": "string",
                        "description": "Search invoices by custom fields.Variants: "
                    },
                    "date": {
                        "type": "string",
                        "description": "Search invoices by invoice date. Default date format is yyyy-mm-dd."
                    },
                    "due_date": {
                        "type": "string",
                        "description": "Search invoices by due date. Default date format is yyyy-mm-dd. "
                    },
                    "last_modified_time": {
                        "type": "string",
                        "description": "This filters invoices generated after the last_modified_time that is greater than the specified param value. Allowed format "
                    },
                    "status": {
                        "type": "string",
                        "description": "Search invoices by invoice status.Allowed Values: "
                    },
                    "customer_id": {
                        "type": "string",
                        "description": "ID of the customer the invoice has to be created."
                    },
                    "filter_by": {
                        "type": "string",
                        "description": "Filter invoices by any status or payment expected date.Allowed Values: "
                    },
                    "search_text": {
                        "type": "string",
                        "description": "Search invoices by invoice number or purchase order or customer name. Max-length [100]"
                    },
                    "sort_column": {
                        "type": "string",
                        "description": "Sort invoices.Allowed Values: "
                    },
                    "zcrm_potential_id": {
                        "type": "string",
                        "description": "Potential ID of a Deal in CRM."
                    },
                    "response_option": {
                        "type": "string",
                        "description": "To get desired response format. There are 5 formats of responses: 0 (Includes all invoices), 1 (Includes all invoices, the number of invoices, and the sum of their total and balance amounts), 2 (Includes only the number of invoices), 3 (Includes the number of invoices and the sum of their total and balance amounts), and 4 (Includes all invoices and the sum of their total and balance amounts)."
                    }
                },
                "required": []
            },
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "update_an_invoice",
            "description": "Update an existing invoice. To delete a line item just remove it from the line_items list.",
            "parameters": {
                "type": "object",
                "properties": {
                    "customer_id": {
                        "type": "string",
                        "description": "ID of the customer the invoice has to be created."
                    },
                    "currency_id": {
                        "type": "string",
                        "description": "The currency id of the currency"
                    },
                    "contact_persons": {
                        "type": "array",
                        "description": "Array of contact person(s) for whom invoice has to be sent.",
                        "items": {
                            "type": "string"
                        }
                    },
                    "invoice_number": {
                        "type": "string",
                        "description": "Search invoices by invoice number.Variants: "
                    },
                    "invoice_number_startswith": {
                        "type": "string",
                        "description": "Search invoices by invoice number.Variants: "
                    },
                    "invoice_number_contains": {
                        "type": "string",
                        "description": "Search invoices by invoice number.Variants: "
                    },
                    "place_of_supply": {
                        "type": "string",
                        "description": "Place where the goods/services are supplied to. (If not given, "
                    },
                    "vat_treatment": {
                        "type": "string",
                        "description": "(Optional) VAT treatment for the invoices. VAT treatment denotes the location of the customer, if the customer resides in UK then the VAT treatment is "
                    },
                    "tax_treatment": {
                        "type": "string",
                        "description": "VAT treatment for the invoice .Choose whether the contact falls under: "
                    },
                    "is_reverse_charge_applied": {
                        "type": "boolean",
                        "description": "(Required if customer tax treatment is "
                    },
                    "gst_treatment": {
                        "type": "string",
                        "description": "Choose whether the contact is GST registered/unregistered/consumer/overseas. Allowed values are "
                    },
                    "cfdi_usage": {
                        "type": "string",
                        "description": "Choose CFDI Usage. Allowed values:"
                    },
                    "cfdi_reference_type": {
                        "type": "string",
                        "description": "Choose CFDI Reference Type. Allowed values:"
                    },
                    "reference_invoice_id": {
                        "type": "string",
                        "description": "Associate the reference invoice."
                    },
                    "gst_no": {
                        "type": "string",
                        "description": "15 digit GST identification number of the customer."
                    },
                    "reference_number": {
                        "type": "string",
                        "description": "The reference number of the invoice"
                    },
                    "template_id": {
                        "type": "string",
                        "description": "ID of the pdf template associated with the invoice."
                    },
                    "date": {
                        "type": "string",
                        "description": "Search invoices by invoice date. Default date format is yyyy-mm-dd."
                    },
                    "payment_terms": {
                        "type": "integer",
                        "description": "Payment terms in days e.g. 15, 30, 60. Invoice due date will be calculated based on this. Max-length [100]"
                    },
                    "payment_terms_label": {
                        "type": "string",
                        "description": "Used to override the default payment terms label. Default value for 15 days is \"Net 15 Days\". Max-length [100]"
                    },
                    "due_date": {
                        "type": "string",
                        "description": "Search invoices by due date. Default date format is yyyy-mm-dd. "
                    },
                    "discount": {
                        "type": "number",
                        "description": "Discount applied to the invoice. It can be either in % or in amount. e.g. 12.5% or 190. Max-length [100]"
                    },
                    "is_discount_before_tax": {
                        "type": "boolean",
                        "description": "Used to specify how the discount has to applied. Either before or after the calculation of tax."
                    },
                    "discount_type": {
                        "type": "string",
                        "description": "How the discount is specified. Allowed values: "
                    },
                    "is_inclusive_tax": {
                        "type": "boolean",
                        "description": "Used to specify whether the line item rates are inclusive or exclusivr of tax."
                    },
                    "exchange_rate": {
                        "type": "number",
                        "description": "Exchange rate of the currency."
                    },
                    "recurring_invoice_id": {
                        "type": "string",
                        "description": "ID of the recurring invoice from which the invoice is created."
                    },
                    "invoiced_estimate_id": {
                        "type": "string",
                        "description": "ID of the invoice from which the invoice is created."
                    },
                    "salesperson_name": {
                        "type": "string",
                        "description": "Name of the salesperson. Max-length [200]"
                    },
                    "custom_fields": {
                        "type": "array",
                        "description": "Custom fields for an invoice.",
                        "items": {
                            "type": "object",
                            "properties": {
                                "customfield_id": {
                                    "type": "integer",
                                    "description": ""
                                },
                                "value": {
                                    "type": "string",
                                    "description": "Value of the Custom Field"
                                }
                            }
                        }
                    },
                    "line_items": {
                        "type": "array",
                        "description": "Search invoices by item id.",
                        "items": {
                            "type": "object",
                            "properties": {
                                "item_id": {
                                    "type": "string",
                                    "description": "Search invoices by item id."
                                },
                                "project_id": {
                                    "type": "string",
                                    "description": "ID of the Project."
                                },
                                "time_entry_ids": {
                                    "type": "array",
                                    "description": "IDs of the time entries associated with the project.",
                                    "items": {
                                        "type": "string"
                                    }
                                },
                                "product_type": {
                                    "type": "string",
                                    "description": "Enter"
                                },
                                "hsn_or_sac": {
                                    "type": "string",
                                    "description": "Add HSN/SAC code for your goods/services"
                                },
                                "sat_item_key_code": {
                                    "type": "string",
                                    "description": "Add SAT Item Key Code for your goods/services. Download the"
                                },
                                "unitkey_code": {
                                    "type": "string",
                                    "description": "Add SAT Unit Key Code for your goods/services. Download the"
                                },
                                "warehouse_id": {
                                    "type": "string",
                                    "description": "Enter warehouse ID"
                                },
                                "expense_id": {
                                    "type": "string",
                                    "description": "Add billable expense id which needs to be convert to invoice"
                                },
                                "expense_receipt_name": {
                                    "type": "string",
                                    "description": ""
                                },
                                "name": {
                                    "type": "string",
                                    "description": "The name of the line item. Max-length [100]"
                                },
                                "description": {
                                    "type": "string",
                                    "description": "The description of the line items. Max-length [2000]"
                                },
                                "item_order": {
                                    "type": "integer",
                                    "description": "The order of the line item_order"
                                },
                                "bcy_rate": {
                                    "type": "number",
                                    "description": "base currency rate"
                                },
                                "rate": {
                                    "type": "number",
                                    "description": "Rate of the line item."
                                },
                                "quantity": {
                                    "type": "number",
                                    "description": "The quantity of line item"
                                },
                                "unit": {
                                    "type": "string",
                                    "description": "Unit of the line item e.g. kgs, Nos. Max-length [100]"
                                },
                                "discount_amount": {
                                    "type": "number",
                                    "description": "The discount amount on the line item"
                                },
                                "tags": {
                                    "type": "array",
                                    "description": "Filter all your reports based on the tag",
                                    "items": {
                                        "type": "string"
                                    }
                                },
                                "tag_id": {
                                    "type": "string",
                                    "description": "ID of the reporting tag"
                                },
                                "tag_option_id": {
                                    "type": "string",
                                    "description": "ID of the reporting tag's option"
                                },
                                "discount": {
                                    "type": "number",
                                    "description": "Discount applied to the invoice. It can be either in % or in amount. e.g. 12.5% or 190. Max-length [100]"
                                },
                                "tax_id": {
                                    "type": "string",
                                    "description": "ID of the tax."
                                },
                                "tds_tax_id": {
                                    "type": "string",
                                    "description": "ID of the TDS tax."
                                },
                                "tax_name": {
                                    "type": "string",
                                    "description": "The name of the tax"
                                },
                                "tax_type": {
                                    "type": "string",
                                    "description": "The type of the tax"
                                },
                                "tax_percentage": {
                                    "type": "number",
                                    "description": "The  percentage of tax levied"
                                },
                                "tax_treatment_code": {
                                    "type": "string",
                                    "description": "Specify reason for using out of scope.Supported values for UAE are"
                                },
                                "header_name": {
                                    "type": "string",
                                    "description": "Name of the item header"
                                },
                                "header_id": {
                                    "type": "string",
                                    "description": "ID of the item header"
                                }
                            }
                        }
                    },
                    "payment_options": {
                        "type": "object",
                        "description": "Payment options for the invoice, online payment gateways and bank accounts. Will be displayed in the pdf.",
                        "properties": {
                            "payment_gateways": {
                                "type": "array",
                                "description": "Online payment gateways through which payment can be made.",
                                "items": {
                                    "type": "string"
                                }
                            },
                            "configured": {
                                "type": "boolean",
                                "description": "Boolean check to see if a payment gateway has been configured"
                            },
                            "additional_field1": {
                                "type": "string",
                                "description": "Paypal payment method. Allowed Values:"
                            },
                            "gateway_name": {
                                "type": "string",
                                "description": "Name of the payment gateway associated with the invoice. E.g. paypal, stripe.Allowed Values:"
                            }
                        }
                    },
                    "allow_partial_payments": {
                        "type": "boolean",
                        "description": "Boolean to check if partial payments are allowed for the contact"
                    },
                    "custom_body": {
                        "type": "string",
                        "description": "no description provided"
                    },
                    "custom_subject": {
                        "type": "string",
                        "description": "no description provided"
                    },
                    "notes": {
                        "type": "string",
                        "description": "The notes added below expressing gratitude or for conveying some information."
                    },
                    "terms": {
                        "type": "string",
                        "description": "The terms added below expressing gratitude or for conveying some information."
                    },
                    "shipping_charge": {
                        "type": "string",
                        "description": "Shipping charges applied to the invoice. Max-length [100]"
                    },
                    "adjustment": {
                        "type": "number",
                        "description": "Adjustments made to the invoice."
                    },
                    "adjustment_description": {
                        "type": "string",
                        "description": "Customize the adjustment description. E.g. Rounding off."
                    },
                    "reason": {
                        "type": "string",
                        "description": "no description provided"
                    },
                    "tax_authority_id": {
                        "type": "string",
                        "description": "ID of the tax authority. Tax authority depends on the location of the customer. For example, if the customer is located in NY, then the tax authority is NY tax authority."
                    },
                    "tax_exemption_id": {
                        "type": "string",
                        "description": "ID of the tax exemption."
                    },
                    "avatax_use_code": {
                        "type": "string",
                        "description": "Used to group like customers for exemption purposes. It is a custom value that links customers to a tax rule. Select from Avalara [standard codes][1] or enter a custom code. Max-length [25]"
                    },
                    "avatax_exempt_no": {
                        "type": "string",
                        "description": "Exemption certificate number of the customer. Max-length [25]"
                    },
                    "tax_id": {
                        "type": "string",
                        "description": "ID of the tax."
                    },
                    "expense_id": {
                        "type": "string",
                        "description": "Add billable expense id which needs to be convert to invoice"
                    },
                    "salesorder_item_id": {
                        "type": "string",
                        "description": "ID of the sales order line item which is invoices."
                    },
                    "avatax_tax_code": {
                        "type": "string",
                        "description": "A tax code is a unique label used to group Items (products, services, or charges) together. Refer the [link][2] for more deails. Max-length [25]"
                    },
                    "line_item_id": {
                        "type": "string",
                        "description": "The line item id"
                    },
                    "ignore_auto_number_generation": {
                        "type": "string",
                        "description": "Ignore auto invoice number generation for this invoice. This mandates the invoice number. Allowed values "
                    }
                },
                "required": [
                    "customer_id",
                    "line_items"
                ]
            },
            "required": [
                "customer_id",
                "line_items"
            ]
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_an_invoice",
            "description": "Get the details of an invoice.",
            "parameters": {
                "type": "object",
                "properties": {
                    "print": {
                        "type": "string",
                        "description": "Print the exported pdf."
                    },
                    "accept": {
                        "type": "string",
                        "description": "Get the details of a particular invoice in formats such as json/ pdf/ html. Default format is json. Allowed values "
                    }
                },
                "required": []
            },
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "delete_an_invoice",
            "description": "Delete an existing invoice. Invoices which have payment or credits note applied cannot be deleted.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            },
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "mark_an_invoice_as_sent",
            "description": "Mark a draft invoice as sent.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            },
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "void_an_invoice",
            "description": "Mark an invoice status as void. Upon voiding, the payments and credits associated with the invoices will be unassociated and will be under customer credits.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            },
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "mark_as_draft",
            "description": "Mark a voided invoice as draft.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            },
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "email_invoices",
            "description": "Send invoices to your customers by email. Maximum of 10 invoices can be sent at once.",
            "parameters": {
                "type": "object",
                "properties": {
                    "contacts": {
                        "type": "array",
                        "description": "Contacts for whom email or snail mail has to be sent.",
                        "items": {
                            "type": "string"
                        }
                    },
                    "contact_id": {
                        "type": "string",
                        "description": "ID of the contact. Can specify if email or snail mail has to be sent for each contact."
                    },
                    "invoice_ids": {
                        "type": "string",
                        "description": "Comma separated invoice ids which are to be emailed."
                    }
                },
                "required": [
                    "contact_id",
                    "invoice_ids"
                ]
            },
            "required": [
                "contact_id",
                "invoice_ids"
            ]
        }
    },
    {
        "type": "function",
        "function": {
            "name": "create_an_instant_invoice",
            "description": "Create an instant invoice for all the confirmed sales orders you have selected.",
            "parameters": {
                "type": "object",
                "properties": {
                    "salesorder_id": {
                        "type": "string",
                        "description": "ID of the salesorder"
                    }
                },
                "required": []
            },
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "submit_an_invoice_for_approval",
            "description": "Submit an invoice for approval.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            },
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "approve_an_invoice_",
            "description": "Approve an invoice.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            },
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "email_an_invoice",
            "description": "Email an invoice to the customer. Input json string is not mandatory. If input json string is empty, mail will be send with default mail content.",
            "parameters": {
                "type": "object",
                "properties": {
                    "send_from_org_email_id": {
                        "type": "boolean",
                        "description": "Boolean to trigger the email from the organization's email address"
                    },
                    "to_mail_ids": {
                        "type": "array",
                        "description": "Array of email address of the recipients.",
                        "items": {
                            "type": "string"
                        }
                    },
                    "cc_mail_ids": {
                        "type": "array",
                        "description": "Array of email address of the recipients to be cced.",
                        "items": {
                            "type": "string"
                        }
                    },
                    "subject": {
                        "type": "string",
                        "description": "The subject of the mail"
                    },
                    "body": {
                        "type": "string",
                        "description": "The body of the mail"
                    },
                    "send_customer_statement": {
                        "type": "string",
                        "description": "Send customer statement pdf a with email."
                    },
                    "send_attachment": {
                        "type": "string",
                        "description": "Send the invoice attachment a with the email."
                    },
                    "attachments": {
                        "type": "string",
                        "description": "Files to be attached to the email"
                    }
                },
                "required": [
                    "to_mail_ids"
                ]
            },
            "required": [
                "to_mail_ids"
            ]
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_invoice_email_content",
            "description": "Get the email content of an invoice.",
            "parameters": {
                "type": "object",
                "properties": {
                    "email_template_id": {
                        "type": "string",
                        "description": "Get the email content based on a specific email template. If this param is not inputted, then the content will be based on the email template associated with the customer. If no template is associated with the customer, then default template will be used."
                    }
                },
                "required": []
            },
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "remind_customer",
            "description": "Remind your customer about an unpaid invoice by email. Reminder will be sent, only for the invoices which are in open or overdue status.",
            "parameters": {
                "type": "object",
                "properties": {
                    "to_mail_ids": {
                        "type": "array",
                        "description": "Array of email address of the recipients.",
                        "items": {
                            "type": "string"
                        }
                    },
                    "cc_mail_ids": {
                        "type": "array",
                        "description": "Array of email address of the recipients to be cced.",
                        "items": {
                            "type": "string"
                        }
                    },
                    "subject": {
                        "type": "string",
                        "description": "The subject of the mail"
                    },
                    "body": {
                        "type": "string",
                        "description": "The body of the mail"
                    },
                    "send_from_org_email_id": {
                        "type": "boolean",
                        "description": "Boolean to trigger the email from the organization's email address"
                    },
                    "send_customer_statement": {
                        "type": "string",
                        "description": "Send customer statement pdf a with email."
                    },
                    "attachments": {
                        "type": "string",
                        "description": "Files to be attached to the email"
                    }
                },
                "required": [
                    "cc_mail_ids"
                ]
            },
            "required": [
                "cc_mail_ids"
            ]
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_payment_reminder_mail_content",
            "description": "Get the mail content of the payment reminder.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            },
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "bulk_invoice_reminder",
            "description": "Remind your customer about an unpaid invoices by email. Reminder mail will be send, only for the invoices is in open or overdue status. Maximum 10 invoices can be reminded at once.",
            "parameters": {
                "type": "object",
                "properties": {
                    "invoice_ids": {
                        "type": "string",
                        "description": "Array of invoice ids for which the reminder has to be sent."
                    }
                },
                "required": [
                    "invoice_ids"
                ]
            },
            "required": [
                "invoice_ids"
            ]
        }
    },
    {
        "type": "function",
        "function": {
            "name": "bulk_export_invoices",
            "description": "Maximum of 25 invoices can be exported in a single pdf.",
            "parameters": {
                "type": "object",
                "properties": {
                    "invoice_ids": {
                        "type": "string",
                        "description": "Comma separated invoice ids which are to be export as pdf."
                    }
                },
                "required": [
                    "invoice_ids"
                ]
            },
            "required": [
                "invoice_ids"
            ]
        }
    },
    {
        "type": "function",
        "function": {
            "name": "bulk_print_invoices",
            "description": "Export invoices as pdf and print them. Maximum of 25 invoices can be printed.",
            "parameters": {
                "type": "object",
                "properties": {
                    "invoice_ids": {
                        "type": "string",
                        "description": "Export invoices as pdf and print them. Maximum of 25 invoices can be printed."
                    }
                },
                "required": [
                    "invoice_ids"
                ]
            },
            "required": [
                "invoice_ids"
            ]
        }
    },
    {
        "type": "function",
        "function": {
            "name": "disable_payment_reminder",
            "description": "Disable automated payment reminders for an invoice.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            },
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "enable_payment_reminder",
            "description": "Enable automated payment reminders for an invoice.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            },
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "write_off_invoice",
            "description": "Write off the invoice balance amount of an invoice.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            },
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "cancel_write_off",
            "description": "Cancel the write off amount of an invoice.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            },
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "update_billing_address",
            "description": "Updates the billing address for this invoice alone.",
            "parameters": {
                "type": "object",
                "properties": {
                    "address": {
                        "type": "string",
                        "description": "Billing address for the invoice"
                    },
                    "city": {
                        "type": "string",
                        "description": "City of the customer\u2019s billing address."
                    },
                    "state": {
                        "type": "string",
                        "description": "State of the customer\u2019s billing address."
                    },
                    "zip": {
                        "type": "string",
                        "description": "Zip code of the customer\u2019s billing address."
                    },
                    "country": {
                        "type": "string",
                        "description": "Country of the customer\u2019s billing address."
                    },
                    "fax": {
                        "type": "string",
                        "description": "Customer's fax number."
                    }
                },
                "required": []
            },
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "update_shipping_address",
            "description": "Updates the shipping address for this invoice alone.",
            "parameters": {
                "type": "object",
                "properties": {
                    "address": {
                        "type": "string",
                        "description": "Shipping address for the invoice"
                    },
                    "street2": {
                        "type": "string",
                        "description": "no description provided"
                    },
                    "city": {
                        "type": "string",
                        "description": "City of the customer\u2019s Shipping address."
                    },
                    "state": {
                        "type": "string",
                        "description": "State of the customer\u2019s Shipping address."
                    },
                    "zip": {
                        "type": "string",
                        "description": "Zip code of the customer\u2019s Shipping address."
                    },
                    "country": {
                        "type": "string",
                        "description": "Country of the customer\u2019s Shipping address."
                    },
                    "fax": {
                        "type": "string",
                        "description": "Customer's fax number."
                    }
                },
                "required": []
            },
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "list_invoice_templates",
            "description": "Get all invoice pdf templates.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            },
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "update_invoice_template",
            "description": "Update the pdf template associated with the invoice.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            },
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "list_invoice_payments",
            "description": "Get the list of payments made for an invoice.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            },
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "list_credits_applied",
            "description": "Get the list of credits applied for an invoice.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            },
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "apply_credits",
            "description": "Apply the customer credits either from credit notes or excess customer payments to an invoice. Multiple credits can be applied at once.",
            "parameters": {
                "type": "object",
                "properties": {
                    "invoice_payments": {
                        "type": "array",
                        "description": "ID of the payment",
                        "items": {
                            "type": "object",
                            "properties": {
                                "payment_id": {
                                    "type": "string",
                                    "description": "ID of the payment"
                                },
                                "amount_applied": {
                                    "type": "number",
                                    "description": "The applied amount to the creditnote"
                                }
                            }
                        }
                    },
                    "apply_creditnotes": {
                        "type": "array",
                        "description": "ID of the creditnote",
                        "items": {
                            "type": "object",
                            "properties": {
                                "creditnote_id": {
                                    "type": "string",
                                    "description": "ID of the creditnote"
                                },
                                "amount_applied": {
                                    "type": "number",
                                    "description": "The applied amount to the creditnote"
                                }
                            }
                        }
                    }
                },
                "required": [
                    "invoice_payments",
                    "apply_creditnotes"
                ]
            },
            "required": [
                "invoice_payments",
                "apply_creditnotes"
            ]
        }
    },
    {
        "type": "function",
        "function": {
            "name": "delete_a_payment",
            "description": "Delete a payment made to an invoice.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            },
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "delete__applied_credit",
            "description": "Delete a particular credit applied to an invoice.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            },
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "add_attachment_to_an_invoice",
            "description": "Attach a file to an invoice.",
            "parameters": {
                "type": "object",
                "properties": {
                    "can_send_in_mail": {
                        "type": "string",
                        "description": "True to send the attachment with the invoice when emailed."
                    },
                    "attachment": {
                        "type": "string",
                        "description": "The file to be attached.Allowed Extensions: "
                    }
                },
                "required": []
            },
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "update_attachment_preference",
            "description": "Set whether you want to send the attached file while emailing the invoice.",
            "parameters": {
                "type": "object",
                "properties": {
                    "can_send_in_mail": {
                        "type": "string",
                        "description": "Boolean to send the attachment with the invoice when emailed."
                    }
                },
                "required": [
                    "can_send_in_mail"
                ]
            },
            "required": [
                "can_send_in_mail"
            ]
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_an_invoice_attachment",
            "description": "Returns the file attached to the invoice.",
            "parameters": {
                "type": "object",
                "properties": {
                    "preview": {
                        "type": "string",
                        "description": "Get the thumbnail of the attachment."
                    }
                },
                "required": []
            },
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "delete_an_attachment",
            "description": "Delete the file attached to the invoice.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            },
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "delete_the_expense_receipt",
            "description": "Delete the expense receipts attached to an invoice which is raised from an expense.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            },
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "update_custom_field_in_existing_invoices",
            "description": "Update the value of the custom field in existing invoices.",
            "parameters": {
                "type": "object",
                "properties": {
                    "customfield_id": {
                        "type": "integer",
                        "description": "no description provided"
                    },
                    "value": {
                        "type": "string",
                        "description": "Value of the Custom Field"
                    },
                    "organization_id": {
                        "type": "string",
                        "description": "ID of the organization"
                    }
                },
                "required": [
                    "organization_id"
                ]
            },
            "required": [
                "organization_id"
            ]
        }
    },
    {
        "type": "function",
        "function": {
            "name": "add_comment",
            "description": "Add a comment for an invoice.",
            "parameters": {
                "type": "object",
                "properties": {
                    "description": {
                        "type": "string",
                        "description": "no description provided"
                    },
                    "payment_expected_date": {
                        "type": "string",
                        "description": "no description provided"
                    },
                    "show_comment_to_clients": {
                        "type": "string",
                        "description": "Boolean to check if the comment to be shown to the clients"
                    }
                },
                "required": []
            },
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "list_invoice_comments_and_history",
            "description": "Get the complete history and comments of an invoice.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            },
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "update_comment",
            "description": "Update an existing comment of an invoice.",
            "parameters": {
                "type": "object",
                "properties": {
                    "description": {
                        "type": "string",
                        "description": "The comment on a invoice"
                    },
                    "show_comment_to_clients": {
                        "type": "string",
                        "description": "Boolean to check if the comment to be shown to the clients"
                    }
                },
                "required": []
            },
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "delete_a_comment",
            "description": "Delete an invoice comment.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            },
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "generate_payment_link",
            "description": "This API generates a payment link for the invoice with an expiry date.",
            "parameters": {
                "type": "object",
                "properties": {
                    "transaction_id": {
                        "type": "string",
                        "description": "The ID of the transaction (Invoice ID)."
                    },
                    "transaction_type": {
                        "type": "string",
                        "description": "The type of the transaction (Invoice)."
                    },
                    "link_type": {
                        "type": "string",
                        "description": "The type of the link (Private or Public)."
                    },
                    "expiry_time": {
                        "type": "string",
                        "description": "The expiry time of the payment link. Supported format : "
                    }
                },
                "required": [
                    "transaction_id",
                    "transaction_type",
                    "link_type",
                    "expiry_time"
                ]
            },
            "required": [
                "transaction_id",
                "transaction_type",
                "link_type",
                "expiry_time"
            ]
        }
    }
]
