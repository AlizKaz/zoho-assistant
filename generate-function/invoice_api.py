class InvoiceApi:
	def __init__(self, zoho_books_api, access_token, session):
		self.access_token = access_token
		self.zoho_books_api = zoho_books_api
		self.session = session

	def zoho_get_api_call(self, api_url, params, headers, data_key_name_in_response):
		print(api_url)
		r = self.session.get(api_url, params=params, headers=headers)
		if r.json()['code'] == 0:
			return True, r.json()[data_key_name_in_response], None
		else:
			return False, None, r.json()

	def zoho_post_api_call(self, api_url, payload, headers, data_key_name_in_response):
		print(api_url)
		r = self.session.post(api_url, json=payload, headers=headers)
		if r.json()['code'] == 0:
			return True, r.json()[data_key_name_in_response], None
		else:
			return False, None, r.json()

	def create_an_invoice(self, **kwargs):
		"""Create an invoice for your customer.
		name:customer_id, type:string, required:Required. description:ID of the customer the invoice has to be created.
		name:currency_id, type:string, required:Optional. description:The currency id of the currency
		name:contact_persons, type:array, required:Optional. description:Array of contact person(s) for whom invoice has to be sent.
		name:invoice_number, type:string, required:Optional. description:Search invoices by invoice number.Variants: 
		name:invoice_number_startswith, type:string, required:Optional. description:Search invoices by invoice number.Variants: 
		name:invoice_number_contains, type:string, required:Optional. description:Search invoices by invoice number.Variants: 
		name:place_of_supply, type:string, required:Optional. description:Place where the goods/services are supplied to. (If not given, 
		name:vat_treatment, type:string, required:Optional. description:(Optional) VAT treatment for the invoices. VAT treatment denotes the location of the customer, if the customer resides in UK then the VAT treatment is 
		name:tax_treatment, type:string, required:Optional. description:VAT treatment for the invoice .Choose whether the contact falls under: 
		name:is_reverse_charge_applied, type:boolean, required:Optional. description:(Required if customer tax treatment is 
		name:gst_treatment, type:string, required:Optional. description:Choose whether the contact is GST registered/unregistered/consumer/overseas. Allowed values are 
		name:gst_no, type:string, required:Optional. description:15 digit GST identification number of the customer.
		name:cfdi_usage, type:string, required:Optional. description:Choose CFDI Usage. Allowed values:
		name:reference_number, type:string, required:Optional. description:The reference number of the invoice
		name:template_id, type:string, required:Optional. description:ID of the pdf template associated with the invoice.
		name:date, type:string, required:Optional. description:Search invoices by invoice date. Default date format is yyyy-mm-dd.
		name:payment_terms, type:integer, required:Optional. description:Payment terms in days e.g. 15, 30, 60. Invoice due date will be calculated based on this. Max-length [100]
		name:payment_terms_label, type:string, required:Optional. description:Used to override the default payment terms label. Default value for 15 days is "Net 15 Days". Max-length [100]
		name:due_date, type:string, required:Optional. description:Search invoices by due date. Default date format is yyyy-mm-dd. 
		name:discount, type:float, required:Optional. description:Discount applied to the invoice. It can be either in % or in amount. e.g. 12.5% or 190. Max-length [100]
		name:is_discount_before_tax, type:boolean, required:Optional. description:Used to specify how the discount has to applied. Either before or after the calculation of tax.
		name:discount_type, type:string, required:Optional. description:How the discount is specified. Allowed values: 
		name:is_inclusive_tax, type:boolean, required:Optional. description:Used to specify whether the line item rates are inclusive or exclusivr of tax.
		name:exchange_rate, type:float, required:Optional. description:Exchange rate of the currency.
		name:recurring_invoice_id, type:string, required:Optional. description:ID of the recurring invoice from which the invoice is created.
		name:invoiced_estimate_id, type:string, required:Optional. description:ID of the invoice from which the invoice is created.
		name:salesperson_name, type:string, required:Optional. description:Name of the salesperson. Max-length [200]
		name:custom_fields, type:array, required:Optional. description:Custom fields for an invoice.
			sub attributes:
			name:customfield_id, type:long, required:Optional. description:
			name:value, type:string, required:Optional. description:Value of the Custom Field
		name:line_items, type:array, required:Required. description:Search invoices by item id.
			sub attributes:
			name:item_id, type:string, required:Required. description:Search invoices by item id.
			name:project_id, type:string, required:Optional. description:ID of the Project.
			name:time_entry_ids, type:array, required:Optional. description:IDs of the time entries associated with the project.
			name:product_type, type:string, required:Optional. description:Enter
			name:hsn_or_sac, type:string, required:Optional. description:Add HSN/SAC code for your goods/services
			name:sat_item_key_code, type:string, required:Optional. description:Add SAT Item Key Code for your goods/services. Download the
			name:unitkey_code, type:string, required:Optional. description:Add SAT Unit Key Code for your goods/services. Download the
			name:warehouse_id, type:string, required:Optional. description:Enter warehouse ID
			name:expense_id, type:string, required:Optional. description:Add billable expense id which needs to be convert to invoice
			name:bill_id, type:string, required:Optional. description:Add billable bill id which needs to be convert to invoice
			name:bill_item_id, type:string, required:Optional. description:Add billable bill item id which needs to be convert to invoice
			name:expense_receipt_name, type:string, required:Optional. description:
			name:name, type:string, required:Optional. description:The name of the line item. Max-length [100]
			name:description, type:string, required:Optional. description:The description of the line items. Max-length [2000]
			name:item_order, type:integer, required:Optional. description:The order of the line item_order
			name:bcy_rate, type:float, required:Optional. description:base currency rate
			name:rate, type:double, required:Optional. description:Rate of the line item.
			name:quantity, type:float, required:Optional. description:The quantity of line item
			name:unit, type:string, required:Optional. description:Unit of the line item e.g. kgs, Nos. Max-length [100]
			name:discount_amount, type:float, required:Optional. description:The discount amount on the line item
			name:discount, type:float, required:Optional. description:Discount applied to the invoice. It can be either in % or in amount. e.g. 12.5% or 190. Max-length [100]
			name:tags, type:array, required:Optional. description:Filter all your reports based on the tag
			name:tag_id, type:string, required:Optional. description:ID of the reporting tag
			name:tag_option_id, type:string, required:Optional. description:ID of the reporting tag's option
			name:tax_id, type:string, required:Optional. description:ID of the tax.
			name:tds_tax_id, type:string, required:Optional. description:ID of the TDS tax.
			name:tax_name, type:string, required:Optional. description:The name of the tax
			name:tax_type, type:string, required:Optional. description:The type of the tax
			name:tax_percentage, type:float, required:Optional. description:The  percentage of tax levied
			name:tax_treatment_code, type:string, required:Optional. description:Specify reason for using out of scope.Supported values for UAE are
			name:header_name, type:string, required:Optional. description:Name of the item header
			name:salesorder_item_id, type:string, required:Optional. description:ID of the sales order line item which is invoices.
		name:payment_options, type:object, required:Optional. description:Payment options for the invoice, online payment gateways and bank accounts. Will be displayed in the pdf.
			sub attributes:
			name:payment_gateways, type:array, required:Optional. description:Online payment gateways through which payment can be made.
			name:configured, type:boolean, required:Optional. description:Boolean check to see if a payment gateway has been configured
			name:additional_field1, type:string, required:Optional. description:Paypal payment method. Allowed Values:
			name:gateway_name, type:string, required:Optional. description:Name of the payment gateway associated with the invoice. E.g. paypal, stripe.Allowed Values:
		name:allow_partial_payments, type:boolean, required:Optional. description:Boolean to check if partial payments are allowed for the contact
		name:custom_body, type:string, required:Optional. description:None
		name:custom_subject, type:string, required:Optional. description:None
		name:notes, type:string, required:Optional. description:The notes added below expressing gratitude or for conveying some information.
		name:terms, type:string, required:Optional. description:The terms added below expressing gratitude or for conveying some information.
		name:shipping_charge, type:string, required:Optional. description:Shipping charges applied to the invoice. Max-length [100]
		name:adjustment, type:double, required:Optional. description:Adjustments made to the invoice.
		name:adjustment_description, type:string, required:Optional. description:Customize the adjustment description. E.g. Rounding off.
		name:reason, type:string, required:Optional. description:None
		name:tax_authority_id, type:string, required:Optional. description:ID of the tax authority. Tax authority depends on the location of the customer. For example, if the customer is located in NY, then the tax authority is NY tax authority.
		name:tax_exemption_id, type:string, required:Optional. description:ID of the tax exemption.
		name:billing_address_id, type:string, required:Optional. description:This is the ID of the billing address you want to apply to the invoice. 
		name:shipping_address_id, type:string, required:Optional. description:This is the ID of the shipping address you want to apply to the invoice. 
		name:avatax_use_code, type:string, required:Optional. description:Used to group like customers for exemption purposes. It is a custom value that links customers to a tax rule. Select from Avalara [standard codes][1] or enter a custom code. Max-length [25]
		name:avatax_exempt_no, type:string, required:Optional. description:Exemption certificate number of the customer. Max-length [25]
		name:tax_id, type:string, required:Optional. description:ID of the tax.
		name:expense_id, type:string, required:Optional. description:Add billable expense id which needs to be convert to invoice
		name:salesorder_item_id, type:string, required:Optional. description:ID of the sales order line item which is invoices.
		name:avatax_tax_code, type:string, required:Optional. description:A tax code is a unique label used to group Items (products, services, or charges) together. Refer the [link][2] for more deails. Max-length [25]
		name:time_entry_ids, type:array, required:Optional. description:IDs of the time entries associated with the project.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def update_an_invoice_using_a_custom_field's_unique_value(self, **kwargs):
		"""A custom field will have unique values if it's configured to not accept duplicate values. Now, you can use that custom field's value to update an invoice by providing its API name in the X-Unique-Identifier-Key header and its value in the X-Unique-Identifier-Value header. Based on this value, the corresponding invoice will be retrieved and updated. Additionally, there is an optional X-Upsert header. If the X-Upsert header is true and the custom field's unique value is not found in any of the existing invoices, a new invoice will be created if the necessary payload details are available
		name:customer_id, type:string, required:Required. description:ID of the customer the invoice has to be created.
		name:currency_id, type:string, required:Optional. description:The currency id of the currency
		name:contact_persons, type:array, required:Optional. description:Array of contact person(s) for whom invoice has to be sent.
		name:invoice_number, type:string, required:Optional. description:Search invoices by invoice number.Variants: 
		name:invoice_number_startswith, type:string, required:Optional. description:Search invoices by invoice number.Variants: 
		name:invoice_number_contains, type:string, required:Optional. description:Search invoices by invoice number.Variants: 
		name:place_of_supply, type:string, required:Optional. description:Place where the goods/services are supplied to. (If not given, 
		name:vat_treatment, type:string, required:Optional. description:(Optional) VAT treatment for the invoices. VAT treatment denotes the location of the customer, if the customer resides in UK then the VAT treatment is 
		name:tax_treatment, type:string, required:Optional. description:VAT treatment for the invoice .Choose whether the contact falls under: 
		name:is_reverse_charge_applied, type:boolean, required:Optional. description:(Required if customer tax treatment is 
		name:gst_treatment, type:string, required:Optional. description:Choose whether the contact is GST registered/unregistered/consumer/overseas. Allowed values are 
		name:cfdi_usage, type:string, required:Optional. description:Choose CFDI Usage. Allowed values:
		name:cfdi_reference_type, type:string, required:Optional. description:Choose CFDI Reference Type. Allowed values:
		name:reference_invoice_id, type:string, required:Optional. description:Associate the reference invoice.
		name:gst_no, type:string, required:Optional. description:15 digit GST identification number of the customer.
		name:reference_number, type:string, required:Optional. description:The reference number of the invoice
		name:template_id, type:string, required:Optional. description:ID of the pdf template associated with the invoice.
		name:date, type:string, required:Optional. description:Search invoices by invoice date. Default date format is yyyy-mm-dd.
		name:payment_terms, type:integer, required:Optional. description:Payment terms in days e.g. 15, 30, 60. Invoice due date will be calculated based on this. Max-length [100]
		name:payment_terms_label, type:string, required:Optional. description:Used to override the default payment terms label. Default value for 15 days is "Net 15 Days". Max-length [100]
		name:due_date, type:string, required:Optional. description:Search invoices by due date. Default date format is yyyy-mm-dd. 
		name:discount, type:float, required:Optional. description:Discount applied to the invoice. It can be either in % or in amount. e.g. 12.5% or 190. Max-length [100]
		name:is_discount_before_tax, type:boolean, required:Optional. description:Used to specify how the discount has to applied. Either before or after the calculation of tax.
		name:discount_type, type:string, required:Optional. description:How the discount is specified. Allowed values: 
		name:is_inclusive_tax, type:boolean, required:Optional. description:Used to specify whether the line item rates are inclusive or exclusivr of tax.
		name:exchange_rate, type:float, required:Optional. description:Exchange rate of the currency.
		name:recurring_invoice_id, type:string, required:Optional. description:ID of the recurring invoice from which the invoice is created.
		name:invoiced_estimate_id, type:string, required:Optional. description:ID of the invoice from which the invoice is created.
		name:salesperson_name, type:string, required:Optional. description:Name of the salesperson. Max-length [200]
		name:custom_fields, type:array, required:Optional. description:Custom fields for an invoice.
			sub attributes:
			name:customfield_id, type:long, required:Optional. description:
			name:value, type:string, required:Optional. description:Value of the Custom Field
		name:line_items, type:array, required:Required. description:Search invoices by item id.
			sub attributes:
			name:item_id, type:string, required:Required. description:Search invoices by item id.
			name:project_id, type:string, required:Optional. description:ID of the Project.
			name:time_entry_ids, type:array, required:Optional. description:IDs of the time entries associated with the project.
			name:product_type, type:string, required:Optional. description:Enter
			name:hsn_or_sac, type:string, required:Optional. description:Add HSN/SAC code for your goods/services
			name:sat_item_key_code, type:string, required:Optional. description:Add SAT Item Key Code for your goods/services. Download the
			name:unitkey_code, type:string, required:Optional. description:Add SAT Unit Key Code for your goods/services. Download the
			name:warehouse_id, type:string, required:Optional. description:Enter warehouse ID
			name:expense_id, type:string, required:Optional. description:Add billable expense id which needs to be convert to invoice
			name:expense_receipt_name, type:string, required:Optional. description:
			name:name, type:string, required:Optional. description:The name of the line item. Max-length [100]
			name:description, type:string, required:Optional. description:The description of the line items. Max-length [2000]
			name:item_order, type:integer, required:Optional. description:The order of the line item_order
			name:bcy_rate, type:float, required:Optional. description:base currency rate
			name:rate, type:double, required:Optional. description:Rate of the line item.
			name:quantity, type:float, required:Optional. description:The quantity of line item
			name:unit, type:string, required:Optional. description:Unit of the line item e.g. kgs, Nos. Max-length [100]
			name:discount_amount, type:float, required:Optional. description:The discount amount on the line item
			name:tags, type:array, required:Optional. description:Filter all your reports based on the tag
			name:tag_id, type:string, required:Optional. description:ID of the reporting tag
			name:tag_option_id, type:string, required:Optional. description:ID of the reporting tag's option
			name:discount, type:float, required:Optional. description:Discount applied to the invoice. It can be either in % or in amount. e.g. 12.5% or 190. Max-length [100]
			name:tax_id, type:string, required:Optional. description:ID of the tax.
			name:tds_tax_id, type:string, required:Optional. description:ID of the TDS tax.
			name:tax_name, type:string, required:Optional. description:The name of the tax
			name:tax_type, type:string, required:Optional. description:The type of the tax
			name:tax_percentage, type:float, required:Optional. description:The  percentage of tax levied
			name:tax_treatment_code, type:string, required:Optional. description:Specify reason for using out of scope.Supported values for UAE are
			name:header_name, type:string, required:Optional. description:Name of the item header
			name:header_id, type:string, required:Optional. description:ID of the item header
		name:payment_options, type:object, required:Optional. description:Payment options for the invoice, online payment gateways and bank accounts. Will be displayed in the pdf.
			sub attributes:
			name:payment_gateways, type:array, required:Optional. description:Online payment gateways through which payment can be made.
			name:configured, type:boolean, required:Optional. description:Boolean check to see if a payment gateway has been configured
			name:additional_field1, type:string, required:Optional. description:Paypal payment method. Allowed Values:
			name:gateway_name, type:string, required:Optional. description:Name of the payment gateway associated with the invoice. E.g. paypal, stripe.Allowed Values:
		name:allow_partial_payments, type:boolean, required:Optional. description:Boolean to check if partial payments are allowed for the contact
		name:custom_body, type:string, required:Optional. description:None
		name:custom_subject, type:string, required:Optional. description:None
		name:notes, type:string, required:Optional. description:The notes added below expressing gratitude or for conveying some information.
		name:terms, type:string, required:Optional. description:The terms added below expressing gratitude or for conveying some information.
		name:shipping_charge, type:string, required:Optional. description:Shipping charges applied to the invoice. Max-length [100]
		name:adjustment, type:double, required:Optional. description:Adjustments made to the invoice.
		name:adjustment_description, type:string, required:Optional. description:Customize the adjustment description. E.g. Rounding off.
		name:reason, type:string, required:Optional. description:None
		name:tax_authority_id, type:string, required:Optional. description:ID of the tax authority. Tax authority depends on the location of the customer. For example, if the customer is located in NY, then the tax authority is NY tax authority.
		name:tax_exemption_id, type:string, required:Optional. description:ID of the tax exemption.
		name:avatax_use_code, type:string, required:Optional. description:Used to group like customers for exemption purposes. It is a custom value that links customers to a tax rule. Select from Avalara [standard codes][1] or enter a custom code. Max-length [25]
		name:avatax_exempt_no, type:string, required:Optional. description:Exemption certificate number of the customer. Max-length [25]
		name:tax_id, type:string, required:Optional. description:ID of the tax.
		name:expense_id, type:string, required:Optional. description:Add billable expense id which needs to be convert to invoice
		name:salesorder_item_id, type:string, required:Optional. description:ID of the sales order line item which is invoices.
		name:avatax_tax_code, type:string, required:Optional. description:A tax code is a unique label used to group Items (products, services, or charges) together. Refer the [link][2] for more deails. Max-length [25]
		name:line_item_id, type:string, required:Optional. description:The line item id
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def list_invoices(self, **kwargs):
		"""List all invoices with pagination.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def update_an_invoice(self, **kwargs):
		"""Update an existing invoice. To delete a line item just remove it from the line_items list.
		name:customer_id, type:string, required:Required. description:ID of the customer the invoice has to be created.
		name:currency_id, type:string, required:Optional. description:The currency id of the currency
		name:contact_persons, type:array, required:Optional. description:Array of contact person(s) for whom invoice has to be sent.
		name:invoice_number, type:string, required:Optional. description:Search invoices by invoice number.Variants: 
		name:invoice_number_startswith, type:string, required:Optional. description:Search invoices by invoice number.Variants: 
		name:invoice_number_contains, type:string, required:Optional. description:Search invoices by invoice number.Variants: 
		name:place_of_supply, type:string, required:Optional. description:Place where the goods/services are supplied to. (If not given, 
		name:vat_treatment, type:string, required:Optional. description:(Optional) VAT treatment for the invoices. VAT treatment denotes the location of the customer, if the customer resides in UK then the VAT treatment is 
		name:tax_treatment, type:string, required:Optional. description:VAT treatment for the invoice .Choose whether the contact falls under: 
		name:is_reverse_charge_applied, type:boolean, required:Optional. description:(Required if customer tax treatment is 
		name:gst_treatment, type:string, required:Optional. description:Choose whether the contact is GST registered/unregistered/consumer/overseas. Allowed values are 
		name:cfdi_usage, type:string, required:Optional. description:Choose CFDI Usage. Allowed values:
		name:cfdi_reference_type, type:string, required:Optional. description:Choose CFDI Reference Type. Allowed values:
		name:reference_invoice_id, type:string, required:Optional. description:Associate the reference invoice.
		name:gst_no, type:string, required:Optional. description:15 digit GST identification number of the customer.
		name:reference_number, type:string, required:Optional. description:The reference number of the invoice
		name:template_id, type:string, required:Optional. description:ID of the pdf template associated with the invoice.
		name:date, type:string, required:Optional. description:Search invoices by invoice date. Default date format is yyyy-mm-dd.
		name:payment_terms, type:integer, required:Optional. description:Payment terms in days e.g. 15, 30, 60. Invoice due date will be calculated based on this. Max-length [100]
		name:payment_terms_label, type:string, required:Optional. description:Used to override the default payment terms label. Default value for 15 days is "Net 15 Days". Max-length [100]
		name:due_date, type:string, required:Optional. description:Search invoices by due date. Default date format is yyyy-mm-dd. 
		name:discount, type:float, required:Optional. description:Discount applied to the invoice. It can be either in % or in amount. e.g. 12.5% or 190. Max-length [100]
		name:is_discount_before_tax, type:boolean, required:Optional. description:Used to specify how the discount has to applied. Either before or after the calculation of tax.
		name:discount_type, type:string, required:Optional. description:How the discount is specified. Allowed values: 
		name:is_inclusive_tax, type:boolean, required:Optional. description:Used to specify whether the line item rates are inclusive or exclusivr of tax.
		name:exchange_rate, type:float, required:Optional. description:Exchange rate of the currency.
		name:recurring_invoice_id, type:string, required:Optional. description:ID of the recurring invoice from which the invoice is created.
		name:invoiced_estimate_id, type:string, required:Optional. description:ID of the invoice from which the invoice is created.
		name:salesperson_name, type:string, required:Optional. description:Name of the salesperson. Max-length [200]
		name:custom_fields, type:array, required:Optional. description:Custom fields for an invoice.
			sub attributes:
			name:customfield_id, type:long, required:Optional. description:
			name:value, type:string, required:Optional. description:Value of the Custom Field
		name:line_items, type:array, required:Required. description:Search invoices by item id.
			sub attributes:
			name:item_id, type:string, required:Required. description:Search invoices by item id.
			name:project_id, type:string, required:Optional. description:ID of the Project.
			name:time_entry_ids, type:array, required:Optional. description:IDs of the time entries associated with the project.
			name:product_type, type:string, required:Optional. description:Enter
			name:hsn_or_sac, type:string, required:Optional. description:Add HSN/SAC code for your goods/services
			name:sat_item_key_code, type:string, required:Optional. description:Add SAT Item Key Code for your goods/services. Download the
			name:unitkey_code, type:string, required:Optional. description:Add SAT Unit Key Code for your goods/services. Download the
			name:warehouse_id, type:string, required:Optional. description:Enter warehouse ID
			name:expense_id, type:string, required:Optional. description:Add billable expense id which needs to be convert to invoice
			name:expense_receipt_name, type:string, required:Optional. description:
			name:name, type:string, required:Optional. description:The name of the line item. Max-length [100]
			name:description, type:string, required:Optional. description:The description of the line items. Max-length [2000]
			name:item_order, type:integer, required:Optional. description:The order of the line item_order
			name:bcy_rate, type:float, required:Optional. description:base currency rate
			name:rate, type:double, required:Optional. description:Rate of the line item.
			name:quantity, type:float, required:Optional. description:The quantity of line item
			name:unit, type:string, required:Optional. description:Unit of the line item e.g. kgs, Nos. Max-length [100]
			name:discount_amount, type:float, required:Optional. description:The discount amount on the line item
			name:tags, type:array, required:Optional. description:Filter all your reports based on the tag
			name:tag_id, type:string, required:Optional. description:ID of the reporting tag
			name:tag_option_id, type:string, required:Optional. description:ID of the reporting tag's option
			name:discount, type:float, required:Optional. description:Discount applied to the invoice. It can be either in % or in amount. e.g. 12.5% or 190. Max-length [100]
			name:tax_id, type:string, required:Optional. description:ID of the tax.
			name:tds_tax_id, type:string, required:Optional. description:ID of the TDS tax.
			name:tax_name, type:string, required:Optional. description:The name of the tax
			name:tax_type, type:string, required:Optional. description:The type of the tax
			name:tax_percentage, type:float, required:Optional. description:The  percentage of tax levied
			name:tax_treatment_code, type:string, required:Optional. description:Specify reason for using out of scope.Supported values for UAE are
			name:header_name, type:string, required:Optional. description:Name of the item header
			name:header_id, type:string, required:Optional. description:ID of the item header
		name:payment_options, type:object, required:Optional. description:Payment options for the invoice, online payment gateways and bank accounts. Will be displayed in the pdf.
			sub attributes:
			name:payment_gateways, type:array, required:Optional. description:Online payment gateways through which payment can be made.
			name:configured, type:boolean, required:Optional. description:Boolean check to see if a payment gateway has been configured
			name:additional_field1, type:string, required:Optional. description:Paypal payment method. Allowed Values:
			name:gateway_name, type:string, required:Optional. description:Name of the payment gateway associated with the invoice. E.g. paypal, stripe.Allowed Values:
		name:allow_partial_payments, type:boolean, required:Optional. description:Boolean to check if partial payments are allowed for the contact
		name:custom_body, type:string, required:Optional. description:None
		name:custom_subject, type:string, required:Optional. description:None
		name:notes, type:string, required:Optional. description:The notes added below expressing gratitude or for conveying some information.
		name:terms, type:string, required:Optional. description:The terms added below expressing gratitude or for conveying some information.
		name:shipping_charge, type:string, required:Optional. description:Shipping charges applied to the invoice. Max-length [100]
		name:adjustment, type:double, required:Optional. description:Adjustments made to the invoice.
		name:adjustment_description, type:string, required:Optional. description:Customize the adjustment description. E.g. Rounding off.
		name:reason, type:string, required:Optional. description:None
		name:tax_authority_id, type:string, required:Optional. description:ID of the tax authority. Tax authority depends on the location of the customer. For example, if the customer is located in NY, then the tax authority is NY tax authority.
		name:tax_exemption_id, type:string, required:Optional. description:ID of the tax exemption.
		name:avatax_use_code, type:string, required:Optional. description:Used to group like customers for exemption purposes. It is a custom value that links customers to a tax rule. Select from Avalara [standard codes][1] or enter a custom code. Max-length [25]
		name:avatax_exempt_no, type:string, required:Optional. description:Exemption certificate number of the customer. Max-length [25]
		name:tax_id, type:string, required:Optional. description:ID of the tax.
		name:expense_id, type:string, required:Optional. description:Add billable expense id which needs to be convert to invoice
		name:salesorder_item_id, type:string, required:Optional. description:ID of the sales order line item which is invoices.
		name:avatax_tax_code, type:string, required:Optional. description:A tax code is a unique label used to group Items (products, services, or charges) together. Refer the [link][2] for more deails. Max-length [25]
		name:line_item_id, type:string, required:Optional. description:The line item id
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def get_an_invoice(self, **kwargs):
		"""Get the details of an invoice.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def delete_an_invoice(self, **kwargs):
		"""Delete an existing invoice. Invoices which have payment or credits note applied cannot be deleted.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def mark_an_invoice_as_sent(self, **kwargs):
		"""Mark a draft invoice as sent.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def void_an_invoice(self, **kwargs):
		"""Mark an invoice status as void. Upon voiding, the payments and credits associated with the invoices will be unassociated and will be under customer credits.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def mark_as_draft(self, **kwargs):
		"""Mark a voided invoice as draft.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def email_invoices(self, **kwargs):
		"""Send invoices to your customers by email. Maximum of 10 invoices can be sent at once.
		name:contacts, type:array, required:Optional. description:Contacts for whom email or snail mail has to be sent.
		name:contact_id, type:string, required:Required. description:ID of the contact. Can specify if email or snail mail has to be sent for each contact.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def create_an_instant_invoice(self, **kwargs):
		"""Create an instant invoice for all the confirmed sales orders you have selected.
		name:salesorder_id, type:string, required:Optional. description:ID of the salesorder
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def submit_an_invoice_for_approval(self, **kwargs):
		"""Submit an invoice for approval.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def approve_an_invoice(self, **kwargs):
		"""Approve an invoice.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def email_an_invoice(self, **kwargs):
		"""Email an invoice to the customer. Input json string is not mandatory. If input json string is empty, mail will be send with default mail content.
		name:send_from_org_email_id, type:boolean, required:Optional. description:Boolean to trigger the email from the organization's email address
		name:to_mail_ids, type:array, required:Required. description:Array of email address of the recipients.
		name:cc_mail_ids, type:array, required:Optional. description:Array of email address of the recipients to be cced.
		name:subject, type:string, required:Optional. description:The subject of the mail
		name:body, type:string, required:Optional. description:The body of the mail
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def get_invoice_email_content(self, **kwargs):
		"""Get the email content of an invoice.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def remind_customer(self, **kwargs):
		"""Remind your customer about an unpaid invoice by email. Reminder will be sent, only for the invoices which are in open or overdue status.
		name:to_mail_ids, type:array, required:Optional. description:Array of email address of the recipients.
		name:cc_mail_ids, type:array, required:Required. description:Array of email address of the recipients to be cced.
		name:subject, type:string, required:Optional. description:The subject of the mail
		name:body, type:string, required:Optional. description:The body of the mail
		name:send_from_org_email_id, type:boolean, required:Optional. description:Boolean to trigger the email from the organization's email address
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def get_payment_reminder_mail_content(self, **kwargs):
		"""Get the mail content of the payment reminder.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def bulk_invoice_reminder(self, **kwargs):
		"""Remind your customer about an unpaid invoices by email. Reminder mail will be send, only for the invoices is in open or overdue status. Maximum 10 invoices can be reminded at once.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def bulk_export_invoices(self, **kwargs):
		"""Maximum of 25 invoices can be exported in a single pdf.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def bulk_print_invoices(self, **kwargs):
		"""Export invoices as pdf and print them. Maximum of 25 invoices can be printed.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def disable_payment_reminder(self, **kwargs):
		"""Disable automated payment reminders for an invoice.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def enable_payment_reminder(self, **kwargs):
		"""Enable automated payment reminders for an invoice.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def write_off_invoice(self, **kwargs):
		"""Write off the invoice balance amount of an invoice.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def cancel_write_off(self, **kwargs):
		"""Cancel the write off amount of an invoice.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def update_billing_address(self, **kwargs):
		"""Updates the billing address for this invoice alone.
		name:address, type:string, required:Optional. description:Billing address for the invoice
		name:city, type:string, required:Optional. description:City of the customer’s billing address.
		name:state, type:string, required:Optional. description:State of the customer’s billing address.
		name:zip, type:string, required:Optional. description:Zip code of the customer’s billing address.
		name:country, type:string, required:Optional. description:Country of the customer’s billing address.
		name:fax, type:string, required:Optional. description:Customer's fax number.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def update_shipping_address(self, **kwargs):
		"""Updates the shipping address for this invoice alone.
		name:address, type:string, required:Optional. description:Shipping address for the invoice
		name:street2, type:string, required:Optional. description:None
		name:city, type:string, required:Optional. description:City of the customer’s Shipping address.
		name:state, type:string, required:Optional. description:State of the customer’s Shipping address.
		name:zip, type:string, required:Optional. description:Zip code of the customer’s Shipping address.
		name:country, type:string, required:Optional. description:Country of the customer’s Shipping address.
		name:fax, type:string, required:Optional. description:Customer's fax number.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def list_invoice_templates(self, **kwargs):
		"""Get all invoice pdf templates.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def update_invoice_template(self, **kwargs):
		"""Update the pdf template associated with the invoice.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def list_invoice_payments(self, **kwargs):
		"""Get the list of payments made for an invoice.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def list_credits_applied(self, **kwargs):
		"""Get the list of credits applied for an invoice.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def apply_credits(self, **kwargs):
		"""Apply the customer credits either from credit notes or excess customer payments to an invoice. Multiple credits can be applied at once.
		name:invoice_payments, type:array, required:Required. description:ID of the payment
			sub attributes:
			name:payment_id, type:string, required:Optional. description:ID of the payment
			name:amount_applied, type:float, required:Optional. description:The applied amount to the creditnote
		name:apply_creditnotes, type:array, required:Required. description:ID of the creditnote
			sub attributes:
			name:creditnote_id, type:string, required:Optional. description:ID of the creditnote
			name:amount_applied, type:float, required:Optional. description:The applied amount to the creditnote
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def delete_a_payment(self, **kwargs):
		"""Delete a payment made to an invoice.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def delete__applied_credit(self, **kwargs):
		"""Delete a particular credit applied to an invoice.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def add_attachment_to_an_invoice(self, **kwargs):
		"""Attach a file to an invoice.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def update_attachment_preference(self, **kwargs):
		"""Set whether you want to send the attached file while emailing the invoice.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def get_an_invoice_attachment(self, **kwargs):
		"""Returns the file attached to the invoice.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def delete_an_attachment(self, **kwargs):
		"""Delete the file attached to the invoice.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def delete_the_expense_receipt(self, **kwargs):
		"""Delete the expense receipts attached to an invoice which is raised from an expense.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def update_custom_field_in_existing_invoices(self, **kwargs):
		"""Update the value of the custom field in existing invoices.
		name:customfield_id, type:long, required:Optional. description:None
		name:value, type:string, required:Optional. description:Value of the Custom Field
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def add_comment(self, **kwargs):
		"""Add a comment for an invoice.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def list_invoice_comments_and_history(self, **kwargs):
		"""Get the complete history and comments of an invoice.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def update_comment(self, **kwargs):
		"""Update an existing comment of an invoice.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def delete_a_comment(self, **kwargs):
		"""Delete an invoice comment.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


	def generate_payment_link(self, **kwargs):
		"""This API generates a payment link for the invoice with an expiry date.
		"""
		api_url = self.zoho_books_api + '/invoices'
		default_params = {
		}

		default_params.update(kwargs)
		headers = {
			'Authorization': f'Zoho-oauthtoken {self.access_token}'
		}

		return self.zoho_get_api_call(api_url, default_params, headers, 'invoices')


