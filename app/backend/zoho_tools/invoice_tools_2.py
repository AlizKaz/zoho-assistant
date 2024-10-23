tools = [
    {
        "type": "function",
        "function": {
            "name": "create_an_invoice",
            "description": "Create an invoice for your customer.",
            "parameters": {
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
                    "description": "Array of contact person(s) for whom invoice has to be sent."
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
                    "type": "float",
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
                    "type": "float",
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
                    "description": "Custom fields for an invoice."
                },
                "customfield_id": {
                    "type": "long",
                    "description": null
                },
                "value": {
                    "type": "string",
                    "description": "Value of the Custom Field"
                },
                "line_items": {
                    "type": "array",
                    "description": "Search invoices by item id."
                },
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
                    "description": "IDs of the time entries associated with the project."
                },
                "product_type": {
                    "type": "string",
                    "description": "Enter goods/services"
                },
                "hsn_or_sac": {
                    "type": "string",
                    "description": "Add HSN/SAC code for your goods/services"
                },
                "sat_item_key_code": {
                    "type": "string",
                    "description": "Add SAT Item Key Code for your goods/services. Download the "
                },
                "unitkey_code": {
                    "type": "string",
                    "description": "Add SAT Unit Key Code for your goods/services. Download the "
                },
                "warehouse_id": {
                    "type": "string",
                    "description": "Enter warehouse ID"
                },
                "expense_id": {
                    "type": "string",
                    "description": null
                },
                "expense_receipt_name": {
                    "type": "string",
                    "description": null
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
                    "type": "float",
                    "description": "base currency rate"
                },
                "rate": {
                    "type": "double",
                    "description": "Rate of the line item."
                },
                "quantity": {
                    "type": "float",
                    "description": "The quantity of line item"
                },
                "unit": {
                    "type": "string",
                    "description": "Unit of the line item e.g. kgs, Nos. Max-length [100]"
                },
                "discount_amount": {
                    "type": "float",
                    "description": "The discount amount on the line item"
                },
                "tags": {
                    "type": "array",
                    "description": "Filter all your reports based on the tag"
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
                    "type": "float",
                    "description": "The  percentage of tax levied"
                },
                "tax_treatment_code": {
                    "type": "string",
                    "description": "Specify reason for using out of scope.Supported values for UAE are "
                },
                "header_name": {
                    "type": "string",
                    "description": "Name of the item header"
                },
                "payment_options": {
                    "type": "object",
                    "description": "Payment options for the invoice, online payment gateways and bank accounts. Will be displayed in the pdf."
                },
                "payment_gateways": {
                    "type": "array",
                    "description": "Online payment gateways through which payment can be made."
                },
                "configured": {
                    "type": "boolean",
                    "description": "Boolean check to see if a payment gateway has been configured"
                },
                "additional_field1": {
                    "type": "string",
                    "description": "Paypal payment method. Allowed Values: "
                },
                "gateway_name": {
                    "type": "string",
                    "description": "Name of the payment gateway associated with the invoice. E.g. paypal, stripe.Allowed Values: "
                },
                "allow_partial_payments": {
                    "type": "boolean",
                    "description": "Boolean to check if partial payments are allowed for the contact"
                },
                "custom_body": {
                    "type": "string",
                    "description": null
                },
                "custom_subject": {
                    "type": "string",
                    "description": null
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
                    "type": "double",
                    "description": "Adjustments made to the invoice."
                },
                "adjustment_description": {
                    "type": "string",
                    "description": "Customize the adjustment description. E.g. Rounding off."
                },
                "reason": {
                    "type": "string",
                    "description": null
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
                "salesorder_item_id": {
                    "type": "string",
                    "description": "ID of the sales order line item which is invoices."
                },
                "avatax_tax_code": {
                    "type": "string",
                    "description": "A tax code is a unique label used to group Items (products, services, or charges) together. Refer the [link][2] for more deails. Max-length [25]"
                },
                "send": {
                    "type": "",
                    "description": "Send the invoice to the contact person(s) associated with the invoice. Allowed values "
                },
                "ignore_auto_number_generation": {
                    "type": "",
                    "description": "Ignore auto invoice number generation for this invoice. This mandates the invoice number. Allowed values "
                }
            },
            "required": [
                "customer_id",
                "line_items",
                "item_id"
            ]
        }
    },
    {
        "type": "function",
        "function": {
            "name": "list_invoices",
            "description": "List all invoices with pagination.",
            "parameters": {},
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "update_an_invoice",
            "description": "Update an existing invoice. To delete a line item just remove it from the line_items list.",
            "parameters": {
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
                    "description": "Array of contact person(s) for whom invoice has to be sent."
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
                    "type": "float",
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
                    "type": "float",
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
                    "description": "Custom fields for an invoice."
                },
                "customfield_id": {
                    "type": "long",
                    "description": null
                },
                "value": {
                    "type": "string",
                    "description": "Value of the Custom Field"
                },
                "line_items": {
                    "type": "array",
                    "description": "Search invoices by item id."
                },
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
                    "description": "IDs of the time entries associated with the project."
                },
                "product_type": {
                    "type": "string",
                    "description": "Enter goods/services"
                },
                "hsn_or_sac": {
                    "type": "string",
                    "description": "Add HSN/SAC code for your goods/services"
                },
                "sat_item_key_code": {
                    "type": "string",
                    "description": "Add SAT Item Key Code for your goods/services. Download the "
                },
                "unitkey_code": {
                    "type": "string",
                    "description": "Add SAT Unit Key Code for your goods/services. Download the "
                },
                "warehouse_id": {
                    "type": "string",
                    "description": "Enter warehouse ID"
                },
                "expense_id": {
                    "type": "string",
                    "description": null
                },
                "expense_receipt_name": {
                    "type": "string",
                    "description": null
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
                    "type": "float",
                    "description": "base currency rate"
                },
                "rate": {
                    "type": "double",
                    "description": "Rate of the line item."
                },
                "quantity": {
                    "type": "float",
                    "description": "The quantity of line item"
                },
                "unit": {
                    "type": "string",
                    "description": "Unit of the line item e.g. kgs, Nos. Max-length [100]"
                },
                "discount_amount": {
                    "type": "float",
                    "description": "The discount amount on the line item"
                },
                "tags": {
                    "type": "array",
                    "description": "Filter all your reports based on the tag"
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
                    "type": "float",
                    "description": "The  percentage of tax levied"
                },
                "tax_treatment_code": {
                    "type": "string",
                    "description": "Specify reason for using out of scope.Supported values for UAE are "
                },
                "header_name": {
                    "type": "string",
                    "description": "Name of the item header"
                },
                "header_id": {
                    "type": "string",
                    "description": "ID of the item header"
                },
                "payment_options": {
                    "type": "object",
                    "description": "Payment options for the invoice, online payment gateways and bank accounts. Will be displayed in the pdf."
                },
                "payment_gateways": {
                    "type": "array",
                    "description": "Online payment gateways through which payment can be made."
                },
                "configured": {
                    "type": "boolean",
                    "description": "Boolean check to see if a payment gateway has been configured"
                },
                "additional_field1": {
                    "type": "string",
                    "description": "Paypal payment method. Allowed Values: "
                },
                "gateway_name": {
                    "type": "string",
                    "description": "Name of the payment gateway associated with the invoice. E.g. paypal, stripe.Allowed Values: "
                },
                "allow_partial_payments": {
                    "type": "boolean",
                    "description": "Boolean to check if partial payments are allowed for the contact"
                },
                "custom_body": {
                    "type": "string",
                    "description": null
                },
                "custom_subject": {
                    "type": "string",
                    "description": null
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
                    "type": "double",
                    "description": "Adjustments made to the invoice."
                },
                "adjustment_description": {
                    "type": "string",
                    "description": "Customize the adjustment description. E.g. Rounding off."
                },
                "reason": {
                    "type": "string",
                    "description": null
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
                    "type": "",
                    "description": "Ignore auto invoice number generation for this invoice. This mandates the invoice number. Allowed values "
                }
            },
            "required": [
                "customer_id",
                "line_items",
                "item_id"
            ]
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_an_invoice",
            "description": "Get the details of an invoice.",
            "parameters": {},
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "delete_an_invoice",
            "description": "Delete an existing invoice. Invoices which have payment or credits note applied cannot be deleted.",
            "parameters": {},
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "mark_an_invoice_as_sent",
            "description": "Mark a draft invoice as sent.",
            "parameters": {},
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "void_an_invoice",
            "description": "Mark an invoice status as void. Upon voiding, the payments and credits associated with the invoices will be unassociated and will be under customer credits.",
            "parameters": {},
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "mark_as_draft",
            "description": "Mark a voided invoice as draft.",
            "parameters": {},
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "email_invoices",
            "description": "Send invoices to your customers by email. Maximum of 10 invoices can be sent at once.",
            "parameters": {
                "contacts": {
                    "type": "array",
                    "description": "Contacts for whom email or snail mail has to be sent."
                },
                "contact_id": {
                    "type": "string",
                    "description": "ID of the contact. Can specify if email or snail mail has to be sent for each contact."
                },
                "invoice_ids": {
                    "type": "",
                    "description": "Comma separated invoice ids which are to be emailed."
                }
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
            "name": "submit_an_invoice_for_approval",
            "description": "Submit an invoice for approval.",
            "parameters": {},
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "approve_an_invoice.",
            "description": "Approve an invoice.",
            "parameters": {},
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "email_an_invoice",
            "description": "Email an invoice to the customer. Input json string is not mandatory. If input json string is empty, mail will be send with default mail content.",
            "parameters": {
                "send_from_org_email_id": {
                    "type": "boolean",
                    "description": "Boolean to trigger the email from the organization's email address"
                },
                "to_mail_ids": {
                    "type": "array",
                    "description": "Array of email address of the recipients."
                },
                "cc_mail_ids": {
                    "type": "array",
                    "description": "Array of email address of the recipients to be cced."
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
                    "type": "",
                    "description": "Send customer statement pdf a with email."
                },
                "send_attachment": {
                    "type": "",
                    "description": "Send the invoice attachment a with the email."
                },
                "attachments": {
                    "type": "",
                    "description": "Files to be attached to the email"
                }
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
            "parameters": {},
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "remind_customer",
            "description": "Remind your customer about an unpaid invoice by email. Reminder will be sent, only for the invoices which are in open or overdue status.",
            "parameters": {
                "to_mail_ids": {
                    "type": "array",
                    "description": "Array of email address of the recipients."
                },
                "cc_mail_ids": {
                    "type": "array",
                    "description": "Array of email address of the recipients to be cced."
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
                    "type": "",
                    "description": "Send customer statement pdf a with email."
                },
                "attachments": {
                    "type": "",
                    "description": "Files to be attached to the email"
                }
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
            "parameters": {},
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "bulk_invoice_reminder",
            "description": "Remind your customer about an unpaid invoices by email. Reminder mail will be send, only for the invoices is in open or overdue status. Maximum 10 invoices can be reminded at once.",
            "parameters": {},
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "bulk_export_invoices",
            "description": "Maximum of 25 invoices can be exported in a single pdf.",
            "parameters": {},
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "bulk_print_invoices",
            "description": "Export invoices as pdf and print them. Maximum of 25 invoices can be printed.",
            "parameters": {},
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "disable_payment_reminder",
            "description": "Disable automated payment reminders for an invoice.",
            "parameters": {},
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "enable_payment_reminder",
            "description": "Enable automated payment reminders for an invoice.",
            "parameters": {},
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "write_off_invoice",
            "description": "Write off the invoice balance amount of an invoice.",
            "parameters": {},
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "cancel_write_off",
            "description": "Cancel the write off amount of an invoice.",
            "parameters": {},
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "update_billing_address",
            "description": "Updates the billing address for this invoice alone.",
            "parameters": {
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
        }
    },
    {
        "type": "function",
        "function": {
            "name": "update_shipping_address",
            "description": "Updates the shipping address for this invoice alone.",
            "parameters": {
                "address": {
                    "type": "string",
                    "description": "Shipping address for the invoice"
                },
                "street2": {
                    "type": "string",
                    "description": null
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
        }
    },
    {
        "type": "function",
        "function": {
            "name": "list_invoice_templates",
            "description": "Get all invoice pdf templates.",
            "parameters": {},
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "update_invoice_template",
            "description": "Update the pdf template associated with the invoice.",
            "parameters": {},
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "list_invoice_payments",
            "description": "Get the list of payments made for an invoice.",
            "parameters": {},
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "list_credits_applied",
            "description": "Get the list of credits applied for an invoice.",
            "parameters": {},
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "apply_credits",
            "description": "Apply the customer credits either from credit notes or excess customer payments to an invoice. Multiple credits can be applied at once.",
            "parameters": {
                "invoice_payments": {
                    "type": "array",
                    "description": "ID of the payment"
                },
                "payment_id": {
                    "type": "string",
                    "description": "ID of the payment"
                },
                "amount_applied": {
                    "type": "float",
                    "description": "The applied amount to the creditnote"
                },
                "apply_creditnotes": {
                    "type": "array",
                    "description": "ID of the creditnote"
                },
                "creditnote_id": {
                    "type": "string",
                    "description": "ID of the creditnote"
                }
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
            "parameters": {},
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "delete__applied_credit",
            "description": "Delete a particular credit applied to an invoice.",
            "parameters": {},
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "add_attachment_to_an_invoice",
            "description": "Attach a file to an invoice.",
            "parameters": {},
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "update_attachment_preference",
            "description": "Set whether you want to send the attached file while emailing the invoice.",
            "parameters": {},
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_an_invoice_attachment",
            "description": "Returns the file attached to the invoice.",
            "parameters": {},
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "delete_an_attachment",
            "description": "Delete the file attached to the invoice.",
            "parameters": {},
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "delete_the_expense_receipt",
            "description": "Delete the expense receipts attached to an invoice which is raised from an expense.",
            "parameters": {},
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "update_custom_field_in_existing_invoices",
            "description": "Update the value of the custom field in existing invoices.",
            "parameters": {
                "customfield_id": {
                    "type": "long",
                    "description": null
                },
                "value": {
                    "type": "string",
                    "description": "Value of the Custom Field"
                },
                "organization_id": {
                    "type": "",
                    "description": "ID of the organization"
                }
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
            "parameters": {},
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "list_invoice_comments_&_history",
            "description": "Get the complete history and comments of an invoice.",
            "parameters": {},
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "update_comment",
            "description": "Update an existing comment of an invoice.",
            "parameters": {},
            "required": []
        }
    },
    {
        "type": "function",
        "function": {
            "name": "delete_a_comment",
            "description": "Delete an invoice comment.",
            "parameters": {},
            "required": []
        }
    }
]
