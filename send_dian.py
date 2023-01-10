from datetime import date
import json, requests,os

class SEND_DIAN:
	def __init__(self,invoice):
		self.invoice = invoice

	def Days(self,d):
		future_date = date(d[0], d[1], d[2])
		today = date.today()
		_days = (future_date - today).days
		return _days

	def Information(self):
		return {
			"number": self.invoice.last().consecutive,
			"type_document_id": 1,
			"date": "2023-01-06",
			"time": "04:08:12",
			"resolution_number": "18764042060055",
			"prefix": "FFET",
		   "notes": "ESTA ES UNA NOTA DE PRUEBA",
		   "disable_confirmation_text": True,
		   "establishment_name": "TORRE SOFTWARE",
		   "establishment_address": "BRR LIMONAR MZ 6 CS 3 ET 1 PISO 2",
		   "establishment_phone": "3226563672",
		   "establishment_municipality": 1,
		   "foot_note": "PRUEBA DE TEXTO LIBRE QUE DEBE POSICIONARSE EN EL PIE DE PAGINA DE LA REPRESENTACION GRAFICA DE LA FACTURA ELECTRONICA VALIDACION PREVIA DIAN"
		}

	def Customer(self):
		c = self.invoice.last().client
		return {
			"identification_number": str(c.identification_number)[:-1],
			"dv": c.dv,
			"name": c.name,
			"phone": c.phone,
			"address": c.address,
			"email": c.email,
			"merchant_registration": "0000000-00" if c.merchant_registration is None else c.merchant_registration,
			"type_document_identification_id": c.type_documentI._id,
			"type_organization_id": c.type_organization._id,
	      "type_liability_id": 7,
			"municipality_id": c.municipality._id,
			"type_regime_id": c.type_regime._id
		}

	def Payment_Form(self):
		pf = self.invoice.last()
		date_ = str(pf.date_expired)
		_date = date_.split('-')
		dates = list(map(int, _date))
		days = self.Days(dates)
		return {
			"payment_form_id": pf.payment_form._id,
			"payment_method_id": 30 if pf.payment_form._id == 2 else 10,
			"payment_due_date": pf.date_expired,
			"duration_measure": days
		}

	def Monetary_Totals(self):
		subtotal = 0; total = 0

		for i in self.invoice:
			subtotal += i.Base_Product()
			total += i.Total_Product()
		return {
			"line_extension_amount": round(subtotal),
			"tax_exclusive_amount": round(subtotal),
			"tax_inclusive_amount": round(total),
			"payable_amount": round(total)
		}
	
	def VALUES_TAXES(self,tax,data):
		total_base = 0
		total_tax = 0
		for i in data:
			if tax == i.tax:
				total_base += i.SubTotal_Product()
				total_tax = i.Tax_Product()
		return {str(tax):total_tax,'base':total_base}

	def Tax_Totals(self):
		taxes = []
		tax_19 = self.VALUES_TAXES(19,self.invoice)
		tax_5 = self.VALUES_TAXES(5,self.invoice)
		tax_0 = self.VALUES_TAXES(0,self.invoice)
		if int(tax_19['base']) != 0:
			taxes.append({
				"tax_id": 1,
				"tax_amount": str(tax_19['19']),
				"percent": "19",
				"taxable_amount": str(tax_19['base'])
			})
		elif int(tax_5['base']) != 0:
			taxes.append({
				"tax_id": 1,
				"tax_amount": str(tax_5['5']),
				"percent": "5",
				"taxable_amount": str(tax_5['base'])
			})
		elif int(tax_0['base']) != 0:
			taxes.append({
				"tax_id": 1,
				"tax_amount": str(tax_0['0']),
				"percent": "0",
				"taxable_amount": str(tax_0['base'])
			})
		return taxes

	def Invoice_Lines(self):
		return [
			{
				"unit_measure_id": 70,
				"invoiced_quantity": str(i.quanty),
				"line_extension_amount": i.Base_Product(),
				"free_of_charge_indicator": False,
				"tax_totals": [
					{
						"tax_id": 1,
						"tax_amount": i.Tax_Product(),
						"taxable_amount": i.Base_Product(),
						"percent": i.tax
					}
				],
				"description": i.description,
	         "notes": "",
				"code": str(i.code),
				"type_item_identification_id": 4,
				"price_amount": str(i.price),
				"base_quantity": "1"
			}
			for i in self.invoice
		]

	def Operations(self):
		url = "http://localhost/apidian2021/public/api/ubl2.1/invoice"
		headers = {
		  'Content-Type': 'application/json',
		  'Accept': 'application/json',
		  'Authorization': 'Bearer fbcaff08718a4625e4885e76ac190d6cade6c001480ef6977994ece1829496f7'
		}
		data = self.Information()
		data['customer'] = self.Customer()
		data['payment_form'] = self.Payment_Form()
		data['legal_monetary_totals'] = self.Monetary_Totals()
		data['tax_totals'] = self.Tax_Totals()
		data['invoice_lines'] = self.Invoice_Lines()
		payload = json.dumps(data)
		print(payload)
		response = requests.request("POST", url, headers=headers, data=payload)
		response_dict = json.loads(response.text)
		message = None
		if int(response.status_code) == 200:
			message = response_dict['ResponseDian']['Envelope']['Body']['SendBillSyncResponse']['SendBillSyncResult']["StatusDescription"]
			if "Documento procesado anteriormente." in response_dict['ResponseDian']['Envelope']['Body']['SendBillSyncResponse']['SendBillSyncResult']['ErrorMessage']['string']:
				message = "Documento procesado anteriormente."
			elif "errors" in response_dict['ResponseDian']['Envelope']['Body']['SendBillSyncResponse']['SendBillSyncResult']['ErrorMessage']['string']:
				message = response_dict['ResponseDian']['Envelope']['Body']['SendBillSyncResponse']['SendBillSyncResult']['ErrorMessage']['string']['errors']['errors']
			for i in self.invoice:
				i.state = message
				i.save()
		else:
			message = "Por favor intentar mas tarde"
			for i in self.invoice:
				i.state = message
				i.save()
		response.connection.close()
		return message








