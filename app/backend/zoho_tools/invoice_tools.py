search_invoices = {
    "type": "function",
    "function":
        {
            "name": "list_invoices",
            "description": "List all invoices with pagination.",
            "parameters": {
                "type": "object",
                "properties": {
                    "invoice_number": {
                        "type": "string",
                        "description": "Search invoices by invoice number."
                    },
                    "invoice_number_startswith": {
                        "type": "string",
                        "description": "Search invoices where the invoice number starts with the specified value."
                    },
                    "invoice_number_contains": {
                        "type": "string",
                        "description": "Search invoices where the invoice number contains the specified value."
                    },
                    "item_name": {
                        "type": "string",
                        "description": "Search invoices by item name."
                    },
                    "item_name_startswith": {
                        "type": "string",
                        "description": "Search invoices where the item name starts with the specified value."
                    },
                    "item_name_contains": {
                        "type": "string",
                        "description": "Search invoices where the item name contains the specified value."
                    },
                    "item_id": {
                        "type": "string",
                        "description": "Search invoices by item id."
                    },
                    "item_description": {
                        "type": "string",
                        "description": "Search invoices by item description."
                    },
                    "item_description_startswith": {
                        "type": "string",
                        "description": "Search invoices where the item description starts with the specified value."
                    },
                    "item_description_contains": {
                        "type": "string",
                        "description": "Search invoices where the item description contains the specified value."
                    },
                    "reference_number": {
                        "type": "string",
                        "description": "The reference number of the invoice."
                    },
                    "customer_name": {
                        "type": "string",
                        "description": "The name of the customer. Max-length [100]."
                    },
                    "recurring_invoice_id": {
                        "type": "string",
                        "description": "ID of the recurring invoice from which the invoice is created."
                    },
                    "email": {
                        "type": "string",
                        "description": "Search contacts by email id. Max-length [100]."
                    },
                    "total": {
                        "type": "number",
                        "description": "The total amount to be paid."
                    },
                    "balance": {
                        "type": "number",
                        "description": "The unpaid amount."
                    },
                    "custom_field": {
                        "type": "string",
                        "description": "Search invoices by custom fields."
                    },
                    "custom_field_startswith": {
                        "type": "string",
                        "description": "Search invoices where the custom field starts with the specified value."
                    },
                    "custom_field_contains": {
                        "type": "string",
                        "description": "Search invoices where the custom field contains the specified value."
                    },
                    "date": {
                        "type": "string",
                        "description": "Search invoices by invoice date. Default date format is yyyy-mm-dd."
                    },
                    "due_date": {
                        "type": "string",
                        "description": "Search invoices by due date. Default date format is yyyy-mm-dd."
                    },
                    "due_date_start": {
                        "type": "string",
                        "description": "Search invoices where the due date starts from the specified date. Default "
                                       "date format is yyyy-mm-dd."
                    },
                    "due_date_end": {
                        "type": "string",
                        "description": "Search invoices where the due date ends at the specified date. Default date "
                                       "format is yyyy-mm-dd."
                    },
                    "due_date_before": {
                        "type": "string",
                        "description": "Search invoices where the due date is before the specified date. Default date "
                                       "format is yyyy-mm-dd."
                    },
                    "due_date_after": {
                        "type": "string",
                        "description": "Search invoices where the due date is after the specified date. Default date "
                                       "format is yyyy-mm-dd."
                    },
                    "last_modified_time": {
                        "type": "string",
                        "description": "Filter invoices by their last modified time. Default date format is yyyy-mm-dd."
                    },
                    "status": {
                        "type": "string",
                        "description": "Search invoices by invoice status. Allowed Values: sent, draft, overdue, "
                                       "paid, void, unpaid, partially_paid and viewed.",
                        "enum": ["sent", "draft", "overdue", "paid", "void", "unpaid", "partially_paid", "viewed"]
                    },
                    "customer_id": {
                        "type": "string",
                        "description": "ID of the customer the invoice has to be created."
                    },
                    "filter_by": {
                        "type": "string",
                        "description": "Filter invoices by any status or payment expected date. Allowed Values: "
                                       "Status.All, Status.Sent, Status.Draft, Status.OverDue, Status.Paid, "
                                       "Status.Void, Status.Unpaid, Status.PartiallyPaid, Status.Viewed and "
                                       "Date.PaymentExpectedDate.",
                        "enum": ["Status.All", "Status.Sent", "Status.Draft", "Status.OverDue", "Status.Paid",
                                 "Status.Void", "Status.Unpaid", "Status.PartiallyPaid", "Status.Viewed",
                                 "Date.PaymentExpectedDate"]
                    },
                    "search_text": {
                        "type": "string",
                        "description": "Search invoices by invoice number or purchase order or customer name. "
                                       "Max-length [100]."
                    },
                    "sort_column": {
                        "type": "string",
                        "description": "Sort invoices by the specified column. Allowed Values: customer_name, "
                                       "invoice_number, date, due_date, total, balance and created_time.",
                        "enum": ["customer_name", "invoice_number", "date", "due_date", "total", "balance",
                                 "created_time"]
                    },
                    "zcrm_potential_id": {
                        "type": "string",
                        "description": "Potential ID of a Deal in CRM."
                    }
                }
            }
        },
}

create_an_invoice = {
    "type": "function",
    "function":
        {
            "name": "create_invoice",
            "description": "Create an invoice for your customer.",
            "parameters": {
                "type": "object",
                "properties": {
                    "customer_id": {
                        "type": "string",
                        "description": "ID of the customer the invoice has to be created.",
                    },
                    "currency_id": {
                        "type": "string",
                        "description": "The currency id of the currency."
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
                        "description": "Search invoices by invoice number. Max-length [100]."
                    },
                    "place_of_supply": {
                        "type": "string",
                        "description": "Place where the goods/services are supplied to. (If not given, place of "
                                       "contact given for the contact will be taken)."
                    },
                    "vat_treatment": {
                        "type": "string",
                        "description": "VAT treatment for the invoices for UK customers."
                    },
                    "tax_treatment": {
                        "type": "string",
                        "description": "VAT treatment for the invoice for GCC and MX customers."
                    },
                    "gst_treatment": {
                        "type": "string",
                        "description": "Choose whether the contact is GST registered/unregistered/consumer/overseas "
                                       "for India. Allowed values are business_gst, business_none, overseas, consumer."
                    },
                    "gst_no": {
                        "type": "string",
                        "description": "15 digit GST identification number of the customer for India."
                    },
                    "cfdi_usage": {
                        "type": "string",
                        "description": "Choose CFDI Usage for MX customers."
                    },
                    "reference_number": {
                        "type": "string",
                        "description": "The reference number of the invoice."
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
                        "description": "Payment terms in days e.g. 15, 30, 60. Invoice due date will be calculated "
                                       "based on this."
                    },
                    "payment_terms_label": {
                        "type": "string",
                        "description": "Used to override the default payment terms label. Max-length [100]."
                    },
                    "due_date": {
                        "type": "string",
                        "description": "Search invoices by due date. Default date format is yyyy-mm-dd."
                    },
                    "discount": {
                        "type": "number",
                        "description": "Discount applied to the invoice. It can be either in % or in amount."
                    },
                    "is_discount_before_tax": {
                        "type": "boolean",
                        "description": "Used to specify how the discount has to applied. Either before or after the "
                                       "calculation of tax."
                    },
                    "discount_type": {
                        "type": "string",
                        "description": "How the discount is specified. Allowed values: entity_level and item_level."
                    },
                    "is_inclusive_tax": {
                        "type": "boolean",
                        "description": "Used to specify whether the line item rates are inclusive or exclusive of tax."
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
                        "description": "ID of the estimate from which the invoice is created."
                    },
                    "salesperson_name": {
                        "type": "string",
                        "description": "Name of the salesperson. Max-length [200]."
                    },
                    "custom_fields": {
                        "type": "array",
                        "description": "Custom fields for an invoice.",
                        "items": {
                            "type": "object"
                        }
                    },
                    "line_items": {
                        "type": "array",
                        "description": "Line items for the invoice.",
                        "items": {
                            "type": "object",
                        }
                    },
                    "payment_options": {
                        "type": "object",
                        "description": "Payment options for the invoice, online payment gateways and bank accounts."
                    },
                    "allow_partial_payments": {
                        "type": "boolean",
                        "description": "Boolean to check if partial payments are allowed for the contact."
                    },
                    "custom_body": {
                        "type": "string",
                        "description": "Custom body text for the invoice."
                    },
                    "custom_subject": {
                        "type": "string",
                        "description": "Custom subject text for the invoice."
                    },
                    "notes": {
                        "type": "string",
                        "description": "Notes added below expressing gratitude or for conveying some information."
                    },
                    "terms": {
                        "type": "string",
                        "description": "Terms added below expressing gratitude or for conveying some information."
                    },
                    "shipping_charge": {
                        "type": "string",
                        "description": "Shipping charges applied to the invoice. Max-length [100]."
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
                        "description": "Reason for the adjustment."
                    },
                    "tax_authority_id": {
                        "type": "string",
                        "description": "ID of the tax authority for US customers."
                    },
                    "tax_exemption_id": {
                        "type": "string",
                        "description": "ID of the tax exemption for India and US customers."
                    },
                    "avatax_use_code": {
                        "type": "string",
                        "description": "Avalara Use Code for exemption purposes."
                    },
                    "avatax_exempt_no": {
                        "type": "string",
                        "description": "Exemption certificate number of the customer for Avalara Integration."
                    },
                    "tax_id": {
                        "type": "string",
                        "description": "ID of the tax."
                    },
                    "expense_id": {
                        "type": "string",
                        "description": "Expense ID associated with the invoice."
                    },
                    "salesorder_item_id": {
                        "type": "string",
                        "description": "ID of the sales order line item invoiced."
                    },
                    "avatax_tax_code": {
                        "type": "string",
                        "description": "Avalara tax code for the item. Max-length [25]."
                    },
                    "time_entry_ids": {
                        "type": "array",
                        "description": "IDs of the time entries associated with the project.",
                        "items": {
                            "type": "string"
                        }
                    }
                },
                "required": ["customer_id", "line_items"],
                # "queryParameters": {
                #     "type": "object",
                #     "properties": {
                #         "send": {
                #             "type": "boolean",
                #             "description": "Send the invoice to the contact person(s) associated with the invoice. "
                #                            "Allowed values: true, false."
                #         },
                #         "ignore_auto_number_generation": {
                #             "type": "boolean",
                #             "description": "Ignore auto invoice number generation for this invoice. This mandates the "
                #                            "invoice number. Allowed values: true, false."
                #         }
                #     }
                # }
            }
        },
}
